type nat = Zero | Succ of nat

let is_zero = function
  | Zero -> true
  | _ -> false

let pred = function
  | Zero -> failwith "pred Zero is undefined"
  | Succ m -> m

let rec add n1 n2 =
  match n1 with
  | Zero -> n2
  | Succ pred_n1 -> add pred_n1 (Succ n2)

let rec int_of_nat = function
  | Zero -> 0
  | Succ pred -> 1 + int_of_nat pred

let rec nat_of_int = function
  | i when i = 0 -> Zero
  | i when i > 0 -> Succ (nat_of_int (i-1))
  | _ -> failwith "nat_of_int is undefined on negative ints"


let rec even = function Zero -> true | Succ m -> odd m
and odd = function Zero -> false | Succ m -> even m


let zero = Zero
let one = Succ zero
let two = Succ one
let three = Succ two
let four = Succ three
let five = Succ four

let () = assert (is_zero zero)
let () = assert (not (is_zero one))

let () = assert (pred one = zero)
let () = assert (pred three = two)

let () = assert (add zero one = one)
let () = assert (add two three = five)

let () = assert (int_of_nat two = 2)
let () = assert (nat_of_int 2 = two)

let () = assert (even zero)
let () = assert (not (even one))
let () = assert (even two)

let () = assert (odd one)
let () = assert (not (odd two))
let () = assert (odd three)
