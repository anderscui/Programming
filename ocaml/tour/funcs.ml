let is_vowel c=
  c = 'a' || c = 'e' || c = 'i' || c = 'o' || c = 'u'

let () = assert (is_vowel 'o')
let () = assert (not (is_vowel 'c'))

let rec gcd a b = 
  if b = 0 then a else gcd b (a mod b)

let () =
  let a = 64000 in 
  let b = 3456 in
  let result = gcd a b in
  Printf.printf "gcd(%d, %d) = %d\n" a b result

let mul10 n = n * 10
let rec acc n = if n = 1 then 1 else n + acc (n-1)

let () = assert (acc 100 = 5050)
