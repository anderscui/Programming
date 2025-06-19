type 'a tree =
  | Leaf
  | Node of 'a * 'a tree * 'a tree


(* the code below constructs this tree:
         4
       /   \
      2     5
     / \   / \
    1   3 6   7
*)
let t =
  Node (4,
    Node (2, 
      Node (1, Leaf, Leaf),
      Node (3, Leaf, Leaf)
    ),
    Node (5, 
      Node (6, Leaf, Leaf),
      Node (7, Leaf, Leaf)
    )
  )

let rec tree_size t =
  match t with
  | Leaf -> 0
  | Node (_, left, right) -> 1 + tree_size left + tree_size right

let () = assert (tree_size t = 7)

(* use records *)
type 'a tree = 
  | Leaf
  | Node of 'a node

and 'a node = {
  value: 'a;
  left: 'a tree;
  right: 'a tree
}

let t =
  Node { 
    value = 2;
    left = Node {value=1; left=Leaf; right=Leaf};
    right = Node {value=3; left=Leaf; right=Leaf}
  }

let rec mem x = function
  | Leaf -> false
  | Node {value; left; right} -> value = x || mem x left || mem x right

let () = assert (mem 1 t)
let () = assert (not (mem 6 t))

let rec preorder = function
  | Leaf -> []
  | Node {value; left; right} -> [value] @ preorder left @ preorder right

let () = assert (preorder t = [2; 1; 3])
