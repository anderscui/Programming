//https://learnxinyminutes.com/docs/scala/

println("Hello, world")
println(10)

val d: Double = 1.0

val s = "Scala strings"
val len = s.length
val sub = s.substring(2, 5)
val sub2 = s.take(5)

// String interpolation
val n = 45
val s2 = s"We have $n apples"

val a = Array(11, 9, 6)
val s3 = s"My second daughter is ${a(0) - a(2)} years old."

// Raw strings
val raw = raw"New line feed: \n. Carriage return: \r."
val escaped = "They stood outside the \"Rose and Crown\""

// 2. Functions
def sumOfSquares(x: Int, y: Int) = {
  val x2 = x * x
  val y2 = y * y
  x2 + y2
}

val sum = sumOfSquares(y = 4, x = 3)

// default param
def addWithDefault(x: Int, y: Int = 5) = x + y

// anonymous func
val sq: Int => Int = x => x * x
val sq2 = sq(10)

// shorter parameters
val addOne: Int => Int = _ + 1
val weirdSum: (Int, Int) => Int = (_ * 2 + _ * 3)

weirdSum(2, 4)

// return statement should be avoided
def foo(x: Int): Int = {
  val anonFunc: Int => Int = { z =>
    if (z > 5)
      return z
    else
      z + 2
  }
  anonFunc(x)
}

foo(6)
foo(4)

// 3. Flow control
val r = 1 to 5
r.foreach(println)
r foreach println

// A while loop
var i = 0
while (i < 10) { println("i = " + i); i += 1 }

// i

// Conditions
println(if (i == 10) "yeah" else "nope")

// 4. Data Structures
val arr = Array(1, 2, 3, 5, 8, 13)
println(arr(0))

val m = Map("fork" -> "tenedor", "spoon" -> "cuchara", "knife" -> "cuchillo")
println(m("fork"))

val safeM = m.withDefaultValue("no lo se")

val set1 = Set(1, 3, 7)
println(s(0))

// Tuples
val t = (1, 2)
val divideInts = (x: Int, y: Int) => (x / y, x % y)
val ints = divideInts(10, 3)
println(ints._2)
val (div, mod) = divideInts(10, 3)

// 5. OOP
// the only top-level constructs
// objects
// classes
// case classes
// traits
val mydog = new Dog("greyhound")
println(mydog.breed)
println(mydog.bark)

val george = Person("George", "123")
val kate = Person("Kate", "567")
println(kate.phoneNumber)

// easy to copy
val otherKate = kate.copy(phoneNumber = "789")