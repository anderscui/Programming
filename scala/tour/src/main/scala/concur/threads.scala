package concur

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