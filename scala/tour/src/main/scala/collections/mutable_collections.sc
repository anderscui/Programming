import java.io.File

// ** mutable
val m = Map("AAPL" -> 597, "MSFT" -> 40)
val n = m - "AAPL" + ("GOOG" -> 521)

val nums = collection.mutable.Buffer(1)
for (i <- 2 to 10) nums += i
nums
nums.toList

val b = n.toBuffer
b += ("GOOG" -> 521)
b.toSet

val bs = Set.newBuilder[Char]
bs += 'h'
bs ++= List('e', 'l', 'l', 'o')

// Arrays
val colors = Array("red", "green", "blue")
colors(0) = "purple"

val files = new File(".").listFiles()
val scala = files map (_.getName) filter (_ endsWith "scala")

// Seqs
val inks = Seq('c', 'm', 'y', 'k')

val hi = "Hello, " ++ "worldly" take 12 replaceAll ("w", "W")

// mutable map
val map = collection.mutable.Map[Int, String]()
map += (1 -> "one")
map += (2 -> "two")
map += (3 -> "three")

for ((k, v) <- map) {
  println(k, v)
}

// mutable set
val set = collection.mutable.Set[String]()
set += "Hello"
set += "World"
set contains "Hello"