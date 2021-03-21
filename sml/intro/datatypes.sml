datatype 'a tree =
    Empty
    | Node of 'a * 'a tree * 'a tree

(* Empty and Node are used as data constructors *)
val t1  = Empty;
val t2 = Node (1, Empty, Empty);
val t3 = Node ((fn x => x), Empty, Empty);

fun max (a, b) =
    if a > b then a else b

fun height t =
    case t of
        Empty => 0
        | Node (_, t1, t2) => 1 + max(height t1, height t2)

val h1 = height t1;
val h2 = height t2;

fun toPreOrder Empty = ""
    | toPreOrder (Node(s, lt, rt)) =
        s ^ "(" ^ toPreOrder lt ^ ")"
        ^ "(" ^ toPreOrder rt ^ ")"

val t1 = Node ("Anders", Node ("Bill", Empty, Empty), Node ("Candy", Empty, Empty));
val ts = toPreOrder t1;

