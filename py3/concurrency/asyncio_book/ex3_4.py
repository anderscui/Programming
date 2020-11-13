# coding=utf-8
import asyncio
import time


def f1():
    return 1


async def f2():
    return 1


# 与普通函数一样，type 都是 function
print(type(f1), type(f2))

import inspect

# True
print(inspect.iscoroutinefunction(f2))

coro = f2()
# coroutine
print(type(coro))
# True
print(inspect.iscoroutine(coro))

try:
    coro.send(None)
except StopIteration as e:
    print('The answer is: ', e.value)
