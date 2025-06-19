type point = float * float
type shape = 
  | Point of point
  | Circle of point * float (* center and radius *)
  | Rect of point * point (* lower-left and upper-right *)

let area = function
  | Point _ -> 0.0
  | Circle (_, r) -> Float.pi *. (r ** 2.0)
  | Rect ((x1, y1), (x2, y2)) -> 
    let width = x2 -. x2 in
    let height = y2 -. y1 in
    width *. height

let center = function
  | Point p -> p
  | Circle (c, _) -> c
  | Rect ((x1, y1), (x2, y2)) -> 
    ((x1 +. x2) /. 2., (y1 +. y2) /. 2.)

type string_or_int =
  | String of string
  | Int of int

type string_or_int_list = string_or_int list

let rec sum: string_or_int list -> int = function
  | [] -> 0
  | String s :: t -> int_of_string s + sum t
  | Int i :: t -> i + sum t

let () = assert (sum [String "1"; Int 2] = 3)

type intlist = Nil | Cons of int * intlist

let lst3 = Cons (3, Nil)
let lst123 = Cons (1, Cons (2, Cons (3, Nil)))

let rec sum (l: intlist) = 
  match l with
  | Nil -> 0
  | Cons (h, t) -> h + sum t

type 'a mylist = Nil | Cons of 'a * 'a mylist

let lst3 = Cons (3, Nil)
let lst_hi = Cons ("hi", Nil)

let empty = function
  | Nil -> true
  | Cons _ -> false

(* polymorphic variants *)
let f = function
  | 0 -> `Infinity
  | 1 -> `Finite 1
  | n -> `Finite (-n)

