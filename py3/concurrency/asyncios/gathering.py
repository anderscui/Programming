# coding=utf-8
import asyncio


async def factorial(name, n):
    f = 1
    for i in range(2, n+1):
        print(f'Task {name}: compute factorial({i})...')
        await asyncio.sleep(1)
        f *= i
    print(f'Task {name}: compute factorial({n}) = {f}')


async def main():
    # schedule 3 tasks
    await asyncio.gather(
        factorial('A', 2),
        factorial('B', 3),
        factorial('C', 4),
    )


asyncio.run(main())
