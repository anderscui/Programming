type BinaryTree<'a, 'b> =
  | Leaf of 'a
  | Node of BinaryTree<'a, 'b> * 'b * BinaryTree<'a, 'b>

let rec depth = function
  | Leaf _ -> 0
  | Node (t1, _, t2) -> 1 + max (depth t1) (depth t2)
  
let rec pre_order = function
  | Leaf _ -> []
  | Node(tl, x, tr) -> x :: (pre_order tl) @ (pre_order tr)

let rec in_order = function
  | Leaf _ -> []
  | Node(tl, x, tr) -> (in_order tl) @ [x] @ (pre_order tr)

let rec post_order = function
  | Leaf _ -> []
  | Node(tl, x, tr) -> (post_order tl) @ (post_order tr) @ [x]

let t1 = Node (Node (Leaf 1, "cd", Leaf 2), "ab", Leaf 3)
let t2 = Node (Leaf 1, "cd", Leaf 2)

let d1 = depth t1

let t3 = Node(Node(Leaf 0, -3, Leaf 0), 0, Node(Leaf 0, 2, Leaf 0))
let t4 = Node(t3, 5, Node(Leaf 0, 7, Leaf 0))
let ans1 = pre_order t4
let ans2 = in_order t4
let ans3 = post_order t4

let rec postFoldBack f t e = 
  match t with
  | Leaf _ -> e
  | Node(tl, x, tr) -> 
      let ex = f x e
      let er = postFoldBack f tr ex
      postFoldBack f tl er
      
let ans4 = postFoldBack (fun x y -> x + y) t4 0
