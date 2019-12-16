package concur

import java.time._

import scala.concurrent._
import scala.concurrent.duration._
import ExecutionContext.Implicits.global
import scala.util.{Failure, Random, Success}

object inFuture {
  def useFuture(): Unit = {
    Future {
      Thread.sleep(500)
      println(s"This is the future at ${LocalTime.now()}")
    }
    println(s"This is the present at ${LocalTime.now()}")
    Thread.sleep(500)
  }

  def valueOfFuture(): Unit = {
    val f = Future {
      //Thread.sleep(2000)
      if  (LocalTime.now.getHour > 12)
        throw new Exception("in the night")
      42
    }
    // now the future is <not completed>
    println(f)
    Thread.sleep(500)
    // now the future is Some(v) or Failure(Exception)
    println(f)
  }

  def waitingForFuture(): Unit = {
    val f = Future {
      Thread.sleep(500); 42
    }
//    // get the value or TimeOutException
//    val result = Await.result(f, 200.milliseconds)
//    print(result)

    // to avoid excepitons, use ready
    Await.ready(f, 900.milliseconds)
    val Some(t) = f.value
//    if (t.isSuccess) {
//      println("sss")
//    }
    t match {
      case Success(v) => println(s"The answer is $v")
      case Failure(ex) => println(ex.getMessage)
    }
    // or use toOption
    val result = t.toOption
    if (result.isEmpty) {
      println("no result")
    } else {
      println(s"the answer is ${result.get}")
    }
  }

  def callback(): Unit = {
    val random = new Random()
    val f = Future {
      Thread.sleep(300)
      if (random.nextFloat() < 0.5) throw new Exception("insufficient gold")
      42
    }
    f.onComplete {
      case Success(v) => println(s"The answer is $v")
      case Failure(ex) => println(ex.getMessage)
    }
    // seems this is required.
    Thread.sleep(600)
  }

  def compose(): Unit = {
    val f1 = Future { Thread.sleep(200); 42}
    val f2 = Future { Thread.sleep(200); 43}
    f1.onComplete {
      case Success(n1) =>
        f2.onComplete {
          case Success(n2) => {
            println(s"result is ${n1+n2}")
          }
          case Failure(ex) => println("f2 failed")
        }
      case Failure(ex) => println("f1 failed")
    }
    Thread.sleep(500)
  }

  def composeMap(): Unit = {
    val f1 = Future { Thread.sleep(200); 42}
    val f2 = Future { Thread.sleep(200); 43}
    val combined = f1.flatMap(n1 => f2.map(n2 => n1+n2))
    combined.onComplete {
      case Success(n) =>
        println(s"result is $n")
      case Failure(ex) => println("combined failed")
    }
    Thread.sleep(500)
  }

  def composeFor(): Unit = {
    val f1 = Future { Thread.sleep(200); 42}
    val f2 = Future { Thread.sleep(200); 43}
    val combined = for (n1 <- f1; n2 <- f2 if n1 != n2) yield n1 + n2
    combined.onComplete {
      case Success(n) =>
        println(s"result is $n")
      case Failure(ex) => println("combined failed")
    }
    Thread.sleep(500)
  }

  def seq(): Unit = {
    println(s"start at ${LocalTime.now()}")

    val parts = (1 to 24).toList
    val futures = parts.map(i => Future {
      Thread.sleep(100)
      i * i
    })
    val result = Future.sequence(futures)
    result.onComplete {
      case Success(n) =>
        println(s"result is $n")
        println(s"end at ${LocalTime.now()}")
      case Failure(ex) => println("failed")
    }
    Thread.sleep(500)
  }

  def main(args: Array[String]): Unit = {
    // useFuture()
    // valueOfFuture()
    // waitingForFuture()
    // callback()
    // compose()
    // composeMap()
    // composeFor()
    seq()
  }
}
