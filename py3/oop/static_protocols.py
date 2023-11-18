# coding=utf-8
from typing import TypeVar, Protocol, SupportsComplex

T = TypeVar('T')


class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...


RT = TypeVar('RT', bound=Repeatable)


def double(x: RT) -> RT:
    return x * 2


if __name__ == '__main__':
    import numpy as np

    # complex
    v = 3+4j
    print(v.real, v.imag)
    print(isinstance(v, complex), isinstance(v, SupportsComplex))

    c64 = np.complex64(3+4j)
    print(isinstance(c64, complex), isinstance(c64, SupportsComplex))
