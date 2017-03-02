let rec gcd = function
  | (0, n) -> n
  | (m, n) -> gcd(n % m, m)

let ans1 = gcd(12, 27)
let ans2 = gcd(36, 116)