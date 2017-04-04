// list comprehension
let squares = [for i in 1..10 do yield i*i]

let rec sieve = function
  | (p::xs) -> p :: [for x in xs do if x % p > 0 then yield x]
  | [] -> []

let primes = sieve [2..50]
printfn "%A" primes