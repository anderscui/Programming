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

// multiple placeholders
def comb(x: Int, y: Int, f: (Int, Int) => Int) = f(x, y)
comb(3, 7, _ * _)

// ** currying
def factorOf(x: Int, y: Int) = y % x == 0
val multipleOf3 = factorOf(3, _: Int)
multipleOf3(15)

// method 2
def factor2(x: Int)(y: Int) = y % x == 0
val isEven = factor2(2) _

// by-name param
def doubles(x: => Int) = {
  println("Now doubling " + x)
  x * 2
}
doubles(5)
def f(i: Int) = { println(s"Hello from f($i)"); i }

doubles(f(8))





