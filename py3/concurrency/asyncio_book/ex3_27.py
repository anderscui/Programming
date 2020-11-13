# coding=utf-8
import asyncio


async def doubler(n):
    for i in range(n):
        yield i, i * 2
        # pretend to be a async function
        await asyncio.sleep(0.1)


async def main():
    result = [x async for x in doubler(3)]
    print(result)
    result = {x: y async for x, y in doubler(3)}
    print(result)
    result = {x async for x in doubler(3)}
    print(result)


asyncio.run(main())
