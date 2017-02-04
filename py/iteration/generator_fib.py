# coding=utf-8
from __future__ import unicode_literals


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


# get a generator
f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
