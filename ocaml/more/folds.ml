let rec fold_left f a lst =
  match lst with
  | [] -> a
  | h :: t -> fold_left f (f a h) t

let rec fold_right f lst a =
  match lst with
  | [] -> a
  | h :: t -> f h (fold_right f t a)

let () = assert (fold_left ( + ) 1 [1; 2; 3] = 7)
let () = assert (fold_right ( + ) [1; 2; 3] 1 = 7)

let all lst = fold_left ( && ) true lst
let any lst = fold_left ( || ) false lst

let () = assert (all [true; true])
let () = assert (not (all [true; false]))

let () = assert (any [false; true; false])
let () = assert (not (any [false; false]))

(* a very interesting function of `fold` *)
let setify lst =
  fold_left (fun a e -> if List.mem e a then a else a @ [e]) [] lst

let () = assert (setify [2; 1; 2; 1; 3; 4; 5] = [2; 1; 3; 4; 5])

let append l1 l2 =
  fold_right (fun e a -> e :: a) l1 l2

let () = assert (append [1; 2] [3] = [1; 2; 3])

let split lst =
  fold_right (fun (x, y) (l1, l2) -> (x :: l1, y :: l2)) lst ([], [])

let () = assert (split [(1, "one"); (2, "two")] = ([1; 2], ["one"; "two"]))

(* folding over trees *)
type 'a tree =
  | Lf
  | Br of 'a * 'a tree * 'a tree

let rec fold_tree f e t =
  match t with
  | Lf -> e
  | Br (x, l, r) -> f x (fold_tree f e l) (fold_tree f e r)

let t = Br (1, Br (0, Lf, Lf), Br (6, Br (4, Lf, Lf), Lf))

let tree_size t = fold_tree (fun _ lv rv -> 1 + lv + rv) 0 t

let () = assert (tree_size t = 4)

let tree_sum t = fold_tree (fun v lv rv -> v + lv + rv) 0 t

let () = assert (tree_sum t = 11)

let tree_preorder t = fold_tree (fun v lv rv -> [v] @ lv @ rv) [] t
let tree_inorder t = fold_tree (fun v lv rv ->  lv @ [v] @ rv) [] t
let tree_postorder t = fold_tree (fun v lv rv -> lv @ rv @ [v]) [] t

let () = assert (tree_preorder t = [1; 0; 6; 4])
let () = assert (tree_inorder t = [0; 1; 4; 6])
let () = assert (tree_postorder t = [0; 4; 6; 1])

let deduct budget expenses =
  fold_left ( - ) budget expenses

let () = assert (deduct 100 [10; 11; 29] = 50)
let () = assert (deduct 100 [10; 11; 129] = -50)

let length lst = List.fold_left (fun a _ -> a + 1) 0 lst

let () = assert (length [] = 0)
let () = assert (length [1] = 1)
let () = assert (length [1; 2; 3] = 3)

let last_elem lst = 
  List.fold_right (fun a acc -> if acc = None then Some a else acc) lst None

let () = assert (last_elem [] = None)
let () = assert (last_elem [1] = Some 1)
let () = assert (last_elem [1; 2; 3] = Some 3)

let rec rev_list lst =
  match lst with
  | [] -> []
  | h :: t -> fold_left (fun acc e -> e :: acc) [] lst

let () = assert (rev_list [] = [])
let () = assert (rev_list [1] = [1])
let () = assert (rev_list [3; 2; 1] = [1; 2; 3])

let rec mem a lst =
  fold_left (fun acc e -> acc || e = a) false lst

let () = assert (mem 1 [3; 1; 2])
let () = assert (not (mem 5 [3; 1; 2]))
