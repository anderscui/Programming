fun sorted_tuple (x, y, z) = z >= y andalso y >= x

val sorted3 = fn x => fn y => fn z => z >= y andalso y >= x

fun sorted3_better x y z = z >= y andalso y >= x

fun fold f acc xs =
	case xs of
		[] => acc
		| x :: xs' => fold f (f(acc, x)) xs'

val sum = fold (fn (x, y) => x + y) 0

fun range i j = if i > j then [] else i :: range (i+1) j

val countup1 = range 1;

fun exists pred xs =
	case xs of
		[] => false
		| x :: xs' => pred(x) orelse exists pred xs'

val has_even = exists (fn x => x mod 2 = 0)

val ans1 = sorted_tuple (1, 2, 3);
val ans2 = ((sorted3 1) 2) 3;
val ans3 = sorted3 1 2 3;
val ans4 = sorted3_better 1 2 3;
val ans5 = sum [1, 2, 3];
val ans6 = has_even [1, 3, 6];