package concur

import scala.collection.mutable.ArrayBuffer

/**
  * Created by andersc on 9/5/17.
  */
object SyncronizedNesting extends App {
  // The ArrayBuffer impl is a collection designed for single-threaded use.
  private val transfers = ArrayBuffer[String]()

  class Account(val name: String, var money: Int)

  def logTransfer(name: String, n: Int) = transfers.synchronized {
    transfers += s"transfer to account '$name' = $n"
  }

  def add(account: Account, n: Int) = account.synchronized {
    account.money += n
    if (n > 10)
      logTransfer(account.name, n) // synchronized is nested.
  }

  val jane = new Account("Jane", 100)
  val john = new Account("John", 200)
  val t1 = thread { add(jane, 5) }
  val t2 = thread { add(john, 50) }
  val t3 = thread { add(jane, 70) }
  t1.join(); t2.join(); t3.join()
  log(s"--- transfers ---\n$transfers")
}

object SynchronizedDeadlock extends App {
  import SyncronizedNesting.Account

  def send(a: Account, b: Account, n: Int): Unit = a.synchronized {
    b.synchronized {
      a.money -= n
      b.money += n
    }
  }

  val a = new Account("Jack", 1000)
  val b = new Account("Jill", 2000)
  // whenever resources are acquired in the same order, there is not danger of deadlock.
  // so establish a total order between resources when acquiring them.
  val t1 = thread { for (i <- 0 until 100) send(a, b, 1) }
  val t2 = thread { for (i <- 0 until 100) send(b, a, 1) }
  t1.join(); t2.join()
  log(s"a = ${a.money}, b = ${b.money}")
}

class Page(val txt: String, var position: Int)

// JVM offers a more lightweight form of sync than `synchronized` block.
// Volative variables can be automatically read and modified, and are mostly used as status flags.
// Two advantages: writes to and reads from volatile vars cannot be `reordered` in a single thread.
// writing to a volatile var is immediately visible to all the other threads.
object Volatile extends App {
  val pages = for (i <- 1 to 5) yield
    new Page("Na" * (1000 - 200 * i) + " Batman!", -1)

  @volatile var found = false

  for (p <- pages) yield thread {
    var i = 0
    while (i < p.txt.length && !found) {
      if (p.txt(i) == '!') {
        p.position = i
        found = true
      } else {
        i += 1
      }
    }
  }

  while (!found) {}
  log(s"results: ${pages.map(_.position)}")
}