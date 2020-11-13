# coding=utf-8
import asyncio
import time


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


# 获取一个 loop，在 async def 函数内，使用 `get_running_loop`
loop = asyncio.get_event_loop()
# schedule the coroutine to be run on the loop
task = loop.create_task(main())
# block 当前线程，通常是主线程
loop.run_until_complete(task)
print('main comes back')
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
# 当程序的主部分 unblock，可能还有其它任务在 loop 上执行，此时通常要 gather、cancel，再次调用 run_until_complete
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
