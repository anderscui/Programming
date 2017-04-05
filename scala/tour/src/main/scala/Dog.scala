/**
  * Created by andersc on 4/5/17.
  */
class Dog(br: String) {
  // ctor here
  var breed: String = br

  // def a method
  def bark = "Woof, woof!"

  // values and methods are assumed public
  private def sleep(hours: Int) =
    println(s"I'm sleeping for $hours hours")
}

// "object" creates a type AND a singleton instance of it.
object Dog {
  def allKnowBreeds = List("pitbull", "shepherd", "retriever")
  def createDog(breed: String) = new Dog(breed)
}

// The primary purpose of case classes is to hold immutable data.
// Case classes also get pattern matching for free
case class Person(name: String, phoneNumber: String)


