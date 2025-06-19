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

let rec insert lst x =
  match lst with
  | [] -> [x]
  | h :: t -> if x <= h 
              then x :: lst
              else h :: insert t x

let () = assert (insert [1; 1; 2; 3; 5; 9] 3 = [1; 1; 2; 3; 3; 5; 9])

(* insertion sort *)
let rec sort lst =
  match lst with
  | [] -> []
  | h :: t -> insert (sort t) h

let () = assert (sort [53; 9; 2; 6; 19] = [2; 6; 9; 19; 53])
let () = assert (sort ["world"; "hello"] = ["hello"; "world"])

let rec merge lst1 lst2 =
  match lst1, lst2 with
  | [], l -> l
  | l, [] -> l
  | h1 :: t1, h2 :: t2 ->
    if h1 <= h2
    then h1 :: merge t1 lst2
    else h2 :: merge lst1 t2

let () = assert (merge [9; 53] [2; 6; 19] = [2; 6; 9; 19; 53])

let rec merge_sort lst =
  match lst with
  | [] -> []
  | [x] -> [x]
  | _ ->
    let mid = List.length lst / 2 in
    let left = take lst mid in
      let right = drop lst mid in
        merge (merge_sort left) (merge_sort right)

let () = assert (merge_sort [53; 9; 2; 6; 19] = [2; 6; 9; 19; 53])

let rec sorted lst =
  match lst with
  | a :: b :: t -> a <= b && sorted (b :: t)
  | _ -> true

