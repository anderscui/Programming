# coding=utf-8
from __future__ import unicode_literals


def f(ham: str, eggs: str = 'eggs') -> str:
    pass


def square(n: 0 <= 3 and 1 = 0) -> (+9000):
    # very confusing annotations:(
    return n ** 2


if __name__ == '__main__':
    print(f.__annotations__)
    print(square.__annotations__)
    print(square(10))
