fun id x = x;

fun twice f x =
    f (f x)

fun inc x = x + 1

val ans1 = twice inc 1;

val f = fn x => twice twice x;
val ans2 = f (fn x => x + 1) 1;
