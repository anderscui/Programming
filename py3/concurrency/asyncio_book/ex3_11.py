# coding=utf-8
import asyncio


async def f():
    await asyncio.sleep(1.0)
    return 1


loop = asyncio.get_event_loop()
coro = f()
print(loop.run_until_complete(coro))
