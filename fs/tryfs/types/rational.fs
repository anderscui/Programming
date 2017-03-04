let rec gcd = function
  | (0, n) -> n
  | (m, n) -> gcd(n % m, m)

let reduce(p, q) =
  let sign = if p * q < 0 then -1 else 1
  let ap = abs p
  let aq = abs q
  let d = gcd(ap, aq)
  (sign * (ap/d), aq/d)
  
let makeQ = function
  | (_, 0) -> failwith "Division by zero"
  | pr -> reduce pr
  
let (.+.) (a, b) (c, d) = reduce(a*d + b*c, b*d)

let (.-.) (a, b) (c, d) = reduce(a*d - b*c, b*d)

let (.*.) (a, b) (c, d) = reduce(a*c, b*d)

let (./.) (a, b) (c, d) = (a, b) .*. makeQ(d, c)

let (.=.) (a, b) (c, d) = (a, b) = (c, d)

let toString(p: int, q: int) = (string p) + "/" + (string q)

let q1 = makeQ(2, -3)
let q2 = makeQ(5, 10)
let q3 = q1 .+. q2
toString(q1 .-. q3 ./. q2)