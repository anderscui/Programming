# coding=utf-8
import asyncio
import time


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


def blocking():
    # 此调用是会 block 主线程，阻止 loop 继续运行下去，因此不能让此函数作为 coroutine。
    # 解决方法是让它执行于一个 executor.
    time.sleep(0.5)
    print(f'{time.ctime()} Hello from a thread!')


loop = asyncio.get_event_loop()
task = loop.create_task(main())

# 此函数仅仅发起一个 schedule，并不真正执行，直到 run_until_complete；返回类型为 Future
loop.run_in_executor(None, blocking)
loop.run_until_complete(task)

# pending 不包含 blocking future，只关心 task。
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
