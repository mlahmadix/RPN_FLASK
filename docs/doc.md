# RPN calculator (Reverse Polish Notation)

Reverse Polish notation (RPN) is a mathematical notation in which every operator follows all of its operands, in contrast to Polish notation, which puts the operator in the prefix position. It is also known as postfix notation and is parenthesis-free as long as operator arities are fixed.

## Available operators

operator | operation                    | example
:-------:|------------------------------|------------
`+`      | addition                     | `1 2 +` = 3
`-`      | subtraction                  | `1 2 -` = -1
`*`      | multiplication               | `2 3 *` = 6
`/`      | division                     | `7 2 /` = 3.5

## available routes:s

### /rpn/stack/<stack_id>
* get(stack_id): Get a stack
* delete(stack_id): Delete a stack
* push(stack_id): Push to a stack

### /rpn/stack
* get(): List the available stacks
* post(): Create a new stack

### /rpn/op
* get(): List all operators

## Tests
```
python -m pytest
```