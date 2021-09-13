threading - 基于线程的并行实现

参考：

* [threading - Thread-based parallelism](https://docs.python.org/3/library/threading.html)
* [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)

# 什么是线程（What Is a Thread?）

线程是独立的执行路径，这样，程序可以同时有两个任务在执行。但在 Python 3 中，只是看起来如此，这是因为 **GIL** 的存在。要真地实现**同时**执行，需要使用 `multitiprocessing` 模块。

如果问题中的多个任务所花费的时间大部分在等待外部服务，那么该问题可以**考虑**使用多线程来解决。而如果问题中的任务需要繁重的 CPU 计算，那么使用多线程不会提升性能。

有时候，使用多线程也能让设计更为清晰和已读。

# 开始线程（Starting a Thread）

`threading` 模块基于 `_thread` 模块构建了高层的线程接口。

在 CPython 中，由于 `GIL` 的存在，每个时刻只能有一个线程执行。如果需要更好地利用多核机器的计算资源，建议使用 `multiplethreading` 或 `concurrent.future.ProcessPoolExecutor`。

`threading` 包含了很多 primitive，具体可参考官方文档。

# 最简单的例子

```python
import logging
import threading
import time

def thread_func(name):
    logging.info(f'thread {name} - {threading.get_ident()}: starting')
    time.sleep(0.5)
    logging.info(f'thread {name}: finishing')

if __name__ == '__main__':
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt='%H:%M:%S')

    logging.info('main: before creating')
    x = threading.Thread(target=thread_func, args=('second',))
    logging.info('main: before running')
    x.start()
    logging.info('main: wait for finishing')
    logging.info('main: job done')
```

可以看到，主线程先执行完毕，子线程在这之后完成。

如果你了解 **daemon** 线程，应该知道它是在后台执行的，并且在主线程结束后立即停止，所以这里的子线程不是 daemon 线程。

`threading._shutdown()` 函数会检查所有的非 daemon 线程，调用每个线程的 `.join()` 方法。

通常这是你需要的方式，但有时也需要其它可能的选项。比如 daemon 线程可通过 Thread 的 `daemon` 参数设置。

如果不想在程序结束时才等待子线程结束，那么可以手动调用 `.join()`。该方法让当前线程等待另一个线程的结束。

# 使用更多线程

通过上述方式，很容易创建多个线程，比如通过一个循环，依次创建线程并 `start` 之，之后再逐一调用 `join`。此时，线程执行的顺序是不确定的，或者说不是程序能确定，它取决于 OS。

Python 提供了若干机制，可帮助控制多个线程的执行。

# 使用 `ThreadPoolExecutor`

上述手工管理线程的方式，容易替换成 `ThreadPoolExecutor`，但它依然不能确定执行顺序。

# 竞态条件（Race Conditions）

当两个或更多线程要访问同一份数据或资源时，竞态条件可能会发生。

```python
import time
from concurrent.futures import ThreadPoolExecutor

class FakeDb:
    def __init__(self):
        # shared data
        self.value = 0

    def update(self, name):
        print(f'thread {name}: starting update')
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print(f'thread {name}: finishing update')

if __name__ == '__main__':
    db = FakeDb()
    print(f'starting value is {db.value}')
    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(2):
            executor.submit(db.update, i)

    print(f'ending value is {db.value}')
```

这里的代码用于确保每次都会发生竞态条件。实际开发中，简单如 `x = x + 1` 的语句都可能会导致竞态条件的发生，这是因为语句的**原子性**会有影响。

# 使用 `Lock` 完成基本的同步操作

解决竞态条件的一种方法是使用 `Lock`，在其它语言中可能叫 `mutex`，意为互斥。它在同一时间内只允许一个线程访问某一段代码，从而避免了竞争。

一旦一个线程获得了锁，其它线程就必须等待之。基本的函数是 `.acquire` 和 `.release`。这里的一个潜在问题是，如果一个线程获得了锁但没有释放，那么程序就会”卡“在那里。

另外还有一个 `RLock` 类值得关注。

# 生产者-消费者线程问题（Producer-Consumer Threading）

Producer-Consumer Problem 是 CS 中的一个标准问题，用于查看线程或进程的同步问题。

作为示例，想象一个程序，它需要从网络中读取信息并吸入数据库。程序不是在需要时请求信息，而是要侦听和接收信息，信息的到来也不是按固定频率，可能会突然涌入。程序的这一部分称为**生产者**。

另一部分，接收到一个信息后，需要写入数据库。数据库访问是很慢的，但平均来看，仍然能足以写入所有接收到的信息。这一部分是**消费者**。

生产者和消费者之间的部分称为 `Pipeline`。

## Lock 实现

```python
import random
import threading
from concurrent.futures import ThreadPoolExecutor

SENTINEL = object()


def producer(pipeline):
    """Pretend getting msgs from the network"""
    for i in range(10):
        msg = random.randint(1, 100)
        pipeline.set_message(msg, 'producer')

    # send a sentinel to tell consumer it's done
    pipeline.set_message(SENTINEL, 'producer')


def consumer(pipeline):
    """Pretend saving msg to the db"""
    msg = 0
    while msg is not SENTINEL:
        msg = pipeline.get_message('consumer')
        if msg is not SENTINEL:
            print(f'consumer storing msg: {msg}')


class Pipeline:
    """Allows a single element pipeline between producer and consumer."""
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        self.consumer_lock.acquire()
        print(f'{name}: have getlock')
        message = self.message
        self.producer_lock.release()
        print(f'{name}: setlock released')
        return message

    def set_message(self, message, name):
        self.producer_lock.acquire()
        print(f'{name}: have setlock')
        self.message = message
        self.consumer_lock.release()
        print(f'{name}: getlock released')


if __name__ == '__main__':
    pipeline = Pipeline()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
```

`__init__` 中，消费者的 lock 被 acquired，当前不能消费，因为此时还没有任何消息。`set_message` 中，写入一条新消息后，可以获取了。

这种实现，消息的生产与消费必须逐一成对儿进行。也就是 pipeline 中最多只能有一条消息存在。更好的实现需要使用 `Queue`。

## Queue 实现

如果希望 pipeline 能够处理多条消息，那么 pipeline 数据结构需要能够根据需要有可变的容量。这里可以使用 `Queue`。要停止工作线程，也需要使用不同的 primitive，即 `threading.Event`。

```python
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


def producer(pipeline, event):
    """Pretend getting msgs from the network"""
    while not event.is_set():
        msg = random.randint(1, 100)
        pipeline.set_message(msg, 'producer')

    print(f'producer received EXIT event, exiting...')


def consumer(pipeline, event):
    """Pretend saving msg to the db"""
    while not event.is_set() or not pipeline.empty():
        msg = pipeline.get_message('consumer')
        print(f'consumer storing msg: {msg} (queue size={pipeline.qsize()}')

    print(f'consumer received EXIT event, exiting...')


class Pipeline(Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        print(f'{name}: about to get from queue')
        value = self.get()
        print(f'{name}: got {value} from queue')
        return value

    def set_message(self, value, name):
        print(f'{name}: about to add {value} to queue')
        self.put(value)
        print(f'{name}: added {value} to queue')


if __name__ == '__main__':
    pipeline = Pipeline()
    event = threading.Event()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.01)
        print(f'main: about to set event')
        event.set()
```

通过 `Event` 来通知 pipeline 的结束。

# Threading Objects

## Semaphore

Semaphore 经常用于保护具有有限容量的资源，比如连接池。

## Timer

# Barrier

`Barrier` 可用于保持若干线程间的同步。
