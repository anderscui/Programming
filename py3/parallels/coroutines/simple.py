# coding=utf-8

from inspect import getgeneratorstate


def simple_coro(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)


coro = simple_coro(14)
print(getgeneratorstate(coro))
print(next(coro))
print(getgeneratorstate(coro))
print(coro.send(28))
print(coro.send(99))
