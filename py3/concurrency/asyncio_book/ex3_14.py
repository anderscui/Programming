# coding=utf-8
import asyncio


async def g():
    # await asyncio.sleep(0.5)
    print('ok')


async def f():
    for i in range(5):
        asyncio.create_task(g())
    await asyncio.sleep(0.5)


asyncio.run(f())
