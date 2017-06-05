/**
  * Created by andersc on 06/06/2017.
  */
package object concur {
  def log(s: String): Unit = {
    println(s"${Thread.currentThread.getName}: $s")
  }

  def thread(body: => Unit): Thread = {
    val t = new Thread {
      override def run(): Unit = body
    }
    t.start()
    t
  }
}
