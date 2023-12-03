# coding=utf-8
import functools
import operator
from collections.abc import Iterable
from typing import overload, Union, TypeVar

T = TypeVar('T')
S = TypeVar('S')


@overload
def mysum(it: Iterable[T]) -> T | int: ...
@overload
def mysum(it: Iterable[T], /, start: S) -> T | S: ...
def mysum(it, /, start=0):
    return functools.reduce(operator.add, it, start)


if __name__ == '__main__':
    print(mysum([1, 2, 3], 1))
