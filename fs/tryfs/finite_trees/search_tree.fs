type BST<'a when 'a : comparison> =
  | Leaf
  | Node of BST<'a> * 'a * BST<'a>
  
let rec add x t =
  match t with
  | Leaf -> Node(Leaf, x, Leaf)
  | Node(tl, v, tr) when x < v -> Node(add x tl, v, tr)
  | Node(tl, v, tr) when x > v -> Node(tl, v, add x tr)
  | _ -> t
  
let rec contains x = function
  | Leaf -> false
  | Node(tl, v, _) when x < v -> contains x tl
  | Node(_, v, tr) when x > v -> contains x tr
  | _ -> true
  
let t = Node(Leaf, 0, Leaf)
let t1 = add 2 (add -3 t)
let t2 = Node(t1, 5, Node(Leaf, 7, Leaf))
let contains2 = contains 2 t2