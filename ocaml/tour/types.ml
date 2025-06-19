type color = 
  Red | Green | Blue
  | Yellow
  | RGB of int * int * int

let col = Blue
let cols = [Red; Green; Blue; Yellow; RGB (0, 128, 128)]
let cpair = ('R', Red)

let components c =
  match c with
  | Red -> (255, 0, 0)
  | Green -> (0, 255, 0)
  | Blue -> (0, 0, 255)
  | Yellow -> (255, 255, 0)
  | RGB (r, g, b) -> (r, g, b)

type 'a option = None | Some of 'a

let nothing = None
let number = Some 11
let numbers = [Some 12; None; Some 2]
let word = Some ['c'; 'a'; 'k'; 'e']

(* a seq type similar to built-in list *)
type 'a sequence = Nil | Cons of 'a * 'a sequence

type expr =
  | Num of int
  | Add of expr * expr
  | Substract of expr * expr
  | Multiply of expr * expr
  | Divide of expr * expr
  | Power of expr * expr

(* 1 + 2 * 3 *)
let e = Add (Num 1, Multiply (Num 2, Num 3))

let rec apply f arg times =
  if times = 1 then f arg
  else f (apply f arg (times - 1))

let power a b = apply (fun x -> x * a) 1 b

let rec evaluate e =
  match e with
  | Num x -> x
  | Add (x, y) -> evaluate x + evaluate y
  | Substract (x, y) -> evaluate x - evaluate y
  | Multiply (x, y) -> evaluate x * evaluate y
  | Divide (x, y) -> evaluate x / evaluate y
  | Power (x, y) -> power (evaluate x) (evaluate y)

let () = assert (evaluate e = 7)

let evaluate_opt e =
  try Some (evaluate e) with
  | Division_by_zero -> None

type rect = 
  | Square of int
  | Rectangle of int * int

let s = Square 5
let r = Rectangle (3, 4)

let rect_area r =
  match r with
  | Square s -> s * s
  | Rectangle (w, h) -> w * h
 
let () = assert (rect_area s = 25)
let () = assert (rect_area r = 12)

let rotate_rect r =
  match r with
  | Square _ -> r
  | Rectangle (w, h) -> if w > h then Rectangle (h, w) else r

let width_of_rect r =
  match r with
  | Square s -> s
  | Rectangle (w, _) -> w

let rect_compare a b =
  width_of_rect a - width_of_rect b

let pack rects =
  List.sort rect_compare (List.map rotate_rect rects)

let rects = [Square 6; Rectangle (4, 3); Rectangle (5, 6); Square 2]
let expected = [Square 2; Rectangle (3, 4); Rectangle (5, 6); Square 6]
let () = assert (pack rects = expected)
