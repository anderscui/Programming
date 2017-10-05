# Traditional Building Blocks of Concurrency

Although these building blocks do not solve all the issues of concurrent programming, they simplify the reasoning about concurrent programs and **can be found across concurrency frameworks and libraries of many languages**, including Scala.

Two aspects of a concurrent programming model:

* Expressing concurrency, e.g. threads;
* Data access, e.g. `synchronized` and `@volatile`

This chapter includes the following topics:

* `Executor` and `ExecutionContext`
* Atomic primitives for non-blocking sync
* Lazy values and concurrency
* Using concurrent collections
* Create processes and communicate with them

## The `Executor` and `ExecutionContext` objects

Thread creation takes less computational time compared to process, it's still much more expensive than allocating a single object, acquiring a monitor lock, or updating an entry in a collection.

Most concurrency frameworks have facilities that maintain a set of threads in a waiting state and start running when concurrently executable work tasks become available. We call such facilities **thread pools**.

JDK包含了一个`Executor`，此接口仅包含一个`execute`方法。它接受一个`Runnable`对象，并调用对象的`run`方法，`Executor`会觉得在那个线程上以及何时调用`run`。JDK7中有一个`Executor`实现，即`ForkJoinPool`。

`Executor`对象将并发运算中的逻辑与运算本身如何执行**解耦**。这样程序员只需要关注逻辑的实现。

比`Executor`更为复杂的实现是`ExecutorService`，后者添加了几个方法，如`shutdown`和`awaitTermination`。两个方法一般结合使用。

另外，Scala中的`ExecutionContext` trait提供了类似功能，但更适用于Scala。很多Scala方法接受`ExecutionContext`为隐式参数。`ExecutionContext`对象包含了默认的context实现`global`：

```scala
object ExecutionContextGlobal extends App {
  val ectx = ExecutionContext.global
  ectx.execute(new Runnable {
    override def run(): Unit = log("Running on exec context.")
  })
  Thread.sleep(500)
}
```

`ExecutionContext`对象定了一对儿方法`fromExecutor`和`fromExecutorService`。

