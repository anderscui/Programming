datatype exp = 
	(* def constructors *)
	Constant of int 
	| Negate of exp
	| Add of exp * exp
	| Multiply of exp * exp

fun eval e =
	case e of
		Constant i => i
		| Negate e2 => ~ (eval e2)
		| Add(e1, e2) => (eval e1) + (eval e2)
		| Multiply(e1, e2) => (eval e1) * (eval e2)

fun num_of_adds e =
	case e of
		Constant i => 0
		| Negate e2 => num_of_adds(e2)
		| Add(e1, e2) => 1+ (num_of_adds e1) + (num_of_adds e2)
		| Multiply(e1, e2) => (num_of_adds e1) * (num_of_adds e2)

fun max_const e =
	case e of
		Constant i => i
		| Negate e2 => max_const e2
		| Add(e1, e2) => Int.max(max_const e1, max_const e2)
		| Multiply(e1, e2) => Int.max(max_const e1, max_const e2)

val exp1 = Add (Constant 19, Negate(Constant 4))

val ans1 = eval(exp1) = 15
val ans2 = num_of_adds(exp1) = 1
val ans3 = max_const(exp1) = 19
