val greetings = new Array[String](3)
greetings(0) = "hello"
greetings(1) = ", "
greetings(2) = "world!\n"

for (s <- greetings)
  print(s)
