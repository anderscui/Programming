import scala.collection.mutable.ArrayBuffer

val names = List("Peter", "Paul", "Mary")
val upper = names.map(_.toUpperCase)
val upper2 = for (name <- names) yield name.toUpperCase

// transform in-place
val buffer = ArrayBuffer("Peter", "Paul", "Mary")
buffer.foreach(println)

// collect
"-1+2-3".collect { case '+' => 1; case '-' => -1}
