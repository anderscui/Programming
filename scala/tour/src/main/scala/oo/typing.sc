object ImplicitClasses {
  implicit class Hello(s: String) { def hello = s"Hello, $s"}
  def test = {
    println("World".hello)
  }
}

ImplicitClasses.test

object ImplicitParams {
  def greet(name: String)(implicit greeting: String) = s"$greeting, $name"
  implicit val hi = "Hello"
  def test = {
    println(greet("Developers"))
  }
}

ImplicitParams.test

// Type param uppper bound （:<) and lower bound (>:)
class Base { var i = 10 }; class Sub extends Base

def inc[B <: Base](b: Base) = { b.i += 1; b }

// List is covariant
val l: List[Base] = List[Sub]()

// Tuples
val t: (Int, Int) = Tuple2(10, 20)
println("Does the arity = 2? " + (t.productArity == 2))

// Functions
val hello1 = (s: String) => s"Hello, $s"
val h1 = hello1("Function Literals")

val hello2 = new Function[String, String] {
  override def apply(s: String): String = s"Hello, $s"
}
val h2 = hello2("Function Instances")

// Compose functions
val doubler = (i: Int) => i * 2
val plus3 = (i: Int) => i + 3

(doubler andThen plus3)(2)
(doubler compose plus3)(2)

implicit class ArrowAssoc[A](x: A) {
  def ->[B](y: B) = Tuple2(x, y)
}

val t2 = 1 -> "B"
