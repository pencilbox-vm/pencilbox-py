# pencilbox-py
pencilbox compiler in Python

## How to use
```python
from dsl import op
from compiler import Compiler

ast = op.scope(
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
compiler.compile(ast)
compiler.output() # We get list of bytecodes here
```