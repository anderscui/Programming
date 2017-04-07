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

// empty parentheses
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



