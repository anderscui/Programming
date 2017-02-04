datatype mytype = 
	TwoInts of int * int 
	| Str of string
	| Pizza

val a = Str "hi"
val b = Str
val c = Pizza
val d = TwoInts(3, 5)
val e = a

fun f (x: mytype) =
	case x of
		Pizza => 3
		| Str s => 8
		| TwoInts(i, j) => i + j

val ans1 = f(a)
val ans2 = f(c)
val ans3 = f(d)