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

比`Executor`更为复杂的实现是`ExecutorService`，后者添加了几个方法，如`shutdown`和`awaitTermination`。两个方法一般结合使用。`shutdown`确保已提交的任务完成，但主线程仍可能提前退出，此时就需要用到`awaitTermination`了。

另外，Scala中的`ExecutionContext` trait提供了类似功能，但更适用于Scala。很多Scala方法接受`ExecutionContext`为隐式参数。`ExecutionContext`大致可理解为线程池。`ExecutionContext`对象包含了默认的context实现`global`：

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

## Atomic primitives

`synchronized`和`@volatile`可帮助实现原子操作。本节将了解如何使用**atomic variable**。

### Atomic variables

原子变量支持复杂的线性化操作，线性化操作是指一个操作是瞬时完成的，即它一旦完成，它的结果对于系统中的其它部分都是可见的。比如**volatile variable**。

多种原子操作定义在**java.util.concurrent.atomic**包里。如`AtomicLong`，典型方法是`incrementAndGet`和`decrementAndGet`，这些方法最后依赖于一个基础操作：`compareAndSet`，此操作有时称为**compare-and-swap（CAS）**，CAS操作是lock-free编程的基础构件。

```scala
// incrementAndGet
object AtomicUid extends App {
  private val uid = new AtomicLong(0L)

  def getUniqueId: Long = uid.incrementAndGet()

  execute { log(s"Uid async: $getUniqueId") }
  log(s"Got a uid: $getUniqueId")
}

// CAS
object CasUid extends App {
  private val uid = new AtomicLong(0L)

  @tailrec
  def getUniqueId: Long = {
    val oldId = uid.get()
    val newId = oldId + 1
    if (uid.compareAndSet(oldId, newId)) newId else getUniqueId
  }

  execute { log(s"Uid async: $getUniqueId") }
  log(s"Got a uid: $getUniqueId")
}
```

以CAS方式编程时，retry是常见模式，如上例所示以tailrec持续调用同一方法。

## Lock-free Programming

**lock**是一种同步机制，用以限制多个线程对于同一资源的访问。JVM中每个对象都固有地拥有一个lock，`synchronized`语句可以使用之，保证最多只能有一个线程可执行语句块中的代码。

我们已经了解，使用lock编程容易导致deadlock。并且，如果OS先行”占有“了一个线程，那么它可能会任意地推迟其它线程的执行。这就是lock-free编程的由来。

原子变量可实现无锁操作，无锁操作当然不需要任何锁，从而提高了吞吐量，也免于死锁之困。如上面CAS实现的`getUniqueId`方法。但使用原子变量只是一个必要条件，却非充分条件。

## The ABA problem

The ABA problem is usually a type of a race condition. In some cases, it leads to program errors.

## Lazy values

只要记住，在并发的情形下，Lazy value和singleton对象容易出问题。

* 要特别注意循环依赖的情况
* 注意同一对象用在不同的context下
* 因上条原因，never对public对象使用`synchronized`，而是使用dedicated、private dummy对象。

## 支持并发操作的集合

在多线程中修改Scala标准库中的集合会导致数据损坏，因为这些集合类没有使用任何同步机制。因此，**永远不要在多线程中使用可修改集合类，除非采用了某种合适的同步机制**。具体方法如下：

* 结合使用不可修改集合类与原子变量
* 结合使用不可修改集合类与`synchronized`，此方法可能会有scalability问题（当线程太多时）
* 支持并发操作的集合类

```scala
// synchronized与集合类
object CollectionsSynced extends App {
  val buffer = mutable.ArrayBuffer[Int]()

  def asyncAdd(numbers: Seq[Int]) = execute {
    buffer.synchronized {
      buffer ++= numbers
      log(s"buffer = $buffer")
    }
  }

  asyncAdd(0 until 10)
  asyncAdd(10 until 20)
  Thread.sleep(100)
}
```

## 并发队列

并发编程中一个常见模式是**生产者-消费者（producer-consumer）**模式，比如在Kafka中。这样的模式中，运算被分发到系统不同的部分，从而有了生产者与消费者之分。实现此模式需要的集合类称为**并发队列**。需要特别注意的是，并发队列对于empty和full情形的处理与单线程的队列有所不同。

JDK在`java.util.concurrent`包中包含了若干高效实现的并发队列实现，它们实现的是`BlockingQueue`接口。

注意：**只有在确定没有其它线程修改并发数据结构时才使用iterators**。


