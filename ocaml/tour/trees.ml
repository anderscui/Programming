(* Leaf: empty tree *)
type 'a tree =
  | Branch of 'a * 'a tree * 'a tree
  | Leaf

let t0 = Leaf
let t1 = Branch (1, Leaf, Leaf)
let t2 = Branch (2, Branch (1, Leaf, Leaf), Leaf)
let t3 = Branch (2, Branch (1, Leaf, Leaf), Branch (4, Leaf, Leaf))

let rec size t =
  match t with
  | Leaf -> 0
  | Branch (_, left, right) -> 1 + size left + size right

let () = assert (size t0 = 0)
let () = assert (size t1 = 1)
let () = assert (size t2 = 2)
let () = assert (size t3 = 3)

let rec contains t v =
  match t with 
  | Leaf -> false
  | Branch (v', left, right) -> v = v' || contains left v || contains right v

let () = assert (contains t3 1)
let () = assert (not (contains t3 3))

let rec max_depth t =
  match t with
  | Branch (_, l, r) -> 1 + (max (max_depth l) (max_depth r))
  | Leaf -> 0

let () = assert (max_depth t0 = 0)
let () = assert (max_depth t1 = 1)
let () = assert (max_depth t3 = 2)

let rec list_of_tree t =
  match t with
  | Branch (v, l, r) -> list_of_tree l @ [v] @ list_of_tree r
  | Leaf -> []

let () = assert (list_of_tree t0 = [])
let () = assert (list_of_tree t3 = [1; 2; 4])

let rec tree_map f t =
  match t with
  | Branch (v, l, r) -> Branch (f v, tree_map f l, tree_map f r)
  | Leaf -> Leaf

let d = Branch ((3, "three"), 
          Branch ((1, "one"), Leaf, Branch ((2, "two"), Leaf, Leaf)),
          Branch ((4, "four"), Leaf, Leaf))

let rec lookup t k =
  match t with
  | Leaf -> None
  | Branch ((k', v), l, r) ->
    if k = k' then Some v
    else if k < k' then lookup l k
    else lookup r k

let () = assert (lookup d 2 = Some "two")
let () = assert (lookup d 5 = None)

let rec insert t k v =
  match t with
  | Leaf -> Branch ((k, v), Leaf, Leaf)
  | Branch ((k', v'), l, r) -> 
    if k = k' then Branch ((k, v), l, r)
    else if k < k' then Branch ((k', v'), insert l k v, r)
    else Branch ((k', v'), l, insert r k v)

let () = assert (lookup d 0 = None)
let d2 = insert d 0 "zero"
let () = assert (lookup d2 0 = Some "zero")

let rec same_shape t1 t2 =
  match t1, t2 with
  | Leaf, Leaf -> true
  | Leaf, _ -> false
  | _, Leaf -> false
  | Branch (v1, l1, r1), Branch (v2, l2, r2) -> same_shape l1 l2 && same_shape r1 r2
