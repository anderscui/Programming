/**
  * Returns the input string without leading or trailing
  * whitespace, or null if the input is null.
  * @param s the input string to trim, or null
  * @return
  */
def safeTrim(s: String): String = {
  if (s == null)
    return null
  s.trim
}

safeTrim(" test   ")

def log(d: Double) = println(f"Got value $d%.2f")
log(3.1415)

// deprecated syntax
def log2(d: Double) { println(f"Got value $d%.2f") }

// empty parentheses, or input-less func
def hi(): String = "hi"

// params groups
def max(x: Int)(y: Int) = if (x > y) x else y

val larger = max(10)(50)

// type params
def id[A](a: A): A = a

val s = id("Hello")
val d = id(65.0)

// infix op notation
d compare 18.0
d + 1.1

// ** Invoking a func with an exp block **
def formatEuro(amt: Double) = f"-> $amt%.2f"

formatEuro(3.1234)
formatEuro { val rate = 1.32; 0.235 + 0.7123 + rate * 5.32 }

// ** recursive
def power(x: Int, n: Int): Long = {
  if (n >= 1)
    x * power(x, n-1)
  else 1
}
power(2, 10)

@annotation.tailrec
def power2(x: Int, n: Int, t: Int = 1): Int = {
  if (n < 1) t
  else power2(x, n-1, x*t)
}

// nested
def max(a: Int, b: Int, c: Int) = {
  def max(x: Int, y: Int) = if (x > y) x else y
  max(a, max(b, c))
}

// varargs
def sum(items: Int*): Int = {
  var total = 0
  println(items.getClass)
  for (i <- items) total += i
  total
}
sum(1, 2, 3)