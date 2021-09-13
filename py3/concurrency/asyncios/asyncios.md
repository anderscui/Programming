threading - 基于线程的并行实现

参考：

* [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
* [asyncio — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
* [aio-libs - The set of asyncio-based libraries](https://github.com/aio-libs)

# AsyncIO 鸟瞰

在不同的编程语言中，多线程和多进程模型都是很常规的并发实现方式。`asyncio` 属于另一种编程范式，即**异步编程**，它不算是一个新概念，在其它语言中早就有了实现，比如 Go、C#、Scala 等。

官方文档中，`asyncio` 定义为”一个使用 async/await 语法编写并发代码的库“，但它与多线程、多进程都不同，并且也不基于其中任何一种。

`asyncio` 是单线程的设计：它使用协作式多任务处理。**协程（coroutine）**是其核心特性，可用于并发安排和执行，但它们不是内在地并发。

## asyncio 直观理解

关于 asyncio，Miguel Ginberg 在 PyCon 2017 上举了一个很好的例子：

> 象棋大师 Polgár Judit 举行了一个象棋表演赛，与多个业余选手比赛。一共有24个对手，Judit 走一步需要5秒，对手需要55秒，每局比赛平均需要30步，即一共需要60步。她可以选择以同步或异步方式下棋。同步版本中，她一次之和一个人下，结束后再和下一个对手下棋，她一共需要12个小时完赛；异步版本中，她从一桌到下一桌，此时她只需要1个小时即可完赛。

Judit 还是那个 Judit，走的步数一样，对手也是，但时间却大大减少了。

## asyncio 不简单

Python 中的 asyncio 模型建立在一堆概念之上，如 callback、event、transports、protocols 和 futures。尤其是在接触初期，需要一个适应的时间。

# asyncio 包 和 async/await 关键字

协程是 asyncio 的核心，它是生成器函数的特殊版本。它可以在 `return` 之前挂起执行，间接地将控制权传给其它协程。

## hello world
```python
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
    # time elapsed: 1.005517503 seconds
    print(f'time elapsed: {elapsed} seconds')
```

`time.sleep()` 对应任何耗时的阻塞操作，`asyncio.sleep()` 则是非阻塞操作。阻塞操作与 asyncio 不兼容，因为它会阻塞所有其它事情。

## asyncio 的规则

* 语法 `async def` 引入的 `native coroutine` 或 `asynchronous generator`。`async with` 和 `async for` 也是合法的。
* `await` 将控制权交回事件循环（挂起所在的 coroutine）。

另外也有关于可否使用 `async/await` 的规则：

* 包含 `async def` 的函数定义了一个协程。其中，可以使用 `await/return/yield`，但三者都是可选的。
    - 使用 `await` 和/或 `return` 创建了一个协程，要调用一个协程，必须使用 `await` 来得到其结果。
    - 较少见的情形是使用 `yield`，此时创建了一个异步生成器，可用于 `async for`。
    - 以 `async def` 定义的对象不可以使用 `yield from`。
* 在 `async def` 定义的协程之外使用 `await` 都是不合法的。
* 使用 `await f()` 时，`f()` 需要是一个 [`awaitable` 对象](https://docs.python.org/3/reference/datamodel.html#awaitable-objects)。

另外，通过 `@aysncio.coroutine` 标注的函数定义了 ”generator-based coroutine“，两种协程本质上等价。此 decorator 将在 3.10 中被移除。

下面看一个例子：

```python
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
```

# asyncio 设计模式

## Chaining

这一特性可以让我们将程序分解为更小的协程链。

```python
# coding=utf-8
import asyncio
import random
import time


async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result


async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    return result


async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
```

在这一部分中，执行 `part1` 结束后，`part2` 开始执行。

```python
p1 = await part1(n)
p2 = await part2(n, p1)
```

## 使用 Queue

队列的一种应用是，它作为生产者和消费者之间的传送者。

```python
# coding=utf-8
import asyncio
import itertools as it
import os
import random
import time


async def make_item(size: int = 5) -> str:
    return os.urandom(size).hex()


async def rand_sleep(caller=None) -> None:
    i = random.randint(0, 3)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
        await rand_sleep(caller=f"Producer {name}")
        i = await make_item()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")


async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await rand_sleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>"
              f" in {now-t:0.5f} seconds.")
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    import argparse

    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
```

这里比较重要的地方是 `q.task_done()` 和 `q.join()`。

# asyncio 与生成器

* 协程是”另作他用“的生成器，它使用了生成器方法的某些特性
* 旧式的生成器协程使用 `yield from` 来等待另一个生成器的结果，新协程则使用 `await` 代替之
* `await` 的使用时一个表明”断点”的信号

## `async for` 与异步生成器、异步列表推导

异步迭代器和生成器的作用，不是并发地将函数应用于序列。它们只是用于让包含它们的协程将控制权转交给其它协程。

## 事件循环和 asyncio.run()

在 Python 3.7 之后，很多情况下可以简单的使用 `asyncio.run(main())` 来管理事件循环，而之前则需要手动获得 loop，并 `run_until_complete(main())`。

关于事件循环，值得注意的点有：

* 协程如果没有关联到事件循环，它不能真正完成什么事情（这一点类似于生成器）
* 默认情况下，asyncio 运行单核、单线程上，通常这是够用的。但也可能让事件循环运行在多核上。参考 [John Reese 的演讲](https://youtu.be/0kXaLh8Fz3k?t=10m30s)
* 事件循环是 pluggable 的。如果你需要并且愿意，可以编写自己的事件循环实现。`uvloop` 是一个很好的例子，它是事件循环在 Cython 中的实现。

# 一个完整的程序：异步请求

大致流程是：

* 从本地文件中读取一个 URL 列表
* 发送 GET 请求，解码响应内容
* 搜索响应中的 urls
* 将 urls 写入文件
* 上述所有任务尽可能以异步方式完成，这将依赖于 `aiohttp` 和 `aiofiles`

```python
import asyncio
import logging
import re
import sys
from os import PathLike
from typing import IO, Union
import urllib.error
import urllib.parse

import aiofiles
import aiohttp
from aiohttp import ClientSession

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True

HREF_RE = re.compile(r'href="(.*?)"')


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    """GET request wrapper to fetch page HTML.

    kwargs are passed to `session.request()`
    """
    resp = await session.request(method='GET', url=url, timeout=5, **kwargs)
    resp.raise_for_status()
    logger.info(f'Got response [{resp.status}] for url: {url}')
    html = await resp.text()
    return html


async def parse(url: str, session: ClientSession, **kwargs) -> set:
    """Find hrefs in the HTML of `url`."""
    found = set()
    try:
        html = await fetch_html(url=url, session=session, **kwargs)
    except (
        aiohttp.ClientError,
        asyncio.exceptions.TimeoutError,
    ) as e:
        logger.error(
            f'aiohttp exception for {url} [{getattr(e, "status", None)}]: {getattr(e, "message", None)}'
        )
        return found
    except Exception as e:
        logger.exception(f'Non-aiohttp exception occurred: {getattr(e, "__dict__", {})}')
        return found
    else:
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                logger.exception(f'Error parsing url: {link}')
                pass
            else:
                found.add(abslink)
        logger.info(f'Found {len(found)} for {url}')
        return found


async def write_one(file: Union[str, PathLike], url: str, **kwargs):
    """Write the found hrefs from `url` to `file`"""
    res = await parse(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, 'a') as f:
        for p in res:
            await f.write(f'{url}\t{p}\n')
        logger.info(f'Wrote results for source url: {url}')


async def bulk_crawl_and_write(file: Union[str, PathLike], urls: set, **kwargs):
    """Crawl and write concurrently to `file` for multiple `urls`."""
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(write_one(file=file, url=url, session=session, **kwargs))
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    import pathlib
    import sys

    assert sys.version_info >= (3, 7)
    here = pathlib.Path(__file__).parent

    with open(here.joinpath('urls.txt')) as inf:
        urls = set(map(str.strip, inf))

    out_path = here.joinpath('found_urls.txt')
    with open(out_path, 'w') as outf:
        outf.write(f'source_url\tparsed_url\n')

    asyncio.run(bulk_crawl_and_write(file=out_path, urls=urls))
```

在 `parse` 的第二部分（`await` 之后），代码是同步的，因此它是阻塞式的，如果它耗时较长，可以考虑将这部分代码放在其它进程里，这需要用到 `loop.run_in_executor()`。

# 应用中的 asyncio

## 何时以及为何选择 asyncio

* 网络 IO
* Serverless design，如 p2p，多用户网路的聊天室
* 希望模拟 fire-and-forget 的读写操作

不选择的主要原因是，`await` 只支持一部分库中的一部分方法，比如不是所有 DBMS 都有其对应的 asyncio 版本的客户端。

# Odds and Ends

## 其它顶层 asyncio 函数

* run()
* gather()
* create_task() / ensure_future()

```python
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
```

`ensure_future()` 已经被 `create_task()` 代替。

# 版本变化

* 3.3：`yield from`
* 3.4：`asyncio` 引入 Python 标准库
* 3.5：`async`、`await` 引入
* 3.7： `async`、`await` 成为保留字

