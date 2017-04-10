val a = Option("Indeed")
val ns: String = null
val b = Option(ns)

a.isDefined
b.isEmpty

def divide(amt: Double, divisor: Double): Option[Double] = {
  if (divisor == 0) None
  else Option(amt / divisor)
}
divide(1, 0)

val odds = List(1, 3, 5)
val evens = odds filter(_ % 2 == 0)
val firstEven = evens.headOption

val large = odds find (i => i > 5)
// no worry about null pointers
val mapped = odds filter(_ > 10) map (_ * 2)

