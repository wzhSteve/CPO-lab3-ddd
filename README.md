# ddd - Lab3 - Variant 2

- Name:
  - ddd

- Member
  - Wang Qihang:
    - id: 212320003
    - email: Wqhlw@hdu.edu.cn
  - Wang Zehao:
    - id: 212320005
    - email: 15029930122@163.com

In lab 2, *Immutable Algorithms and Data Structure Implementation*, our
variant 2 aims to implement dynamic array using Python.

## Project structure

- `MathExpression.py` -- includes class `expression` with methods `str_tolist`, `value_replace` and `process`,
 class `Stack` with `isEmpty`, `push`, `pop`, `peek` and `size`, and functions `types`, `direct_cal` and `simple_cal`.

- `MathExpression_test.py` -- unit and PBT tests for classes and functions in `MathExpression.py`.

## Features

- `types(argType)`: use as a decorator to check the types of the input parameters of each function.
- `expression(object)`: This `Class` process the input string and function like `lambda a, b: a + b`. The function `str_tolist` in this `Class` transforms the input function string into a list based on the property of each element in the string. The function `value_repalce` in this `Class` replaces the variants in the string with their values.
- `direct_cal(infix)`: This function converts string expressions into postfix expressions.
- `simple_cal(a, b, x)`: This function calculates the result of the input values `a` and `b` based on the operator `x`.

## contribution

- Wang Qihang Completed the MathExpression.py

- Wang Zehao Completed the MathExpression_test.py

## Changelog

- 19.06.2022 - 3
  - Wang Zehao revise MathExpression.py & MathExpression_test.py
- 13.06.2022 - 2
  - Wang Qihang upload MathExpression.py
- 13.06.2022 - 1
  - Wang Zehao upload MathExpression_test.py
- 13.06.2022 - 0
  - Initial.

## Design notes

- Advantages of unittest:
  - Support automated testing
  - Secondary development is convenient
  - Organize test cases together by class

- Disadvantages of unittest:
  - Must be written in TestCase subclass
  - Must write test method
  - Difficult to expand
