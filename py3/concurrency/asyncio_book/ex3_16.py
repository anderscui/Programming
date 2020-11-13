# coding=utf-8
import asyncio
from asyncio import Future


async def main(f: Future):
    await asyncio.sleep(0.5)
    f.set_result('I have finished.')


loop = asyncio.get_event_loop()
future = asyncio.Future()
print(future.done())

task = loop.create_task(main(future))
print(task)

loop.run_until_complete(future)
print(future.done())
print(future.result())
