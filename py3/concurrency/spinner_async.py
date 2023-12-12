# coding=utf-8
import asyncio
import itertools

spin_chars = r'\|/-'
# spin_chars = r'1234567890'


async def spin(msg: str):
    status = ''
    for c in itertools.cycle(spin_chars):
        status = f'\r{c} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def slow():
    await asyncio.sleep(3)
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    return result


def main():
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
