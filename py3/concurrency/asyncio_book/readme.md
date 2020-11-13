# Using Asyncio in Python

# Preface

Py3.4 引入了 `asyncio` 库，py3.5 引入了 `async` 和 `await` 关键字，它们统称为"异步编程"，或 `asyncio`。
 
社区的反应很谨慎，有的人认为它过于复杂，难以理解，而且这一观点还不限于初学者。

有过几年py经验的开发者，多数用过线程，即使没有，也了解 `blocking`，比如使用 `requests` 时。如果想要**同时请求**数以万计的 URL，使用 requests 就相当困难了。

本书的目标是让读者对这些新特性有一个基本的理解，并了解如何使用之，具体来说是：

* asyncio 与 treading 的仔细对比
* 理解 `async/await` 关键字
* 对于 asyncio 的概览
* 通过详细的代码案例，演示如何使用若干流行的与 asyncio 兼容的三方库  

asyncio 不会给你的代码带来剧烈的变化，它更多的是提供特别的工具，并仅适用于特别的情形，但在合适的情形下，它却异常有用。

# Ch 01 - Introducing Asyncio

`asyncio` 不止是能够执行并行操作，它的内涵要丰富得多，它需要我们改变构造程序的方式。它的核心点是：当你等待 `this task` 执行时，可以去做 `other tasks`。

相比于多线程方式，`asyncio` 真正的优势是消除了**竞态条件（Race Condition）**。

## asyncio 要解决的是什么问题？

对于 I/O-bound 任务，采用异步方式而非多线程方式有且仅有两个原因：

* asyncio 提供了更安全的选项——相比于抢占式多任务方式（多线程），因而避免了很多 bug、竞态条件等非确定性的危险。
* asyncio 提供了更简单的方式来处理数以千计的同时（simuataneous）操作

多线程——作为一种编程模型——最适合的场景是，任务可执行于多个CPU上，线程之间需要高效通讯。网络编程不属于上述场景，它包含大量的**等待完成**，此时不需要 OS 将任务分发给多个 CPU。

同时，关于 event-based 编程模型也有很多误解，比如：

* asyncio 会让代码运行得特别快：事实上不是，尽管它可以更容易创建大量的 socket 连接。
* asyncio 会替代掉多线程编程：绝对不是。对于 CPU-bound 任务，多线程是更好的选择。
* asyncio 消除了 GIL 的影响：依然不是。asyncio 不受 GIL 影响，只是因为它不使用多线程。
* asyncio 避免了所有的竞态问题：错。它只能消除一部分，任何并发编程都会存在竞态问题。
* asyncio 使得并发编程更容易：？

并行编程总是复杂的，不过在单个线程中开发，其中的”验证“会稍微容易些。

# Ch 02 - The Truth about Threads

线程是 OS 提供的一个特性，可使得程序的某些部分并行执行。OS 负责管理它们，包括如何在线程之间共享数据。

本书本不应该涉及任何线程相关内容，但既然 asyncio 是线程的一种替代项，如果不讲线程，则很难理解 asyncio 的价值。另一方面，即使使用 asyncio，线程和进程也是必须要用到的技术。

## 线程的优点

* 易于阅读：在函数体内部，我们可以装作它不是并发的
* 可以共享内存的并行
* 大量已有代码、知识、最佳实践

不过，由于 GIL 的存在，Python 的多线程代码实际上不能真正地并行执行。但代码的简单性是实实在在的，尤其是在我们学习了如何保持代码简单、安全之后。

一般来说，最佳实践是使用 `ThreadPoolExecutor`，在必要时关闭它（.shutdown）。另外，尽量避免访问全局变量。

## 线程的缺点

多线程编程本质是复杂，不论编程语言如何改进，模式如何演化。

* 多线程是复杂的：bugs、竞态条件等等
* 多线程是资源密集的：需要OS耗费额外的资源，在32位系统中，每个进程的地址空间上限是3G，这极大地限制了线程的创建，在64位系统中则缓和了许多。
* 多线程影响吞吐量：当并发程度很高时（>5000），由于上下文切换的成本，吞吐量受到很大限制
* 多线程是不灵活的：OS对所有线程一视同仁，即使一个线程处于等待状态，系统还是会给它分配大量的执行时间。

上述问题不是某些平台特有的，Windows、Linux等都是如此。

通过例子2.2可以看到，如果涉及到非原子性操作，”共享资源“将成为一个潜在的问题。此时需要使用 lock，但也就需要所有共享资源的地方添加 lock；而且单纯通过”阅读“代码是不能够找出所有这些地方的；还有一种情况是，如果代码依赖于三方库。

因此，干脆使用单个线程吧，让它负责所有工作——问题迎刃而解；而且，我们能够看到所有的上下文切换，欢迎来到 `asyncio` 的世界。

# Ch 03 - Asyncio Walk-Through

asyncio 是复杂的，一个主要原因是，它实际上是面向不同开发者、解决不同问题的。不幸的是，很少有教程说清哪些部分是我们需要的。它面向的是两类：

* end-users：一般应用开发
* framework：框架应用开发

由于未作上述区分，社区里产生了大量的混乱与疑惑。比如，asyncio 的官方文档实际上更适合 framework 开发者，因为很多开发者对它望而却步。

## Quickstart

asyncio 的开发者之一 **Yury Selevanov**说过，作为日常开发之用，只需要了解大约7个函数。它们可总结为：

* 开始 asyncio event loop
* 调用 async/await 函数
* 创建 task，在 loop 上执行之
* 等待多个任务完成
* 在所有并行任务结束之后，关闭 loop

### Hello World of Asyncio

```python
import asyncio, time


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


asyncio.run(main())
```

实际开发中，多数应用会用到这里的 `run`，有必要深入理解它。

例子3.2，尽管不是严格等同于 `run`，但它很接近，可以帮助我们理解 `run` 做的事情。run 每次都会创建一个 loop，它应当作为程序的 entry point。

```python
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
```

可以看到 `run` 函数确实帮助我们做了很多事情。后面会逐渐看到，虽然使用 asyncio 需要注意它的底层机制（而不像 Node.js 那样隐藏了许多），但其中的模式类似于上例。

目前的例子还少了一环，即阻塞式函数调用。asyncio 提供了类似于 `concurrent.futures` 包的API，看下面的例子：

```python
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
```

以上就是 asyncio 中开发者所需要了解的部分了。

## The Tower of Asyncio

作为终端开发者只需要了解少数几个函数，但作为框架开发者则不然，他们需要了解各种钩子（hook point）。本节将从框架开发者角度去理解 asyncio，并且将该模块组织为一个层级结构。

* **T9: Network：streams**: StreamReader ...
* T8: Network：TCP & UDP：Protocol
* T7: Network: transports: BaseTransport
* **T6: Tools**: asyncio.Queue
* **T5: Subprocesses & Threads**: run_in_executor, asyncio.subprocess
* T4: Tasks: Task, create_task()
* T3: Futures: Future
* **T2: Event Loop**: run(), BaseEventLoop
* **T1(Base): Coroutines**: async def, async with, async for, await

加粗者为终端用户需重点关注的。

T1 是最底层的 API，流行的库包括 Curio 和 Trio。

T2 提供了 loop，Trio 则提供了自己的实现，而 uvloop 则仅仅替换了 loop 的实现，这恰是 asyncio 设计之初衷。

Future 和 Task 相关，后者是前者的子类。

asyncio.Queue 类似于 queue.Queue，但它的 get 和 put 需要 await。queue.Queue 不能直接在协程中使用。

T7-9中，终端用户可能常用到的是 T9。

了解这些组件后，重新考虑在网络编程中需要着重学习那些部分：

* T1: 理解如何编写 async def 函数，如何使用 await 调用；
* T2: 理解如何启动、关闭 loop，如何与之交互
* T5: 执行阻塞式代码时 executors 是必要的，而且现实是大部分第三方库还不是 asyncio 兼容的，比如 sqlalchemy
* T6: 在需要将数据”喂入“长时间运行的协程时，最好的方法是使用 asyncio.Queue，恰如 queue.Queue 在多线程开发中的角色
* T9: 处理 socket 编程的最简单方法是 streams API。

## Coroutines

本节解释诸如 coroutine、异步函数的概念。

coro 在 py 3.4 引入，而 async def 在 py 3.5 才有，那么在它之前用什么？答案是 generators，在老的代码中会看到 `@asyncio.coroutine` 这样的 decorator。现在通过 async def 定义的协程被称为 native coroutines。

### The new async def keywords

```python
import inspect

def f1():
    return 1


async def f2():
    return 1


# 与普通函数一样，type 都是 function
print(type(f1), type(f2))

# True
print(inspect.iscoroutinefunction(f2))

coro = f2()
# coroutine
print(type(coro))
# True
print(inspect.iscoroutine(coro))

try:
    coro.send(None)
except StopIteration as e:
    print('The answer is: ', e.value)
```

`f2` 是函数，它求值之后的结果是协程。协程是这样一种对象，它封装了一种能力，可以“恢复”因尚未完成而挂起的函数。这听起来像是 generator。

协程通过 `send` 一个 None 来初始化，在使用 loop，它会为我们做这件事。当协程返回时，抛出一个 `StopInteration`。`send` 和 `StopInteration`，两者定义了协程的始终。看起来这样做，平白让事情变得复杂了，但一般开发中，是 loop 去做这些事情的。

### The new await keywords

`await` 关键字接受一个参数，其类型必须是 awaitable 的：

* 协程（async def 函数的结果）
* 实现了 `__await__` 函数的对象

本书重点看第一种对象。

在例子中的各种 `send` 之后，来看看如果借助于 loop，是如何简洁的：

```python
import asyncio


async def f():
    await asyncio.sleep(1.0)
    return 1


loop = asyncio.get_event_loop()
coro = f()
print(loop.run_until_complete(coro))
```

## Event Loop

获取 loop 的两种方式：

* get_running_loop: 在协程函数中可调用
* get_event_loop: 在任何地方可调用

get_running_loop 在 3.8 中添加，因此还能在遗留代码中看到 get_event_loop 的使用。在协程函数中，两者都可以用。

get_event_loop 仅可在**同一线程**上调用，除非通过 new_event_loop 和 set_event_loop 来设置，一般开发中不需要这些。

推荐的方法是 get_running_loop，它总是如你期望的运行：由于它只能在协程、task、被上述两者调用的函数里，因此它总是返回当前的 running loop。

```py
async def g():
    # await asyncio.sleep(0.5)
    print('ok')


async def f():
    for i in range(5):
        asyncio.create_task(g())
    await asyncio.sleep(0.5)


asyncio.run(f())
```

通过 create_task 来分发若干 tasks。

## Tasks and  Futures

用得较多的是 Task，通常用 create_task 来创建。Future 是 Task 的父类，提供了与 loop 交互的各种功能。

Future 表示一个 activity 的未来完成状态，由 loop 来管理。Task 几乎是一样的，除了它的 activity 是协程。

```py
from asyncio import Future

f = Future()
# false
print(f.done())

f.set_result(1)
# true
print(f.done())
```

Future 实例可以做如下操作：

* set_result + result()
* cancel + cancelled()
* add callbacks

Future 是不能完全避免的，比如在 executor 上调用函数时，返回的是 Future，而非 Task。

```py
import asyncio
from asyncio import Future


async def main(f: Future):
    await asyncio.sleep(0.5)
    f.set_result('I have finished.')


loop = asyncio.get_event_loop()
future = asyncio.Future()
print(future.done())

task = loop.create_task(main(future))
print(task)

loop.run_until_complete(future)
print(future.done())
print(future.result())
```

这里有一个 task，一个 future，create_task 时，它会 schedule 一个 task，但不会立即执行，到了 run_until_complete后，loop 开始运行，task 也开始执行，这样 future 也得到了 result。

在 py3.8 后，set_result 不能 task 上执行。

### create_task or ensure_future

之前看到了 `asyncio.create_task`，在此函数引入之前，需要现获取 loop，然后调用 `loop.create_task`，此外还可以使用 `asyncio.ensure_future`，这两个函数都有推荐使用者。

ensure_future 需要为 asyncio 的广泛误解负很大责任，大部分 API 的文档很清晰，而 ensure_future 是少数不清晰的之一。它的作用是：

* 如果传入一个 coro 对象，将其封装为 Task 实例（因此可运行在 loop 上），等价于调用 create_task。
* 如果传入一个 Future 对象（或 Task，Task 是 Future 的子类），则直接返回

```py
async def f():
    pass

coro = f()

loop = asyncio.get_event_loop()
task = loop.create_task(coro)
assert isinstance(task, asyncio.Task)

new_task = asyncio.ensure_future(coro)
assert isinstance(new_task, asyncio.Task)

mystery_one = asyncio.ensure_future(task)
assert mystery_one is task
```

总之，ensure_future 是一个给 framework 设计者提供的 helper，它将终端用户的输入统一转换为 Future，方便后续操作。

而作为终端用户，尽可能不使用 ensure_future 函数，而是依赖于 create_task。

## Async Context Manager

同步的上下文管理器依赖于 method call，即 `__enter__` 和 `__exit__`，异步版本也是类似的。不过至于当 `enter` 和 `exit` 是阻塞式 I/O 代码时，才需要异步，否则只要用同步管理器即可。

### The contextlib Way

```py
# use sync manager
from contextlib import contextmanager

@contextmanager
def web_page(url):
    data = download_webpage(url)
    yield data
    update_status(url)


with web_page('google.com') as data:
    preprocess(data)
```

```py
# use async manager
from contextlib import asynccontextmanager

@asynccontextmanager
async def web_page(url):
    # download_webpage should be awaitable
    data = await download_webpage(url)
    # make the func as async generator function
    yield data
    await update_status(url)


async with web_page('google.com') as data:
    preprocess(data)
```

两个版本很接近，但 download_webpage、update_status 不一定容易修改为异步函数。如果它依赖于三方库，就颇为常见了，比如 `requests`。此时就可以用 `run_in_executor` 了。

```py
@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, download_webpage, url)
    yield data
    await loop.run_in_executor(None, update_status, url)


async with web_page('google.com') as data:
    preprocess(data)
```

## Async Iterators

接下来是异步版的 for 循环。同步的 for 循环借助于特殊方法，即 `__iter__` 和 `__next__`。

## Async Generators

TODO:

## Async Comprehensions

TODO:

## Starting Up and Shutting Down (gracefully)

如果关闭 loop 时，有未完成的任务，那么会有 warning 信息：

```py
async def f(delay):
    await asyncio.sleep(delay)

loop = asyncio.get_event_loop()
t1 = loop.create_task(f(1))
t2 = loop.create_task(f(2))
loop.run_until_complete(t1)
loop.close()
```

这就是为何 `run` 会在 close 之前，收集 pending 的任务，将它们 cancel。

下面的示例会演示 shutdown 的各个步骤。

```py

```

# Ch 04 - 20 Async Libs

## Streams API

## The Janus Queue

## aiohttp

### Hello World

```py
from aiohttp import web

async def hello(request):
    return web.Response(text='Hello world')

app = web.Application()
app.router.add_get('/', hello)
web.run_app(app, port=8080)
```

这里没有 loop、task、future 之类，这是其开发者有意为之的，他们隐藏了很多细节。

### Scraping the News

```py
from asyncio import gather, create_task
from string import Template

from aiohttp import web, ClientSession
from bs4 import BeautifulSoup


async def news_fetch(url, postprocess):
    proxy_url = (
        f'http://localhost:8050/render.html?url={url}&timeout=60&wait=1'
    )
    async with ClientSession() as session:
        async with session.get(proxy_url) as resp:
            data = await resp.read()
            data = data.decode('utf-8')
    return postprocess(url, data)


def cnblogs_articles(url, page_data):
    soup = BeautifulSoup(page_data, 'lxml')
    headlines = soup.find_all('a', class_='post-item-title')
    return [(hl['href'], hl.text, 'cnblogs') for hl in headlines]


def csdn_articles(url, page_data):
    soup = BeautifulSoup(page_data, 'lxml')
    def match(tag):
        return tag.has_attr('href') \
               and tag['href'].startswith('https://blog.csdn.net') \
               and tag.has_attr('data-report-click') \
               and '精选头条' in tag['data-report-click']

    headlines = soup.find_all(match)
    return [(hl['href'], hl.p.text, 'csdn') for hl in headlines]


async def news(request):
    sites = [('https://www.cnblogs.com/', cnblogs_articles),
             ('https://www.csdn.net/', csdn_articles)]
    tasks = [create_task(news_fetch(*s)) for s in sites]
    await gather(*tasks)

    items = {
        text: (f'<div class="box {kind}">'
               f'<span>'
               f'<a href="{href}">{text}</a>'
               f'</span>'
               f'</div>')
        for task in tasks for href, text, kind in task.result()
    }
    content = ''.join(items[x] for x in sorted(items))

    page = Template(open('index.html').read())
    return web.Response(
        body=page.safe_substitute(body=content),
        content_type='text/html'
    )

app = web.Application()
app.router.add_get('/news', news)
web.run_app(app, port=8080)
```

## asyncpg and Sanic

TODO:

## Other libs

# Ch 05 - Concluding Thoughts


