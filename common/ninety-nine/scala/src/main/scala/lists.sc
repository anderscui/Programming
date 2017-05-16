// See: http://aperiodic.net/phil/scala/s-99/

// P01
def last[A](list: List[A]): Option[A] = list match {
    case Nil => None
    case last :: Nil => Some(last)
    case _ :: rest => last(rest)
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

