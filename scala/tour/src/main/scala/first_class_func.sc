def double(x: Int) = x * 2

// func as a value
val myDouble: (Int) => Int = double
val myDouble2 = double _

def max(x: Int, y: Int) = if (x > y) x else y
val maximize: (Int, Int) => Int = max

def hi() = "hi"
val start: () => String = hi

// higher-order
def safeStrOp(s: String, op: String => String) = {
  if (s != null) op(s) else s
}

// func literals (or anonymours func, lambda exp, lambdas)
safeStrOp("hello", s => s.toUpperCase)

// placeholder syntax
safeStrOp("one", _.reverse) // func type is defined outside






