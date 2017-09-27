package concur

import scala.collection.mutable

/*
Creating a new thread is much more expensive than creating a new lightweight object such as *Account*.
The same thread should be reused for many requests, a set of such reusable threads is usually called a thread pool.
 */

object SynchronizedBadPool extends App {
  private val tasks = mutable.Queue[() => Unit]()

  val worker = new Thread {
    def poll(): Option[() => Unit] = tasks.synchronized {
      if (tasks.nonEmpty)
        Some(tasks.dequeue())
      else
        None
    }

    // busy-waiting...
    override def run(): Unit = while (true) poll() match {
      case Some(task) => task()
      case None =>
    }
  }

  def asynchronous(body: => Unit) = tasks.synchronized {
    tasks.enqueue(() => body)
  }

  worker.setName("Worker")
  // Generally, a JVM process does not stop when the main thread terminates
  // it terminates when all non-daemon threads terminate.
  worker.setDaemon(true)
  worker.start()

  asynchronous { log("Hello") }
  asynchronous { log(" world!") }
  Thread.sleep(2000)
}

object SynchronizedPool {
  private val tasks = mutable.Queue[() => Unit]()

  def asynchronous(body: => Unit) = tasks.synchronized {
    tasks.enqueue(() => body)
    tasks.notify()
  }

  object Worker extends Thread {
    setDaemon(true)

    def poll() = tasks.synchronized {
      // waits until the main thread adds a code block instead of 'busy-waiting'
      // however, its stack space is not reclaimed until the app terminates.
      while (tasks.isEmpty)
        tasks.wait()
      tasks.dequeue()
    }

    override def run(): Unit = while (true) {
      val task = poll()
      task()
    }
  }

  def main(args: Array[String]): Unit = {

    Worker.start()
    asynchronous { log("Hello") }
    asynchronous { log("World") }
    Thread.sleep(1000)
  }
}

object InterruptSynchronizedPool {
  private val tasks = mutable.Queue[() => Unit]()

  def asynchronous(body: => Unit) = tasks.synchronized {
    tasks.enqueue(() => body)
    tasks.notify()
  }

  object Worker extends Thread {
    var terminated = false

    def poll(): Option[() => Unit] = tasks.synchronized {
      while (tasks.isEmpty && !terminated)
        tasks.wait()

      if (!terminated)
        Some(tasks.dequeue())
      else
        None
    }

    import scala.annotation.tailrec
    @tailrec
    override def run() = poll() match {
      case Some(task) => task(); run()
      case None =>
    }

    def shutdown() = tasks.synchronized {
      terminated = true
      tasks.notify()
    }
  }

  def main(args: Array[String]): Unit = {

    Worker.start()
    asynchronous { log("Hello") }
    asynchronous { log("World") }
    Thread.sleep(1000)
    Worker.shutdown()
  }
}
