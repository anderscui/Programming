# coding=utf-8
import asyncio
import random

# ANSI colors
c = (
    '\033[0m',  # end of color
    '\033[36m',  # cyan
    '\033[91m',  # red
    '\033[35m',  # magenta
)


async def make_random(idx: int, threshold: int = 6) -> int:
    print(c[idx+1] + f'initialized make_random({idx})')
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx+1] + f'make_random({idx}) == {i} too low; retrying...')
        await asyncio.sleep(idx+1)
        i = random.randint(0, 10)
    print(c[idx+1] + f'finished: make_random({idx}) == {i}')
    return i


async def main():
    res = await asyncio.gather(*(make_random(i, 10 - i - 2) for i in range(3)))
    return res


if __name__ == '__main__':
    # random.seed(111)

    r1, r2, r3 = asyncio.run(main())
    print()
    print(f'r1: {r1}, r2: {r2}, r3: {r3}')
