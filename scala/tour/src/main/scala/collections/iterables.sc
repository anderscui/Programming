import java.awt.Color

import scala.collection.SortedSet
import scala.collection.mutable.ArrayBuffer

// c1 is a List
val c1 = Iterable(1, 2, 3)

// a Set
val c2 = Set(Color.RED, Color.GREEN, Color.BLUE)

val c3 = Map(Color.RED -> 0xFF0000, Color.GREEN -> 0xFF00, Color.BLUE -> 0xFF)

val c4 = SortedSet("Hello", "World", "About")
for (w <- c4) {
  println(w)
}

// conversions
val col1 = Seq(1, 1, 2, 3, 5)
val set = col1.toSet
val buffer = col1.to[ArrayBuffer]

