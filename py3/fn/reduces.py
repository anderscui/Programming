# coding=utf-8

import functools


if __name__ == '__main__':
    items = ()
    print(sum(items))
    print(functools.reduce(lambda a, b: a+b, items, 1))

    items = (1,)
    print(functools.reduce(lambda a, b: a+b, items))
