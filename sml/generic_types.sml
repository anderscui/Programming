datatype 'a option = NONE | SOME of 'a
datatype 'a mylist = Empty | Cons of 'a * 'a mylist

datatype ('a, 'b) tree =
	Node of 'a * ('a, 'b) tree * ('a, 'b) tree
	| Leaf of 'b

fun sum xs =
	case xs of
		[] => 0
		| x :: xs' => x + sum xs'

fun append (xs, ys) =
	case xs of
		[] => ys
		| x :: xs' => x :: append(xs', ys)

val ans1 = sum [1, 2, 3];
val ans2 = append([1, 2, 3], [4, 5, 6]);