def inc(i: Int): Stream[Int] = Stream.cons(i, inc(i+1))

val s = inc(1)
val l = s.take(5).toList

// bouned stream
def to(head: Char, end: Char): Stream[Char] =
  if (head > end) {
    Stream.empty
  } else {
    head #:: to((head + 1).toChar, end)
  }

val hexChars = to('A', 'F').take(10).toList

def numsFrom(n: BigInt): Stream[BigInt] = n #:: numsFrom(n+1)

val tenOrMore = numsFrom(10)
tenOrMore.tail.tail

val squares = numsFrom(1).map(x => x * x)
squares.take(5).force
