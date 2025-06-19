type point = {x: float; y: float}

let p = {x = 4.5; y = 6.0}

type point = {x: float; y: float; label: string}

type 'a point = {
  x: float;
  y: float;
  label: string;
  content: 'a
}

let make_point x y lbl c =
  {x=x; y=y; label=lbl; content=c}

let p = make_point 4.5 6.0 "P" [1; 3; 1]

(* simplify record def *)
let make_point x y label content =
  {x; y; label; content}

let string_of_point p =
  p.label 
  ^ " = ("
  ^ string_of_float p.x
  ^ ", "
  ^ string_of_float p.y
  ^ ")"

let () = assert (string_of_point p = "P = (4.5, 6.)")

(* let () =
  let s = string_of_point p in
  print_string s;
  print_newline () *)

(* use record syntax in patterns *)
(* 不需要显式写出所有 fields，有时也可以 _ 指代之 *)
let string_of_point {label = l; x = x; y = y} =
  l
  ^ " = ("
  ^ string_of_float x
  ^ ", "
  ^ string_of_float y
  ^ ")"

let () = assert (string_of_point p = "P = (4.5, 6.)")

(* 简化版的 patterns *)
let string_of_point {label; x; y; _} =
  label
  ^ " = ("
  ^ string_of_float x
  ^ ", "
  ^ string_of_float y
  ^ ")"

let () = assert (string_of_point p = "P = (4.5, 6.)")

(* copy a record *)
let relabel p l = {p with label = l}

(* shorthand *)
let relabel p label = {p with label}

let mirror p = {p with x = p.y; y = p.x}

(* mutable records *)
type 'a point = {
  x: float;
  y: float;
  label: string;
  mutable content: 'a
}

let p = {x = 4.5; y = 6.; label = "P"; content = [1; 3; 1]}
let () = p.content <- [1]

let x = ref 0
let () = assert (!x = 0)

let () =
  x.contents <- 1;
  assert (!x = 1)
