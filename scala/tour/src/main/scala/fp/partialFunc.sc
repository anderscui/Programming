def sum(a: Int, b: Int, c: Int) =
  a + b + c

// _ is a placeholder
val fa = sum _
val fb = sum(1, _: Int, 3)

