val p = (2, 3);

fun f (x, y) =
    x + y

val ans1 = f p;

val first = #1 p;
val ans2 = f {1=2, 2=3};
