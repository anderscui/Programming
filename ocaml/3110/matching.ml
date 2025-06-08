let x =
  match not true with
  | true -> "nope"
  | false -> "yep"

let () = assert (x = "yep")

let y =
  match "foo" with
  | "bar" -> 0
  | _ -> 1

let () = assert (y = 1)

(* for list *)
let a =
  match [] with
  | [] -> "empty"
  | _ -> "not empty"

let () = assert (a = "empty")

let b = 
  match ["taylor"; "swift"] with
  | [] -> "folklore"
  | h :: t -> h

let () = assert (b = "taylor")

(* first of a triple *)
let fst3 t =
  match t with
  | (a, b, c) -> a

let () = assert (fst3 (1, 2, 3) = 1)
(* let () = assert (fst3 (1, 2) = 1) *)

let empty lst =
  match lst with
  | [] -> true
  | _ :: _ -> false

let () = assert (empty [] = true)
let () = assert (empty [1] = false)

let rec sum lst =
  match lst with
  | [] -> 0
  | h :: t -> h + sum t

let () = assert (sum [] = 0)
let () = assert (sum [1; 2; 3] = 6)

let rec length lst =
  match lst with
  | [] -> 0
  | _ :: t -> 1 + length t

let () = assert (length [] = 0)
let () = assert (length [1; 2; 3] = 3)

let rec append lst1 lst2 =
  match lst1 with
  | [] -> lst2
  | h :: t -> h :: append t lst2

let () = assert (append [] [] = [])
let () = assert (append [1] [] = [1])
let () = assert (append [] [1] = [1])
let () = assert (append [1] [2] = [1; 2])

let rec sum lst =
  match lst with
  | [] -> 0
  | h :: t -> h + sum t

let () = assert (sum [1; 2] = 3)

let rec sum = function
  | [] -> 0
  | h :: t -> h + sum t

let rec from i j l =
  if i > j then l else from i (j-1) (j :: l)

let ( -- ) i j = from i j []

let () = assert (0 -- 2  = [0; 1; 2])

let rec range i j l =
  if i >= j then l else range i (j-1) (j-1 :: l)

let ( -- ) i j = range i j []

let () = assert (0 -- 2  = [0; 1])
let () = assert (5 -- 10  = [5; 6; 7; 8; 9])
