# coding=utf-8
import asyncio

async def f():
    pass

coro = f()

loop = asyncio.get_event_loop()
task = loop.create_task(coro)
assert isinstance(task, asyncio.Task)

new_task = asyncio.ensure_future(coro)
assert isinstance(new_task, asyncio.Task)

mystery_one = asyncio.ensure_future(task)
assert mystery_one is task
