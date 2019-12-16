import scala.collection.mutable.ArrayBuffer

def digits(n: Int) : Set[Int] = {
  if (n < 0)
    digits(-n)
  else if (n < 10) Set(n)
  else digits(n/10) + (n % 10)
}

val d1 = digits(12345)

///

// immutables
val v1 = Vector(1, 2, 3)
println(v1(2))
val v2 = 1 +: v1

// mutables
val numbers = ArrayBuffer(1, 2, 3)
numbers += 5

var numbers2 = Set(1, 2, 3)
numbers2 += 5
println(numbers2)

