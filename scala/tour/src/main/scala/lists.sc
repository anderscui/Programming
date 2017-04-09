val numbers = List(32, 95, 24, 21, 17)
val colors = List("red", "green", "blue")

println(s"I have ${colors.size} colors: $colors")

colors.head
colors.tail
colors(1)

// for loops
var total = 0; for (i <- numbers) { total += i }
total

// high-order
val sizes = colors.map(_.length)
val total2 = numbers.reduce(_ + _)
val total3 = numbers.reduce((a, b) => a + b)

// Set
val unique = Set(10, 20, 30, 10, 30)
val sum = unique.sum

// Map
val colorMap = Map("red" -> 0xFF0000, "green" -> 0xFF00, "blue" -> 0xFF)
val redRGB = colorMap("red")
val hasWhite = colorMap.contains("white")

for (pairs <- colorMap) { println(pairs) }

// traverse a list
val primes = List(2, 3, 5, 11, 13)
val i = primes

def visit(nums: List[Int]): Unit = {
  if (nums != Nil) {
    print(nums.head + ", ")
    visit(nums.tail)
  }
}
visit(primes)

// use cons
val nums = 1 :: 2 :: 3 :: Nil
val oddList = Nil.::(1)

// ops
val strs = List("apple", "to", "scala", "language")
strs sortBy (_.size)
strs slice (1, 3)
strs splitAt 2
strs partition (_(1) < 'o')
strs take 2

// right-end
List(1, 2) :+ 3 // for ::
List(1 to 5) takeRight 3 // ?

// ** Mapping lists
List("milk", "tea") map (_.toUpperCase)
List("milk,tea", "fruit,water") flatMap (_.split(','))
List(0, 1, 0, 1) collect { case 1 => "OK"}

// ** Reducing lists
nums
nums contains 2
nums exists (_ < 2)
nums forall (_ % 2 == 0)
// also startsWith
nums endsWith List(2, 3)
// also max, min, sum
nums.product

// impl recude
def reduceOp[A, B](l: List[A], start: B)(f: (B, A) => B): B = {
  var acc = start
  for (elem <- l)
    acc = f(acc, elem)
  acc
}

// fold, reduce, scan
List(4, 5, 6).scan(0)(_+_)

val included = List(46, 19, 92).foldLeft(false) { (a, i) =>
  if (a) a else (i == 19)
}

val answer = List(11.1, 12.2, 13.7).reduceLeft(_ + _)

// Converting collections
List(1, 2, 3).mkString(", ")
// toBuffer, toList, toMap, toSet, toString
Map("a" -> 1, "b" -> 2).toList


















