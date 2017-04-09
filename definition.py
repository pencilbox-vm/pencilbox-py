#encoding=utf-8

EOT = [3, 0]

# ========= opdata define ===========
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

class Opdata():
  def __getattr__(self, item):
    return _Opdata[item]

  def __iter__(self):
    for item in _Opdata:
      yield _Opdata[item]


# ============= opimplicit define ===========
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

class Opimplicit():
  def __getattr__(self, item):
    return _Opimplicit[item]

  def __iter__(self):
    for item in _Opimplicit:
      yield _Opimplicit[item]



# ============== opexplicit define =============
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
  "ifElse",
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

class Opexplicit():
  def __getattr__(self, item):
    return _Opexplicit[item]

  def __iter__(self):
    for item in _Opexplicit:
      yield _Opexplicit[item]

opdata = Opdata()
opimplicit = Opimplicit()
opexplicit = Opexplicit()

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