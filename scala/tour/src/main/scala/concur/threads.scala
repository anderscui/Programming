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
    t.join()
    log("New thread joined.")
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

  def getUniqueId() = {
    // not atomic
    val freshUid = uidCount + 1
    uidCount = freshUid
    freshUid
  }

  def printUniqueIds(n: Int): Unit = {
    val uids = for (i <- 0 until n) yield getUniqueId()
    log(s"Generated uids: $uids")
  }

  def main(args: Array[String]): Unit = {
    // a race condition
    val t = thread { printUniqueIds(5) }
    printUniqueIds(5)
    t.join()
  }
}

object SynchronizedUid {
  var uidCount = 0L

  // don't omit "this" object.
  // each object on the JVM has a special built-in *monitor lock*, also called *intrinsic lock*.
  // when a thread calls the synchronized statement on an x object, it gains ownership of the monitor lock.
  def getUniqueId() = this.synchronized {
    val freshUid = uidCount + 1
    uidCount = freshUid
    freshUid
  }

  def printUniqueIds(n: Int): Unit = {
    val uids = for (i <- 0 until n) yield getUniqueId()
    log(s"Generated uids: $uids")
  }

  def main(args: Array[String]): Unit = {
    val t = thread { printUniqueIds(5) }
    printUniqueIds(5)
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
      // the JVM is allowed to reorder certain program statements executed by one thread
      // as long as it does not change the serial semantics of the program.
      // additionally, the threads do not need to write all their updates to the main memory immediately.
      val t1 = thread {
        a = true
        y = if (b) 0 else 1
      }
      // We always need to apply proper sync to ensure that the writes by one thread
      // are VISIBLE to antoher thread.
      // Writes by any thread executing the synchronized statement on an x object are not only atomic,
      // but also visible to threads that execute synchronized on x.
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
          // on gaining ownership of the monitor, the thread can witness the memory writes of all the
          // threads that previously released that monitor.
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
