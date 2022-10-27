# coding=utf-8
from functools import partial
from operator import __mul__


def multiply():
    return [lambda x: i * x for i in range(4)]


def multiply2():
    return (lambda x: i * x for i in range(4))


def multiply3():
    return [partial(__mul__, i) for i in range(4)]


if __name__ == '__main__':
    print([m(100) for m in multiply()])
    print([m(100) for m in multiply2()])
    print([m(100) for m in multiply3()])
