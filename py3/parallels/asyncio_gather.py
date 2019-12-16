# coding=utf-8
import asyncio
import time


async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print(f'Task {name}: compute factorial({i})...')
        await asyncio.sleep(1)
        f *= i
    print(f'Task {name}: factorial({number}) = {f}')


async def main():
    # schedule multiple calls *concurrently*
    await asyncio.gather(factorial('A', 2), factorial('B', 3), factorial('C', 4))


asyncio.run(main())
