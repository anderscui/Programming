# coding=utf-8
import asyncio
from asyncio import Future

f = Future()
# false
print(f.done())

f.set_result(1)
# true
print(f.done())

f.cancel()
print(f.cancelled())
