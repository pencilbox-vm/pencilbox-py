from definition import _Opexplicit

class Op():
  def __getattr__(self, item):
    if item == "func" or item == "scope":
      return lambda *x : lambda *y : [_Opexplicit[item], x] + list(y)
    else:
      return lambda *x : [_Opexplicit[item]] + list(x)

op = Op()