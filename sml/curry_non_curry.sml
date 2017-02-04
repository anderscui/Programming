fun curry f x y = f (x, y)

fun uncurry f (x, y) = f x y

fun switch_args f x y = f y x

(* non-curried fun *)
fun range (i, j) = if i > j then [] else i :: range (i+1, j);

val countup = curry range 1;

val ans1 = range(1, 5);
val ans2 = countup(5);