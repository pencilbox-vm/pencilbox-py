from dsl import op
from compiler import Compiler

from random import random

ast = op.scope('fib',
    op.func('n')(
      op.ifElse(
        op.lt(op.get('n'), 2),
        op.get('n'),
        op.add(
          op.apply(op.get('fib'), op.sub(op.get('n'), 1)),
          op.apply(op.get('fib'), op.sub(op.get('n'), 2))
        )
      )
    )
  )(
    op.print('fib 30 of pencilbox', op.apply(op.get('fib'), 30))
  )

ast2 = op.scope('f',
  op.func('a', 'b')(
    op.scope('f-nest',
      op.func('x', 'y')(
        op.add(op.get('x'), op.get('y'))
      )
    )(
      op.apply(op.get('f-nest'), op.get('a'), op.get('b'))
    )
  )
)(
  op.print('eq: ', op.eq(9, op.apply(op.get('f'), 3, 6)))
)

compiler = Compiler()
compiler.compile(ast, ast2)
print('fib')
print(compiler.output())


colors = []
for i in range(0, 1000):
  colors.append("rgba(" + str(int(random() * 250)) + "," + str(int(random() * 250)) + "," + str(int(random() * 250)) + ",1)")

compiler_web = Compiler()
compiler_web.compile(
  op.print(op.canvas()),
  op.font('14px Helvatica, Arial'),
  op.globalAlpha(0.8),
  op.globalCompositeOperation('exclusion'),
  op.lineCap('round'),
  op.lineDashOffset(3),
  op.lineJoin('miter'),
  op.miterLimit(2),
  op.shadowColor('black'),
  op.shadowBlur(5),
  op.shadowOffsetX(3),
  op.shadowOffsetY(3),
  op.textAlign('center'),
  op.textBaseline('bottom')
)

compiler_web.compile(
  op.beginPath(),
  op.rect(0,0,50,50),
  op.arc(25, 25, 25, 0, 1.5 * 3.14159265359),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke()
)

compiler_web.compile(
  op.beginPath(),
  op.rect(50,0,100,100),
  op.arcTo(50, 0, 100, 32, 23),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke()
)

compiler_web.compile(
  op.beginPath(),
  op.rect(150,0,100,100),
  op.moveTo(150, 0),
  op.lineTo(250, 100),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke()
)

compiler_web.compile(
  op.beginPath(),
  op.rect(250,0,100,100),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke(),
  op.beginPath(),
  op.rect(300, 50, 100, 100),
  op.rect(200, -50, 100, 100),
  op.closePath(),
  op.save(),
  op.clip(),
  op.fillStyle(colors.pop()),
  op.fillRect(250, 0, 100, 100),
  op.restore()
)

compiler_web.compile(
  op.envSet('createImageData', op.createImageData(100, 100))
)

compiler_web.compile(
  op.scope('g', op.createLinearGradient(350, 0, 450, 150))(
    op.addColorStop(op.get('g'), 0, colors.pop()),
    op.addColorStop(op.get('g'), 1, colors.pop()),
    op.fillStyle(op.get('g')),
    op.fillRect(350, 0, 100, 100)
  )
)

compiler_web.compile(
  op.clearRect(390,40,20,20)
)

compiler_web.compile(
  op.envSet('getImageData', op.getImageData(0,0,1000,500))
)

compiler_web.compile(
  op.fillStyle(op.createPattern(op.envGet('pattern_img'), 'repeat')),
  op.fillRect(450, 0, 100, 100)
)

compiler_web.compile(
  op.scope('g', op.createRadialGradient(600, 50, 100, 600, 50, 0))(
    op.addColorStop(op.get('g'), 0, colors.pop()),
    op.addColorStop(op.get('g'), 1, colors.pop()),
    op.fillStyle(op.get('g')),
    op.fillRect(550, 0, 100, 100)
  )
)

compiler_web.compile(
  op.drawImage(op.envGet('pattern_img'), 0, 0, 100, 100, 650, 0, 100, 100),
  op.drawImage(op.envGet('pattern_img'), 700, 0, 50, 50)
)

compiler_web.compile(
  op.beginPath(),
  op.rect(750,0,100,100),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke(),

  op.beginPath(),
  op.ellipse(800, 50, 25, 50, 45 * 3.14159265359/180, 0, 2 * 3.14159265359),
  op.closePath(),
  op.stroke()
)

compiler_web.compile(
  op.beginPath(),
  op.rect(850, 0, 100, 100),
  op.closePath(),
  op.fillStyle(colors.pop()),
  op.fill(),
  op.fillStyle(colors.pop()),
  op.fillText('fillText填充文本', 850, 40),
  op.fillText('テキストを入力します', 850, 60)
)

compiler_web.compile(
  op.translate(200, 200),
  op.lineWidth(20),
  op.beginPath(),
  op.moveTo(20, 20),
  op.lineTo(80, 20),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke(),

  op.beginPath(),
  op.moveTo(20, 20),
  op.lineTo(80, 80),
  op.lineTo(20, 80),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke(),
  op.lineWidth(1),
  op.translate(-200, -200)
)

compiler_web.compile(
  op.setLineDash(5, 5),
  op.print(op.getLineDash())
)

compiler_web.compile(
  op.beginPath(),
  op.rect(0, 100, 100, 100),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke(),
  op.fillStyle(colors.pop()),
  op.fillText(op.add('40,150 ', op.isPointInPath(40, 150)), 10, 160),
  op.fillText(op.add('40,0 ', op.isPointInPath(40, 0)), 10, 140)
)

compiler_web.compile(
  op.beginPath(),
  op.rect(100, 100, 100, 100),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke(),
  op.fillStyle(colors.pop()),
  op.fillText(op.add('140,100 ', op.isPointInStroke(140, 100)), 110, 160),
  op.fillText(op.add('140,140 ', op.isPointInStroke(140, 140)), 110, 140)
)

compiler_web.compile(
  op.fillStyle(colors.pop()),
  op.fillText('abcdefg', 210, 150),
  op.beginPath(),
  op.rect(200, 100, 100, 100),
  op.rect(210, 140, op.measureText('abcdefg'), 15),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke()
)

compiler_web.compile(
  op.putImageData(op.envGet('getImageData'), 300, 100)
)

compiler_web.compile(
  op.beginPath(),
  op.rect(750, 100, 100, 100),
  op.quadraticCurveTo(800, 150, 850, 150),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke()
)

compiler_web.compile(
  op.beginPath(),
  op.rect(850, 100, 100, 100),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke(),
  op.rotate(-1 * 3.14159265359/180),
  op.beginPath(),
  op.rect(850, 100, 100, 100),
  op.closePath(),
  op.strokeStyle(colors.pop()),
  op.stroke(),
  op.rotate(0)
)

compiler_web.compile(
  op.setTransform(1, 0.1, -0.1, 1, 0, 200),
  op.strokeStyle(colors.pop()),
  op.strokeRect(0, 0, 100, 100),
  op.setTransform(1, 0, 0, 1, 0, 0)
)

compiler_web.compile(
  op.translate(100, 200),
  op.strokeStyle(colors.pop()),
  op.strokeRect(0, 0, 100, 100)
)


compiler_web.compile(
  op.translate(0, 150),
  op.fillStyle('black'),
  op.textAlign('left'),

  op.scope('l', op.list(0, 5, 10, 15, 20, 25, 30, 35, 40))(
    op.fillText(op.eq(8, op.add(3, 5)), op.pop(op.get('l')), 0),
    op.fillText(op.eq(7, op.sub(56, 49)), op.pop(op.get('l')), 0),
    op.fillText(op.eq(6, op.mul(2, 3)), op.pop(op.get('l')), 0),
    op.fillText(op.eq(4, op.div(28, 7)), op.pop(op.get('l')), 0),
    op.fillText(op.eq(3, op.mod(7, 4)), op.pop(op.get('l')), 0),
    op.fillText(op.eq(3, op.mod(7, 4)), op.pop(op.get('l')), 0),
    op.fillText(op.eq('branch 1 false', op.ifElse(op.eq(8,9), 'branch 1 true', 'branch 1 false')), op.pop(op.get('l')), 0),
    op.fillText(op.eq('branch 2 true', op.ifElse(op.eq(8,8), 'branch 2 true', 'branch 2 false')), op.pop(op.get('l')), 0),
    op.fillText(op.eq('branch 3 false', op.ifElse(op.eq(8,7), 'branch 3 true', 'branch 3 false')), op.pop(op.get('l')), 0)
  )
)

compiler_web.compile(
  op.scope('l', op.list(45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145))(
    op.fillText(op.eq(1,1), op.pop(op.get('l')), 0),
    op.fillText(op.eq('x','x'), op.pop(op.get('l')), 0),
    op.fillText(op.eq(0, op.eq(2,'2')), op.pop(op.get('l')), 0),

    op.fillText(op.gt(2,1), op.pop(op.get('l')), 0),
    op.fillText(op.gt('2', 1), op.pop(op.get('l')), 0),
    op.fillText(op.eq(0, op.gt(1,1)), op.pop(op.get('l')), 0),
    op.fillText(op.eq(0, op.gt(1,2)), op.pop(op.get('l')), 0),

    op.fillText(op.ge(2, 1), op.pop(op.get('l')), 0),
    op.fillText(op.ge(1, 1), op.pop(op.get('l')), 0),
    op.fillText(op.eq(0, op.ge(1,2)), op.pop(op.get('l')), 0),

    op.fillText(op.lt(1, 2), op.pop(op.get('l')), 0),
    op.fillText(op.lt(1,'5'), op.pop(op.get('l')), 0),
    op.fillText(op.eq(0, op.lt(2,2)), op.pop(op.get('l')), 0),

    op.fillText(op.le(1, 2), op.pop(op.get('l')), 0),
    op.fillText(op.le(1,'1'), op.pop(op.get('l')), 0),
    op.fillText(op.eq(0, op.le(3,2)), op.pop(op.get('l')), 0)
  )
)

compiler_web.compile(
  op.scope('l', op.list(200, 205, 210, 215, 220, 225, 230, 235, 240))(
    op.fillText(op.eq(240, op.pop(op.get('l'))), op.pop(op.get('l')), 0),
    op.fillText(op.eq(205, op.index(op.get('l'), 1)), op.pop(op.get('l')), 0),
    op.fillText(op.eq(200, op.shift(op.get('l'))), op.pop(op.get('l')), 0),
    op.push(op.get('l'), 1000),
    op.fillText(op.eq(1000, op.pop(op.get('l'))), op.pop(op.get('l')), 0),
    op.unshift(op.get('l'), 1000),
    op.fillText(op.eq(1000, op.shift(op.get('l'))), op.pop(op.get('l')), 0)
  )
)

print('canvas plotting')
print(compiler_web.output())