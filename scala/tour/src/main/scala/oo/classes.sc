// simplest class
class User

val u = new User
u.isInstanceOf[AnyRef]

//
class User2(userName: String) {
  val name: String = userName
  val greet: String = s"Hello from $name"

  override def toString: String = s"User($name)"
}
val u2 = new User2("Zeniba")
println(u2.greet)

// fields in the ctor
class User3(val name: String) {
  def greet: String = s"Hello from $name"

  override def toString: String = s"User($name)"
}
val users = List(new User3("Shoto"), new User3("Art3mis"))
users map (_.name.size)
users sortBy (_.name)

// inheritance
class A {
  def hi = "Hello from A"

  override def toString: String = getClass.getName
}

class B extends A
class C extends B {
  override def hi: String = "hi C -> " + super.hi
}

new A().hi
new B().hi
new C().hi

//
class Car(val make: String, var reserved: Boolean = true) {
  def reserve(r: Boolean) = { reserved = r}
}

class Lotus(val color: String, reserved: Boolean) extends Car("Lotus", reserved)

// type parameter
class Singular[A](element: A) extends Traversable[A] {
  override def foreach[U](f: (A) => U): Unit = f(element)
}

val p = new Singular("Planes")
p foreach println

