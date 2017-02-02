fun n_times (f, n, x) =
	if n = 0
	then x
	else f (n_times(f, n-1, x))

fun inc x = x + 1
fun double x = 2 * x

val ans1 = n_times(inc, 10, 0);
val ans2 = n_times(double, 5, 1);
val ans3 = n_times(tl, 2, [1, 2, 3, 4]);

fun add(n, x) = n_times(inc, n, x);
fun triple_n_times (n, x) =
	n_times(fn x => 3 * x, n, x)