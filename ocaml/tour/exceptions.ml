let rec take lst n =
  match lst with
    | [] ->
      if n = 0 then [] else raise (Invalid_argument "take")
    | h :: t -> 
      if n < 0 then raise (Invalid_argument "take") else
        if n = 0 then [] else h :: take t (n-1)

let rec drop lst n =
  match lst with
    | [] ->
      if n = 0 then [] else raise (Invalid_argument "drop")
    | h :: t -> 
      if n < 0 then raise (Invalid_argument "drop") else
        if n = 0 then lst else drop t (n-1)

(* custom exceptions *)
exception Problem

let f x = if x <= 0 then raise Problem else 100 / x

(* exception handler *)
let safe_divide x y =
  try x / y with
    Division_by_zero -> 0

let rec last lst =
  match lst with
  | [] -> raise Not_found
  | [x] -> x
  | _ :: t -> last t

let rec smallest lst =
  match lst with
  | [] -> raise Not_found
  | [x] -> if x > 0 then x else raise Not_found
  | h :: t -> if h > 0 then min h (smallest t) else smallest t

let () = assert (smallest [5; 0; -1; 6; 2] = 2)
(* let () =
  let x = try smallest [] with
     *)

exception Complex

let rec sqrt_inner x n =
  if x * x > n then x - 1 else sqrt_inner (x+1) n

let sqrt n =
  if n < 0 then raise Complex else sqrt_inner 1 n

let () = assert (sqrt 0 = 0)
let () = assert (sqrt 1 = 1)
let () = assert (sqrt 2 = 1)
let () = assert (sqrt 8 = 2)
let () = assert (sqrt 10 = 3)

let safe_sqrt n =
  try sqrt n with Complex -> 0

let () = assert (safe_sqrt (-1) = 0)
