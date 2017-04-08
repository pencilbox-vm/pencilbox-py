#encoding=utf-8

EOT = [3, 0]

opdata_list = [
  "sot",
  "iot",
  "int8",
  "uint8",
  "int16",
  "uint16",
  "int32",
  "uint32",
  "float32",
  "float64"
]

_Opdata = {}
index = 0
for item in opdata_list:
  _Opdata[item] = index
  index += 1

opimplicit_list = [
  "textstack",
  "sweep",
  "sweepn",
  "jump",
  "jumpoffset",
  "localfget"
]
_Opimplicit = {}
index = 16
for item in opimplicit_list:
  _Opimplicit[item] = index
  index += 1

opexplicit_list = [
  "scope",
  "get",
  "func",
  "apply",
  "print",
  "add",
  "sub",
  "div",
  "mul",
  "mod",
  "envGet",
  "envSet",
  "if",
  "eq",
  "gt",
  "ge",
  "lt",
  "le",
  "list",
  "index",
  "pop",
  "push",
  "shift",
  "unshift",

  # canvas properties
  "canvas",
  "fillStyle",
  "font",
  "globalAlpha",
  "globalCompositeOperation",
  "lineCap",
  "lineDashOffset",
  "lineJoin",
  "lineWidth",
  "miterLimit",
  "shadowBlur",
  "shadowColor",
  "shadowOffsetX",
  "shadowOffsetY",
  "strokeStyle",
  "textAlign",
  "textBaseline",

  # canvas methods
  "arc",
  "arcTo",
  "beginPath",
  "bezierCurveTo",
  "clearRect",
  "clip",
  "closePath",
  "createImageData",
  "createLinearGradient",
  "addColorStop",
  "createPattern",
  "createRadialGradient",
  "drawImage",
  "ellipse",
  "fill",
  "fillRect",
  "fillText",
  "getImageData",
  "getLineDash",
  "isPointInPath",
  "isPointInStroke",
  "lineTo",
  "measureText",
  "moveTo",
  "putImageData",
  "quadraticCurveTo",
  "rect",
  "restore",
  "rotate",
  "save",
  "scale",
  "setLineDash",
  "setTransform",
  "stroke",
  "strokeRect",
  "strokeText",
  "transform",
  "translate"
]


_Opexplicit = {}
index = 31
for item in opexplicit_list:
  _Opexplicit[item] = index
  index += 1


class Opdata():
  def __getattr__(self, item):
    item = item.replace("_", "")
    return _Opdata[item]

  def __iter__(self):
    for item in _Opdata:
      yield _Opdata[item]


class Opimplicit():
  def __getattr__(self, item):
    item = item.replace("_", "")
    return _Opimplicit[item]

  def __iter__(self):
    for item in _Opimplicit:
      yield _Opimplicit[item]


class Opexplicit():
  def __getattr__(self, item):
    item = item.replace("_", "")
    return _Opexplicit[item]

  def __iter__(self):
    for item in _Opexplicit:
      yield _Opexplicit[item]

class Op():
  def __getattr__(self, item):
    item = item.replace("_", "")
    if item == "func" or item == "scope":
      return lambda *x : lambda *y : [_Opexplicit[item], x] + list(y)
    else:
      return lambda *x : [_Opexplicit[item]] + list(x)


opdata = Opdata()
opimplicit = Opimplicit()
opexplicit = Opexplicit()

op = Op()

OpOnlyTwoParams = set([
  opexplicit.eq,
  opexplicit.gt,
  opexplicit.ge,
  opexplicit.lt,
  opexplicit.le,

  opexplicit.add,
  opexplicit.sub,
  opexplicit.mul,
  opexplicit.div,
  opexplicit.mod
])