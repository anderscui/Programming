for (i <- 0 to 2) {
  print(i)
}

// 0 to 2 is actually 0.to(2)
0.to(2).toList

// 1 + 2 => 1.+(2)
1.+(2)

// apply and update
val greetings = new Array[String](3)
greetings(0) = "hello"
greetings(1) = ", "
greetings(2) = "world!\n" // greetings.update(2, "world!\n")

greetings(0) // greetings.apply(0)