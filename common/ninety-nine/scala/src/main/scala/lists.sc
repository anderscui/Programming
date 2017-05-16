// See: http://aperiodic.net/phil/scala/s-99/

// P01
def last[A](list: List[A]): Option[A] = list match {
    case Nil => None
    case head :: Nil => Some(head)
    case _ :: tail => last(tail)
}

assert(last(List(1, 2, 3)) == Some(3))
assert(last(List(1)) == Some(1))
assert(last(List.empty).isEmpty)

// P02
def penultimate[A](list: List[A]): Option[A] = list match {
  case first :: _ :: Nil => Some(first)
  case _ :: second :: rest => penultimate(second :: rest)
  case _ => None
}

assert(penultimate(List(1, 2, 3)) == Some(2))
assert(penultimate(List(1, 2)) == Some(1))
assert(penultimate(List(1)).isEmpty)
assert(penultimate(List.empty).isEmpty)

def lastNth[A](list: List[A], n: Int): Option[A] = {
  def lastNthRecur(count: Int, resultList: List[A], curList: List[A]): Option[A] = {
    curList match {
      case Nil if count > 0 => None
      case Nil => Some(resultList.head)
      case _ :: tail =>
        lastNthRecur(count - 1,
          if (count > 0) resultList else resultList.tail,
          tail)
    }
  }
  lastNthRecur(n, list, list)
}

val fib = List(1, 1, 2, 3, 5, 8)
assert(lastNth(fib, 3) == Some(3))

// P03
def nth[A](list: List[A], n: Int): Option[A] = (n, list) match {
  case (0, head :: _) => Some(head)
  case (i, _ :: tail) => nth(tail, i-1)
  case _ => None
}

assert(nth(fib, 2) == Some(2))
assert(nth(fib, 10) == None)

// P04
def len[A](list: List[A]): Int = {
  // scala 'would' do tail-call for final or local func.
  def lenRecur(acc: Int, lst: List[A]): Int = lst match {
    case Nil => acc
    case _ :: tail => lenRecur(acc+1, tail)
  }
  lenRecur(0, list)
}

assert(len(fib) == 6)
assert(len(List.empty) == 0)

def len2[A](list: List[A]): Int = {
  list.foldLeft(0) { (acc, _) => acc + 1}
}

assert(len2(fib) == 6)
assert(len2(List.empty) == 0)
