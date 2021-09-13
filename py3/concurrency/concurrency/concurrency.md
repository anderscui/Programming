# 通过并发来为 Python 程序提速

参考：

* [An Intro to Threading in Python](https://realpython.com/python-concurrency/)
* * [multiprocessing — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html)

也许你已经听说过 **asyncio**，但尚未了解它和其它并发方法有何不同，甚至还不清楚如何使用并发，本文将介绍这些内容。

本文要介绍的并发方法包括 `threading`、`asyncio`、`multiprocessing`。

# 什么是并发（Concurrency）

并发的意思是**同步发生**，它有不同的实现方法，比如线程（多线程）、任务（asyncio）、进程（多进程）。在高层角度来看，它们是类似的，都指向按序执行的指令序列。在实现细节上，这些方法会有差异，适用于不同的场景。

考虑**同步**这个说法，只有多进程是真正可以同时执行的。多线程和 asyncio 都运行在单个 CPU 上，一个时刻只能执行一个任务。

不过，多线程和 asyncio 的机制也有很大差异。对于多线程而言，OS 面对的是多个真实的线程，可以在需要时中断某个线程以执行另一个线程。这种方式是所谓的**抢占式多任务处理（pre-emptive multitasking）**，OS 可以控制如何切换线程。抢占式多任务处理的一个好处是，线程内的代码不需要考虑如何切换，但这一点也带来了其它问题，即使是简单的 `x = x + 1` 语句。

`asyncio` 属于**协作式多任务处理（cooperative multitasking）**。各个任务可以主动声明，自己已准备就绪，可以切换出去。代码中的任务需自行处理这一部分，但好处时可以确定任务是何时切换的，因而有时可以简化设计。

# 什么是并行（Parallelism）

如果电脑是多核的，如何能更有效地利用之？

使用 `multiprocessing`，Python 可以创建新进程，**每个进程会拥有自己的解释器**，不同线程可以运行在不同的核上，因而能够真正意义上**同步运行**。

# 并发何时是有用的？

并发对于两类问题区别很大，即 CPU 密集型和 I/O 密集型。

I/O 问题会让程序慢许多，因为它必须要频繁地等待外部资源的获取，这一般发生在程序与远慢于 CPU 的组件交互之时。常见的例子访问文件系统和网络连接时。当程序需要大量的 I/O 操作时，程序会耗费大量时间在等待外部结果，可以说是空等。

如果是 CPU 密集型问题，那么它主要等待的时间在计算上，此时应想办法尽量高效地利用 CPU。

前面提及的三种方法，适用于这两类问题某一种，同时它们也都会让程序复杂一些，因此需要综合考虑，确定选择哪一种。

优化 I/O 问题意味着减少空等的时间，优化 CPU 密集型问题意味着尽可能让 CPU 有更多 load 的时间。

# 如何提升 I/O 问题的性能

## 同步版本

```python
import requests
import time

def download_site(url, session):
    with session.get(url) as resp:
        print(f'read {len(resp.content)} from {url}')

def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)

if __name__ == '__main__':
    sites = ['https://realpython.com/',
             'https://www.cnblogs.com/'] * 10

    start = time.time()
    download_all_sites(sites)
    elapsed = time.time() - start
    # downloaded 20 in 5.453153133392334 seconds.
    print(f'downloaded {len(sites)} in {elapsed} seconds.')
```

代码使用了 `Session`，在这个测试中，它比直接使用 `requests.get` 快一倍。

### 同步版本的特点

* 优点：代码简单，不论是编写还是调试。
* 缺点：比较慢，相比其它方式

## 多线程版本

```python
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as resp:
        print(f'read {len(resp.content)} from {url}')

def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

if __name__ == '__main__':
    sites = ['https://realpython.com/',
             'https://www.cnblogs.com/'] * 10

    start = time.time()
    download_all_sites(sites)
    elapsed = time.time() - start
    # downloaded 20 in 1.5748848915100098 seconds.
    print(f'downloaded {len(sites)} in {elapsed} seconds.')
```

一个改动是，在获取 session 时，需要为每个线程创建一个 session，`requests.Session` 不是线程安全的。

另外，线程池的 `max_workers` 需要通过实验调整之，没有固定的“最优值”。

### 多线程版本的特点

* 优点：更快，性能是同步版本三倍以上
* 缺点：代码更复杂一些，不论是编写还是调试都会更麻烦

## asyncio 版本

### asyncio 基础

`asyncio` 的概念是：一个称为事件循环（event loop）的对象，控制每个任务如何及合适运行。事件循环会了解每个任务的状态。

PS：如果没记错的话，很久以前，Windows 编程中，也有一个核心概念叫事件循环。

任务的状态有多种，这里假设只有 `ready` 和 `waiting` 两种。ready 状态表明，一个任务有事情要完成，并且准备就绪。`waiting` 状态表明，任务在等待外部组件的完成，如网络操作。

事件循环维护两个任务列表，分别用于上述两种状态。loop 不断检查 ready 的任务，持续运行，直至所有任务都已完成。

`asyncio` 的一个重要特点是，只有任务主动放弃控制后，控制权才会交换事件循环。因此，在  `asyncio` 中，资源的共享会比多线程更容易一些，不需要担心线程安全问题。

### async 与 await

使用 `await` 时，任务将控制权交还事件循环。当代码 await 一个函数调用，这意味着该调用可能耗时较久，因此任务需要交还控制权。

```python
import aiohttp
import asyncio
import time

async def download_site(session, url):
    async with session.get(url) as resp:
        print(f'read {len(resp.content_length)} from {url}')

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    sites = ['https://realpython.com/',
             'https://www.cnblogs.com/'] * 10

    start = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    elapsed = time.time() - start
    # downloaded 20 in 0.9054982662200928 seconds.
    print(f'downloaded {len(sites)} in {elapsed} seconds.')
```

这段代码看起来更为复杂，但实际上其结构是更简单的。性能由于多线程版本。

在 `download_all_sites` 中可以看到，`session` 可以在任务之间共享，因为这些任务运行在同一线程上。

使用任务有一个巨大的优点，即它的扩展性远好于多线程，因为“任务”所消耗的资源远小于线程。

### asyncio 版本的特点

* 优点：更快，也能帮助产生更好的设计
* 缺点：需要特定的库的 `async` 版本才能充分利用 `asyncio`。如果有一个任务“协作失灵”，那么整个协作式多任务处理也就失效了。

## multiprocessing 版本

```python
import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as resp:
        proc_name = multiprocessing.current_process().name
        print(f'{proc_name} - {id(session)} read {len(resp.content)} from {url}')


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == '__main__':
    sites = ['https://realpython.com/',
             'https://www.cnblogs.com/'] * 10

    start = time.time()
    download_all_sites(sites)
    elapsed = time.time() - start
    # downloaded 20 in 2.4319159984588623 seconds.
    print(f'downloaded {len(sites)} in {elapsed} seconds.')
```

`multiprocessing` 包支持生成多个进程，其 API 类似于 `threading` 包的。它可以跳过 GIL 的限制，因为它使用的是子进程而非线程。因此，它可以让程序员更有效地利用机器上的多核资源。

`Pool` 会创建一批进程，每个进程拥有自己的解释器，主进程和子进程的交互有 `multiprocessing` 来完成。创建 pool 时，如果不指定进程数，`Pool` 会决定当前机器的核数，以此为准，在当前问题中，这一做法是最优选择。增加进程数，不会使程序执行得更快，它实际上会更慢，因为创建和销毁进程也会增加相当多的额外成本。

`initializer` 参数在进程创建时执行，这里它的作用是创建一个新的 `Session` 对象。需要注意的是，虽然标记了 `global`，但每个进程享有自己的解释器，所以其结果是，每个进程有自己的 `Session` 对象，在这个进程内，session 是唯一的、global 的。

### multiprocessing 的特点

* 优点：可充分利用机器资源；编码相对简单
* 缺点：额外的初始化代码，全局的 `session` 对象有点奇怪。

# 如何提供 CPU 问题的性能

## 同步版本

```python
import time


def cpu_bound(n):
    return sum(i * i for i in range(n))


def find_sums(nums):
    for n in nums:
        cpu_bound(n)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    start = time.time()
    find_sums(numbers)
    elapsed = time.time() - start
    # time elapsed: 7.635008096694946 seconds
    print(f'time elapsed: {elapsed} seconds')
```

这是一个基准时间。

## threading 版本

改为多线程执行，时间会更慢一点，意料之中。

## multiprocessing 版本

```python
import multiprocessing
import time


def cpu_bound(n):
    return sum(i * i for i in range(n))


def find_sums(nums):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, nums)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    start = time.time()
    find_sums(numbers)
    elapsed = time.time() - start
    # time elapsed: 1.6001529693603516 seconds
    print(f'time elapsed: {elapsed} seconds')
```

速度大约是同步版本的5倍（电脑是6核的），实现也很简单。

# 何时使用并发？

上面提到两类问题和三种不同实现。实际开发中，大致可按一下思路确定何时使用：

1. 确定是否通过并发优化性能：考虑问题的类型，并考虑以上三种实现是否有帮助
2. 对于 CPU 密集型问题，使用多进程
3. 对于 I/O 密集型问题，使用 `asyncio` 或 `threading`。前者需要额外的库的支持，后者开销更大，需要按情况处理

一句格言是：`Use asyncio when you can, threading when you must.`
