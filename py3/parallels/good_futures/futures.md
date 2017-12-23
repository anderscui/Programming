# concurrent.futures

The two classes manage an internal pool of worker threads or processes, and a queue of tasks to be executed. But the interface is very high level.

Common mode: turning the body of a sequential `for` loop into a function to be called concurrently.

As of Python 3.4, there are two classes named `Future` in the standard lib: `concurrent.futures.Future`和`asyncio.Future`。
They represents a deferred computation that may or may not have completed, this is similar to the `Deferred` in Twisted, `Future` in Tornado, and `Promise` objects in various JS libs. 

Futures encapsulate pending operations so that they can be put in queues, their state of completion can be queued, and their results or exceptions can be retrieved when available.

## ThreadPoolExecutor

The `executor.__exit__` method will call `executor.shutdown(wait=True)`, which will block until all threads are done.

## ProcessPoolExecutor

