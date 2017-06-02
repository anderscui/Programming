import oo.Person
//import Person

def matchPerson(person: Person): String =
  person match {
    case Person("George", number) => "George found, his number is " + number
    case Person("Kate", number) => "Kate found, her number is " + number
    case Person(name, number) => "someone else found: " + name + ", phone: " + number
  }

println(matchPerson(Person("George", "123")))
println(matchPerson(Person("Steve", "123")))

val email = "(.*)@(.*)".r

def matchEverything(obj: Any): String = obj match {
  case "Hello world" => "Got the string"
  case x: Double => "Got a double: " + x
  case x: Int if x > 1000 => "Got a pretty big number"
  case Person(name, number) => s"Got contact info for $name"
  case email(name, domain) => s"Got email addr $name@$domain"
  case (a: Int, b: Double) => s"Got a tuple: $a, $b"
  case _ => "Got unknown object"
}

println(matchEverything("a@b.c"))
println(matchEverything(1, 2.0))
println(matchEverything("test"))

val s: Some[Any] = Some(1)
s match {
  case Some(v: String) => println(v)
  case _ => println("Others")
}