// declare a pair: float * int
let pair = (2.0, 3)

let rec power = function
  | (x, 0) -> 1.0
  | (x, n) -> x * power (x, n-1)

let ans1 = power(2.0, 5)
let ans2 = power pair // apply to a pair directly