fun swap_pair (pr: int * bool) =
	(#2 pr, #1 pr)

fun sum_pairs (pr1: int * int, pr2: int * int) =
	(#1 pr1) + (#2 pr1) + (#1 pr2) + (#2 pr2)

fun div_mod (x: int, y: int) =
	(x div y, x mod y)

fun sort_pair(pr: int * int) = 
	if (#1 pr) < (#2 pr)
	then pr
	else (#2 pr, #1 pr)

val x = swap_pair(1, true);
val s = sum_pairs((1, 2), (3, 4));
val dm = div_mod(7, 3);
val sp = sort_pair(3, 2);