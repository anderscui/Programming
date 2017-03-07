type BinaryTree<'a, 'b> =
  | Leaf of 'a
  | Node of BinaryTree<'a, 'b> * 'b * BinaryTree<'a, 'b>

let rec depth = function
  | Leaf _ -> 0
  | Node (t1, _, t2) -> 1 + max (depth t1) (depth t2)

let t1 = Node (Node (Leaf 1, "cd", Leaf 2), "ab", Leaf 3)
let t2 = Node (Leaf 1, "cd", Leaf 2)

let d1 = depth t1
