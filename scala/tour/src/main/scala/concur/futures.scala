package concur

import scala.concurrent.{Await, Future}
import scala.concurrent.duration._
import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.{Failure, Random, Success}

/**
  * Created by andersc on 5/15/17.
  */
object futures {

  def sleep(time: Long): Unit = {
    Thread.sleep(time)
  }

  def main(args: Array[String]): Unit = {
    //blocking
    callback
  }

  private def blocking = {
    implicit val baseTime = System.currentTimeMillis

    val f = Future {
      sleep(500)
      1 + 1
    }

    val result = Await.result(f, 1 second)
    println(result)

    sleep(1000)
  }

  private def callback = {

    println("starting calc...")

    implicit val baseTime = System.currentTimeMillis

    val f = Future {
      sleep(Random.nextInt(1000))
      42
    }

    println("before onComplete")

    f.onComplete {
      case Success(value) => println(s"Got the result: $value")
      case Failure(e) => e.printStackTrace()
    }

    println("A ..."); sleep(100)
    println("B ..."); sleep(100)
    println("C ..."); sleep(100)

    sleep(1000)
  }
}
