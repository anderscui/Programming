fun curry f x y = f (x, y)

fun uncurry f (x, y) = f x y

fun switch_args f x y = f y x

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

val has_even = exists (fn x => x mod 2 = 0);

