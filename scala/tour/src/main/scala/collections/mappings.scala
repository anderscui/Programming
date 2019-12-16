package collections

import scala.collection.mutable.ArrayBuffer

object mappings {
  def main(args: Array[String]): Unit = {
    val buffer = ArrayBuffer("Peter", "Paul", "Mary")
    buffer.foreach(println)
  }
}
