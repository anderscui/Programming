package concur

import scala.collection.mutable.ArrayBuffer

/**
  * Created by andersc on 9/5/17.
  */
object SyncronizedNesting extends App {
  private val transfers = ArrayBuffer[String]()

  class Account(val name: String, var money: Int)

  def logTransfer(name: String, n: Int) = transfers.synchronized {
    transfers += s"transfer to account '$name' = $n"
  }

  def add(account: Account, n: Int) = account.synchronized {
    account.money += n
    if (n > 10)
      logTransfer(account.name, n)
  }

  val jane = new Account("Jane", 100)
  val john = new Account("John", 200)
  val t1 = thread { add(jane, 5) }
  val t2 = thread { add(john, 50) }
  val t3 = thread { add(jane, 70) }
  t1.join(); t2.join(); t3.join()
  log(s"--- transfers ---\n$transfers")
}
