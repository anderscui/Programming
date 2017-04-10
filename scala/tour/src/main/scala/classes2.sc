import com.sun.tools.doclets.internal.toolkit.util.DocFinder.Input

abstract class Car {
  val year: Int
  val automatic: Boolean = true
  def color: String
}

class RedMini(val year: Int) extends Car {
  def color = "Red"
}

val c: Car = new RedMini(2010)

// use `field` for `method`?
class Mini(val year: Int, val color: String) extends Car

val mini: Car = new Mini(2005, "Red")

// anonymous
abstract class Listener { def trigger }
val listener = new Listener {
  override def trigger { println(s"Trigger at ${new java.util.Date}")}
}
listener.trigger

// apply
class Multiplier(factor: Int) {
  def apply(input: Int) = input * factor
}

val triple = new Multiplier(3)
triple.apply(10)
triple(10)

val l = (1 to 5).toList
l.apply(1)
l(1)










