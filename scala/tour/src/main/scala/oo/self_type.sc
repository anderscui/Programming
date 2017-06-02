class A { def hi = "hi" }

trait B { self: A =>
  override def toString: String = "B: " + hi
}

class C extends A with B
new C()