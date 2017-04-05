// Functional Programming
val add10: Int => Int = _ + 10
List(1, 2, 3) map add10

// anonymous func
List(1, 2, 3) map (x => x + 10)

List(1, 2, 3) map (_ + 10)

List(1, 2, 3) foreach println

// Combinators
List(1, 2, 3) filter (_ > 2)

List(
  Person(name = "Dom", phoneNumber = "1"),
  Person(name = "Bob", phoneNumber = "2")
).filter(_.name > "Candy")

// For comprehensions
val nums = (1 to 10).toList
val sq: Int => Int = x => x * x
for { n <- nums } yield sq(n)
for { n <- nums if n < 5} yield sq(n+n)

// Implicits
implicit val myInt = 1000
implicit def myImpFunc(breed: String) = new Dog("Golden " + breed)

def sendGreetings(toWhom: String)(implicit howMany: Int) =
  s"Hello, $toWhom, $howMany blessings to you and yours!"

sendGreetings("John")(100)
sendGreetings("Jane")

"Sheperd".bark

