let fst p = match p with (x, _) -> x
let snd p = match p with (_, y) -> y

let fst (x, _) = x
let snd (_, y) = y

let census = [(1, 4); (2, 2); (3, 2); (4, 3); (5, 1); (6, 2)]

let rec lookup x lst =
  match lst with
  | [] -> raise Not_found
  | (k, v) :: t -> if k = x then v else lookup x t

let () = assert (lookup 3 census = 2)

let v = try lookup 7 census with Not_found -> -1
let () = assert (v = -1)

let rec add k v d =
  match d with
  | [] -> [(k, v)]
  | (k1, v1) :: t -> 
    if k1 <> k 
      then (k1, v1) :: (add k v t)
      else (k, v) :: t

let census = add 7 10 census
let () = assert (lookup 7 census = 10)

let rec remove k d =
  match d with
  | [] -> []
  | (k', v') :: t ->
    if k' = k
      then t
      else (k', v') :: remove k t

let census = remove 4 (remove 7 census)
let () = assert (List.length census = 5)

let rec build_dict keys values =
  match (keys, values) with
  | [], [] -> []
  | [], _ | _, [] -> raise (Invalid_argument "build_dict")
  | k :: kt, v :: vt -> (k, v) :: build_dict kt vt
