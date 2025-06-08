(* [fact n] is [n!] 
  Requires: [n >= 0]. *)
let rec fact n =
  if n <= 1 then 1 else n * fact (n - 1)

let () = assert (fact 0 = 1)
let () = assert (fact 1 = 1)
let () = assert (fact 2 = 2)
let () = assert (fact 3 = 6)
let () = assert (fact 4 = 24)
let () = assert (fact 5 = 120)

(** [pow x y] is [x] to the power of [y].
  Requires: [y >= 0]. *)
let rec pow x y =
  if y = 0 then 1
  else x * pow x (y - 1)

let () = assert (pow 2 0 = 1)
let () = assert (pow 2 1 = 2)
let () = assert (pow 2 3 = 8)


let rec even n = 
  n = 0 || odd (n - 1)
and odd n =
  n <> 0 && even (n - 1)

let () = assert (even 0)
let () = assert (even 2)

let () = assert (not (odd 0))
let () = assert (odd 1)
let () = assert (odd 3)

let inc x = x + 1
let inc2= fun x -> x + 1

let () = assert (inc 1 = 2)
let () = assert (inc2 1 = 2)

let inc x = x + 1
let square x = x * x

let () = assert (square (inc 5) = 36)
let () = assert (5 |> inc |> square = 36)

(* polymorphic fun *)
let id x = x

let () = assert (id 5 = 5)
let () = assert (id true = true)
let () = assert (id "hello" = "hello")

let id_int (x: int): int = x

let id_int': int -> int = id

let () = assert (id_int' 5 = 5)
(* let () = assert (id_int' true = true)   *)

let add ~first_num:x ~second_num:y = x + y

let () = assert (add ~first_num:2 ~second_num:3 = 5)

let add ~first_num ~second_num = first_num + second_num

let () = assert (add ~first_num:2 ~second_num:3 = 5)

let add ~first_num:(x: int) ~second_num:(y: int) = x + y
let () = assert (add ~first_num:2 ~second_num:3 = 5)

let f ?name:(arg1=8) arg2 = arg1 + arg2
let () = assert (f ~name:2 7 = 9)
let () = assert (f 7 = 15)        (* uses default value for arg1 *)

(* Partial application *)
let add x y = x + y
let addx x = fun y -> x + y

let add5 = addx 5
let () = assert (add5 3 = 8)

let add5' = add 5
let () = assert (add5' 3 = 8)

let ( ^ ) x y = max x y

let () = assert (2 ^ 3 = 3)

let rec count n =
  if n = 0 then 0
  else 1 + count (n - 1)

let () = assert (count 0 = 0)
let () = assert (count 1 = 1)
let () = assert (count 5 = 5)

let () = assert (count 1_000_000 = 1_000_000)
(* let () = assert (count 1_000_000_000 = 1_000_000_000) *)

let rec count_aux n acc =
  if n = 0 then acc
  else count_aux (n - 1) (1 + acc)
let count_tr n = count_aux n 0

let () = assert (count_tr 0 = 0)
let () = assert (count_tr 1 = 1)
let () = assert (count_tr 5 = 5)

let rec fact n =
  if n = 0 then 1
  else n * fact (n - 1)

let rec fact_aux n acc =
  if n = 0 then acc
  else fact_aux (n - 1) (n * acc)
  
let fact_tr n = fact_aux n 1

let () = assert (fact_tr 0 = 1)
let () = assert (fact_tr 1 = 1)
let () = assert (fact_tr 5 = 120)

let double x = 2 * x

let _ = assert (double 5 = 10)
let _ = assert (double 0 = 0)
let _ = assert (double (-1) = -2)

let cube x = x *. x *. x

let () = assert (cube 2.0 = 8.0)
let () = assert (cube 3.0 = 27.0)

let sign x = 
  if x > 0 then 1
  else if x < 0 then -1
  else 0

let () = assert (sign 2 = 1)
let () = assert (sign (-2) = -1)
let () = assert (sign 0 = 0)

let circle_area r = Float.pi *. r ** 2.

let close_enough a b =
  Float.abs (a -. b) < 1e-5

let () = assert (close_enough (circle_area 1.0) Float.pi)

let rms x y =
  Float.sqrt ((x ** 2. +. y ** 2.) /. 2.)

let () = assert (close_enough (rms 2.0 2.0) 2.0)
let () = assert (close_enough (rms 7.0 42.0) 30.10813)

let date d m =
  if m = "Jan" || m = "Mar" || m = "May" || m = "Jul" || m = "Aug" || m = "Oct" || m = "Dec" then 1 <= d && d <= 31
  else if m = "Apr" || m = "Jun" || m = "Sep" || m = "Nov" then 1 <= d && d <= 30
  else if m = "Feb" then 1 <= d && d <= 28
  else false

let () = assert (date 1 "Jan")
let () = assert (date 31 "Oct")
let () = assert (date 30 "Apr")
let () = assert (not (date 31 "Apr"))

let () = assert (date 28 "Feb")
let () = assert (not (date 29 "Feb")) 

let rec fib n =
  if n = 0 then 0
  else if n = 1 then 1
  else fib (n-1) + fib (n-2)

let () = assert (fib 1 = 1)
let () = assert (fib 2 = 1)
let () = assert (fib 3 = 2)
let () = assert (fib 4 = 3)
let () = assert (fib 5 = 5)
(* let _ = fib 50 *)

let rec fib_2 n pp p = 
  if n = 0 then pp
  else if n = 1 then p
  else fib_2 (n - 1) p (pp + p)

let fib_fast n = fib_2 n 0 1

let () = assert (fib_fast 0 = 0)
let () = assert (fib_fast 1 = 1)
let () = assert (fib_fast 2 = 1)
let () = assert (fib_fast 5 = 5)
let x = fib_fast 50
let _ = print_int x

let divide ~numerator ~denominator = numerator /. denominator
let () = assert (divide ~numerator:10.0 ~denominator:2.0 = 5.0)

let ( +/. ) x y = (x +. y) /. 2.0

let () = assert (1.0 +/. 2.0 = 1.5)
let () = assert (0. +/. 0. = 0.)

