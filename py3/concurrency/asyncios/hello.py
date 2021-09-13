# coding=utf-8
import asyncio


async def hello():
    print('hello')
    await asyncio.sleep(1)
    print('world')


async def main():
    await asyncio.gather(hello(), hello(), hello())


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f'time elapsed: {elapsed} seconds')
