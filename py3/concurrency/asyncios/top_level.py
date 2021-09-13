import asyncio
import time


async def coro(seq) -> list:
    await asyncio.sleep(max(seq) * 0.1)
    return list(reversed(seq))


async def main():
    t = asyncio.create_task(coro([3, 2, 1]))
    t2 = asyncio.create_task(coro([10, 5, 0]))

    start = time.time()
    a = await asyncio.gather(t, t2)
    print(f'elapsed: {time.time() - start}')
    print(f'all tasks done: {all((t.done(), t2.done()))}')
    return a


if __name__ == '__main__':
    result = asyncio.run(main())
    print(result)
