package concur

import scala.collection.mutable

object ThreadsMain extends App {
  val t = Thread.currentThread
  println(s"I am the thread ${t.getName}")
}

object ThreadsCreation extends App {
  val t = thread { println("New thread running..."); 1 }
  // halts the execution of the main thread until t completes its execution.
  t.join()
  println("New thread joined.")
}

object ThreadsSleep {
  def main(args: Array[String]): Unit = {
    val t = thread {
      // the order is deterministic
      Thread.sleep(1000)
      log("New thread running...")
      Thread.sleep(1000)
      log("Still running...")
      Thread.sleep(1000)
      log("Completed...")
    }
  }
}

object Nondeterminism {
  def main(args: Array[String]): Unit = {
    val t = thread { log("New thread running...") }
    log("...")
    log("...")
    t.join()
    log("New thread joined")
  }
}

object UnprotectedUid {
  var uidCount = 0L

  def getUid() = {
    // not atomic
    val freshUid = uidCount + 1
    uidCount = freshUid
    freshUid
  }

  def printUids(n: Int): Unit = {
    val uids = for (i <- 0 until n) yield getUid()
    log(s"Generated uids: $uids")
  }

  def main(args: Array[String]): Unit = {
    // a race condition
    val t = thread { printUids(5) }
    printUids(5)
    t.join()
  }
}

object SynchronizedUid {
  var uidCount = 0L

  // don't omit "this" object.
  def getUid() = this.synchronized {
    val freshUid = uidCount + 1
    uidCount = freshUid
    freshUid
  }

  def printUids(n: Int): Unit = {
    val uids = for (i <- 0 until n) yield getUid()
    log(s"Generated uids: $uids")
  }

  def main(args: Array[String]): Unit = {
    val t = thread { printUids(5) }
    printUids(5)
    t.join()
  }
}

object SharedStateAccessReordering {
  def main(args: Array[String]): Unit = {
    for (i <- 0 until 100000) {
      var a = false
      var b = false
      var x = -1
      var y = -1
      val t1 = thread {
        a = true
        y = if (b) 0 else 1
      }
      val t2 = thread {
        b = true
        x = if (a) 0 else 1
      }
      t1.join()
      t2.join()
      assert(!(x == 1 && y == 1), s"x = $x, y = $y")
    }
  }
}

object SharedStateAccessReorderingSync {
  def main(args: Array[String]): Unit = {
    for (i <- 0 until 100000) {
      var a = false
      var b = false
      var x = -1
      var y = -1
      val t1 = thread { this.synchronized {
          a = true
          y = if (b) 0 else 1
        }
      }
      val t2 = thread { this.synchronized {
          b = true
          x = if (a) 0 else 1
        }
      }
      t1.join()
      t2.join()
      assert(!(x == 1 && y == 1), s"x = $x, y = $y")
    }
  }
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