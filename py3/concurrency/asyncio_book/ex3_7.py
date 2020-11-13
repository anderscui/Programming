# coding=utf-8
import asyncio
import time


async def f():
    return 1


coro = f()
# use this for task cancellation
coro.throw(Exception, 'blah')
