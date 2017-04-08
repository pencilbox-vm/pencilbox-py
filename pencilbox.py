#encoding=utf-8

import struct
from definition import EOT, opdata, opimplicit, opexplicit, op, OpOnlyTwoParams

class Compiler():
  def __init__(self):
    self.textstack_bytes = [opimplicit.textstack, 0, 0, 0, 0]
    self.textstack_map = {}
    self.textstack_index = 0
    self.bytecodes = []

  def walk(self, node, varstack, varstack_callindex):
    if type(node) == list:
      code = node[0]

      if code == opexplicit.scope:

        params = node[1]

        # params[0] is the variable name
        # params[1] is the content
        if len(params) >= 2:
          varstack.append(params[0])

          self.walk(params[1], varstack, varstack_callindex)

          self.bytecodes.append(code)

        for item in node[2:]:
          self.walk(item, varstack, varstack_callindex)

        if len(params) >= 2:
          varstack.pop()
          self.bytecodes.append(opimplicit.sweep)

      elif code == opexplicit.get:

        name = node[1]
        not_found = True

        for index in range(0, len(varstack))[::-1]:
          if name == varstack[index]:
            if index < varstack_callindex:
              self.bytecodes.append(opexplicit.get)
              self.bytecodes.append(index)
            else:
              self.bytecodes.append(opimplicit.localfget)
              self.bytecodes.append(index - varstack_callindex)

            not_found = False
            break

        if not_found:
          raise Exception("no variable " + name + " in scope")

      elif code == opexplicit.func:

        self.bytecodes.append(code)

        # ======= set the length of function body ========
        self.bytecodes.append(0)
        self.bytecodes.append(0)
        self.bytecodes.append(0)
        self.bytecodes.append(0)

        # ========= push variables to var stack ==========
        bytecodes_len = len(self.bytecodes)
        params = node[1]

        self.bytecodes.append(len(params))

        varstack_callindex = len(varstack)

        for item in params:
          varstack.append(item)

        # ========= walk through function body ==========
        for item in node[2:]:
          self.walk(item, varstack, varstack_callindex)

        # ========= jump back to origin pc =============
        self.bytecodes.append(opimplicit.sweepn)
        self.bytecodes.append(opimplicit.jump)

        # ========= cleanup ==========
        params_len = len(params)
        while params_len:
          params_len -= 1
          varstack.pop()


        # ========= set function body length ============
        offset_bytes = struct.unpack("BBBB", struct.pack("I", len(self.bytecodes) - bytecodes_len))
        self.bytecodes[bytecodes_len - 4] = offset_bytes[0]
        self.bytecodes[bytecodes_len - 3] = offset_bytes[1]
        self.bytecodes[bytecodes_len - 2] = offset_bytes[2]
        self.bytecodes[bytecodes_len - 1] = offset_bytes[3]

      elif code == opexplicit._if:

        # push condition on stack
        self.walk(node[1], varstack, varstack_callindex)

        self.bytecodes.append(code)

        # else branch address
        else_val_address = len(self.bytecodes)
        self.bytecodes.append(0)
        self.bytecodes.append(0)
        self.bytecodes.append(0)
        self.bytecodes.append(0)

        # body of branch true
        self.walk(node[2], varstack, varstack_callindex)

        # exit address
        self.bytecodes.append(opdata.uint32)

        exit_val_address = len(self.bytecodes)
        self.bytecodes.append(0)
        self.bytecodes.append(0)
        self.bytecodes.append(0)
        self.bytecodes.append(0)

        self.bytecodes.append(opimplicit.jumpoffset)

        offset_bytes = struct.unpack("BBBB", struct.pack("I", len(self.bytecodes) - else_val_address))
        self.bytecodes[else_val_address + 0] = offset_bytes[0]
        self.bytecodes[else_val_address + 1] = offset_bytes[1]
        self.bytecodes[else_val_address + 2] = offset_bytes[2]
        self.bytecodes[else_val_address + 3] = offset_bytes[3]

        # body of branch false
        self.walk(node[3], varstack, varstack_callindex)

        exit_address_bytes = struct.unpack("BBBB", struct.pack("I", len(self.bytecodes) - (exit_val_address + 5)))
        self.bytecodes[exit_val_address + 0] = exit_address_bytes[0]
        self.bytecodes[exit_val_address + 1] = exit_address_bytes[1]
        self.bytecodes[exit_val_address + 2] = exit_address_bytes[2]
        self.bytecodes[exit_val_address + 3] = exit_address_bytes[3]

      else:

        for item in node[1:]:
          self.walk(item, varstack, varstack_callindex)

        self.bytecodes.append(code)

        if code in opexplicit and not code in OpOnlyTwoParams:
          self.bytecodes.append(len(node) - 1)



    elif type(node) == int or type(node) == float:
      num_type = None
      struct_type = None

      if type(node) == int:
        # is int

        if node >= 0:
          if node <= 255:
            num_type = opdata.uint8
            struct_type = ("B", "B")
          elif node <= 65535:
            num_type = opdata.uint16
            struct_type = ("H", "BB")
          elif node <= 4294967295:
            num_type = opdata.uint32
            struct_type = ("I", "BBBB")
          else:
            num_type = opdata.float64
            struct_type = ("Q", "BBBBBBBB")
        else:
          if node >= -128:
            num_type = opdata.int8
            struct_type = ("b", "B")
          elif node >= -32768:
            num_type = opdata.int16
            struct_type = ("h", "BB")
          elif node >= -2147483648:
            num_type = opdata.int32
            struct_type = ("i", "BBBB")
          else:
            num_type = opdata.float64
            struct_type = ("q", "BBBBBBBB")

      else:
        # is float

        num_type = opdata.float32
        struct_type = ("f", "BBBB")

      result = [num_type] + list(struct.unpack(struct_type[1], struct.pack(struct_type[0], node)))
      self.bytecodes += result


    elif type(node) == str:

      self.bytecodes.append(opdata.iot)

      if node in self.textstack_map:

        self.walk(self.textstack_map[node], [], 0)

      else:

        for char in node:
          self.textstack_bytes += list(struct.unpack('HBB', char.encode('utf-16'))[1:])

        self.textstack_bytes += EOT

        self.textstack_map[node] = self.textstack_index

        self.walk(self.textstack_index, [], 0)

        self.textstack_index += 1

  def compile(self, *ast_list):
    for ast in ast_list:
      self.walk(ast, [], float("inf"))

      offset_bytes = struct.unpack("BBBB", struct.pack("I", len(self.textstack_bytes) - 1))
      self.textstack_bytes[1] = offset_bytes[0]
      self.textstack_bytes[2] = offset_bytes[1]
      self.textstack_bytes[3] = offset_bytes[2]
      self.textstack_bytes[4] = offset_bytes[3]

