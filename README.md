# pencilbox-py
**PencilBox** compiler in Python

## Environment
Python3

## How to use

### Example: basic plotting
```python
from dsl import op
from compiler import Compiler

compiler = Compiler()
compiler.compile(
  op.beginPath(),
  op.rect(0, 0, 50, 50),
  op.arc(25, 25, 25, 0, 1.5 * 3.14159265359),
  op.closePath(),
  op.strokeStyle('red'),
  op.stroke()
)
bytecodes = compiler.output() # We get list of bytecodes here
```

### Example: fibonacci
```python
from dsl import op
from compiler import Compiler

code = op.scope(
      'fib',
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

compiler = Compiler()
compiler.compile(code)
bytecodes = compiler.output() # We get list of bytecodes here
```

### Using bytecodes
Once the bytecodes is generated, it should be passed to **PencilBox** runtime in browser to run the program.
Please checkout the [**PencilBox** runtime `How to use`](https://github.com/pencilbox-vm/runtime#how-to-use) 
