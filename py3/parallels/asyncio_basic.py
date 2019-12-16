# coding=utf-8
import asyncio
import time

##### method 1: asyncio.run

# async def main():
#     print('hello')
#     await asyncio.sleep(1)
#     print('world')
#
#
# # run method 1: asyncio.run
# asyncio.run(main())


##### method 2: await a coroutine


# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     print(f'started at {time.strftime("%X")}')
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f'finished at {time.strftime("%X")}')
#
#
# asyncio.run(main())


##### method 3: create_task


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(type(task1))

    print(f'started at {time.strftime("%X")}')

    await task1
    await task2

    print(f'finished at {time.strftime("%X")}')


asyncio.run(main())
