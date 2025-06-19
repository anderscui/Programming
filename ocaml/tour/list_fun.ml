let rec take lst n =
  if n = 0 then [] else 
    match lst with
      | [] -> []
      | h :: t -> h :: take t (n-1)

let rec drop lst n =
  if n = 0 then lst else
    match lst with
      | [] -> lst
      | h :: t -> drop t (n-1)

let rec map lst f =
  match lst with
  | [] -> []
  | h :: t -> f(h) :: map t f

let () = assert (map [10; 20; 30] (fun x -> x / 2) = [5; 10; 15])
let () = assert (map [1; 2; 3] (fun x -> x mod 2 = 0) = [false; true; false])

let calm c = if c = '!' then '.' else c

let () = assert (map ['H'; 'e'; 'l'; 'p'; '!'] calm = ['H'; 'e'; 'l'; 'p'; '.'])

(* let greater a b = a >= b *)

let rec merge lst1 lst2 cmp =
  match lst1, lst2 with
  | [], l -> l
  | l, [] -> l
  | h1 :: t1, h2 :: t2 ->
    if cmp h1 h2
    then h1 :: merge t1 lst2 cmp
    else h2 :: merge lst1 t2 cmp

let rec merge_sort lst cmp =
  match lst with
  | [] -> []
  | [x] -> [x]
  | _ ->
    let mid = List.length lst / 2 in
    let left = take lst mid in
      let right = drop lst mid in
        merge (merge_sort left cmp) (merge_sort right cmp) cmp

let () = assert (merge_sort [5; 4; 6; 2; 1] (fun x y -> x <= y) = [1; 2; 4; 5; 6])
let () = assert (merge_sort [5; 4; 6; 2; 1] ( > ) = List.rev [1; 2; 4; 5; 6])

let rec apply f arg times =
  if times = 1 then f arg
  else f (apply f arg (times - 1))

let double x = x * 2
let () = assert (apply double 1 1 = 2)
let () = assert (apply double 1 2 = 4)
let () = assert (apply double 1 3 = 8)

let power a b = apply (fun x -> x * a) 1 b
let () = assert (power 2 5 = 32)

let rec filter lst pred =
  match lst with
  | [] -> []
  | h :: t -> if pred h then h :: filter t pred else filter t pred

let () = assert (filter [1; 3; 2; 6; 5] (fun x -> x mod 2 = 0) = [2; 6])
