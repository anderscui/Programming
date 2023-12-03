# coding=utf-8
import itertools
from collections.abc import Iterator


def fib() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


if __name__ == '__main__':
    print(list(itertools.takewhile(lambda i: i < 100, fib())))
