import java.util.Calendar
import java.time.format.DateTimeFormatter
import java.time.{Instant, ZoneId, ZonedDateTime}

import scala.concurrent.ExecutionContext

/**
  * Created by andersc on 06/06/2017.
  */
package object concur {
  val datetimeFormater = DateTimeFormatter.ISO_OFFSET_DATE_TIME

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

  def execute(body: => Unit): Unit = ExecutionContext.global.execute(() => body)

  def now(): String = {
    datetimeFormater.format(ZonedDateTime.now())
  }
}
