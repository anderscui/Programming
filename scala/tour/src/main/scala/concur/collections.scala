package concur

import java.util.concurrent.atomic.AtomicReference

import scala.annotation.tailrec
import scala.collection._

object CollectionsBad extends App {
  val buffer = mutable.ArrayBuffer[Int]()

  def asyncAdd(numbers: Seq[Int]) = execute {
    buffer ++= numbers
    log(s"buffer = $buffer")
  }

  asyncAdd(0 until 10)
  asyncAdd(10 until 20)
  Thread.sleep(100)
}

class AtomicBuffer[T] {
  private val buffer = new AtomicReference[List[T]](Nil)

  def data: List[T] = buffer.get

  @tailrec
  final def +=(x: T): Unit = {
    val xs = buffer.get
    val nxs = x :: xs
    if (!buffer.compareAndSet(xs, nxs))
      this += x
  }
}

object CollectionsAtomic extends App {
  val buffer = new AtomicBuffer[Int]

  def asyncAdd(numbers: Seq[Int]) = execute {
    for (num <- numbers) {
      buffer += num
      log(s"buffer = ${buffer.data}")
    }
  }

  asyncAdd(0 until 10)
  asyncAdd(10 until 20)
  Thread.sleep(100)
}

object CollectionsSynced extends App {
  val buffer = mutable.ArrayBuffer[Int]()

  def asyncAdd(numbers: Seq[Int]) = execute {
    buffer.synchronized {
      buffer ++= numbers
      log(s"buffer = $buffer")
    }
  }

  asyncAdd(0 until 10)
  asyncAdd(10 until 20)
  Thread.sleep(100)
}
