# coding=utf-8
from fractions import Fraction

from oop.ndvectors import Vector

if __name__ == '__main__':
    # more test cases, see oop.vectors.py
    v1 = Vector((3, 4))
    print(abs(v1))
    # TypeError: bad operand type for unary -: 'Vector'
    print(-v1)
    # TypeError: bad operand type for unary +: 'Vector'
    print(+v1)

    v2 = Vector((1, 2))
    print(v1+v2)
    print((1, 2, 3) + v2)
    # TypeError: unsupported operand type(s) for +: 'Vector' and 'str'
    # print(v2 + 'abc')

    print(v2 * 11, 11 * v2)
    print(v2 * 1.1, v2 * True, v2 * Fraction(1, 3))

    # @ operator: since py 3.5
    v1 = Vector([1, 2, 3])
    v2 = Vector([5, 6, 7])
    # TypeError: unsupported operand type(s) for @: 'Vector' and 'Vector'
    print(v1 @ v2)

    print(v1 == (1, 2, 3))

    print(id(v2), v2)
    # create a new object
    v2 += v1
    print(id(v2), v2)
