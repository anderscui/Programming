val greetings = new Array[String](3)
greetings(0) = "hello"
greetings(1) = ", "
greetings(2) = "world!\n"

for (s <- greetings)
  print(s)

//val l1 = List(("2", 0.1, "A"), ("1", 0.2, "A"), ("3", 0.15, "A"))
//val l2 = List(("2", 0.5, "B"), ("1", 0.1, "B"), ("3", 0.25, "B"))

val l1 = List(("2", 0.1), ("1", 0.2), ("3", 0.15))
val l2 = List(("2", 0.5), ("1", 0.1), ("3", 0.25))

val merged = l1.map(elem => (elem._1, elem._2, "A")) ++ l2.map(elem => (elem._1, elem._2, "B"))
merged.sortBy(i => i._2).reverse