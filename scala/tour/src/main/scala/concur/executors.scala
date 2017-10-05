package concur

//import scala.concurrent._
import java.util.concurrent.ForkJoinPool
import java.util.Calendar

import scala.concurrent.ExecutionContext

object ExecutorsCreate extends App {
  val executor = new ForkJoinPool
  executor.execute(() => log("This is a run async."))

  // prevent the daemon threads in the ForkJoinPool from being terminated.
  Thread.sleep(500)
}

object ExecutionContextGlobal extends App {
  val ectx = ExecutionContext.global
  ectx.execute(new Runnable {
    override def run(): Unit = log("Running on exec context.")
  })
  Thread.sleep(500)
}

object ExecutionContextCreate extends App {
  // parallelism level 2 (2 threads in its pool)
  val pool = new ForkJoinPool(2)
  val ectx = ExecutionContext.fromExecutorService(pool)
  ectx.execute(() => log("Running on exec context again."))

  Thread.sleep(500)
}

object ExecutionContextSleep extends App {
  for (i <- 1 to 32) execute {
    Thread.sleep(500)
    log(s"Task $i completed...")
    println(now())
  }
  log("waiting...")
  Thread.sleep(5000)
  println(now())
}
