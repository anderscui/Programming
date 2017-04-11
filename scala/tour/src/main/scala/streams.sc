def inc(i: Int): Stream[Int] = Stream.cons(i, inc(i+1))

val s = inc(1)
val l = s.take(5).toList
s

// bouned stream
def to(head: Char, end: Char): Stream[Char] =
  (head > end) match {
    case true => Stream.empty
    case false => head #:: to((head+1).toChar, end)
  }

val hexChars = to('A', 'F').take(10).toList

