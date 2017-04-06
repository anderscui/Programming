// if (<bool exp>) <exp>
if (47 % 3 > 0)
  println("Not a multiple of 3")

val x = 10; val y = 20
val max = if (x > y) x else y

// match exp
// <exp> match {
// case <pat match> => <exp>
// [case ...]
// }
val max2 = x > y match {
  case true => x
  case false => y
}

val status = 500
val msg = status match {
  case 200 => "OK"
  case 400 => {
    println("400 Error")
    "ERROR"
  }
  case 500 => {
    println("500 Error")
    "ERROR"
  }
}

// pattern alternative, wildcard
val day = "MON"
val kind = day match {
  case "SAT" | "SUN" => "weekend"
  case _ => "weekday"
}

// pattern guard
val resp: String = null
val resp_result = resp match {
  case s if s != null => println(s"Recieved '$s'")
  case s => println("Error! Received a null resp")
}

// type pattern
val i: Int = 123
val j: Any = i
j match {
  case x: String => s"'x'"
  case x: Int => s"${x}i"
  case _ => "other type"
}

// loops
// range
// <starting int> [to|until] <ending int> [by increment]
// for
// for (<id> <- <iter>) [yield] [<exp>]
for (x <- 1 to 7) yield { s"Day $x: " }

// guards or filters
val threes = for (i <- 1 to 20 if i % 3 == 0) yield i
val quotes = "Faith,Hope,,Charity"
for {
  t <- quotes.split(",")
  if t != null
  if t.length > 0
} println(t)

// nested
for {
  x <- 1 to 2
  y <- 1 to 3
} println(s"($x, $y)")

// value binding
val powersOf2 = for (i <- 0 to 8; pow = 1 << i) yield pow

// while
var x2 = 10; while (x2 > 0) x2 -= 1
println(x2)









