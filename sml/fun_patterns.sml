datatype exp = 
	(* def constructors *)
	Constant of int 
	| Negate of exp
	| Add of exp * exp
	| Multiply of exp * exp

fun eval (Constant i) = i
	| eval (Negate e2) = ~ (eval e2)
	| eval (Add(e1, e2)) = (eval e1) + (eval e2)
	| eval (Multiply(e1, e2)) = (eval e1) * (eval e2)

fun append ([], ys) = ys
	| append (x :: xs', ys) = x :: append (xs', ys)

val exp1 = Add (Constant 19, Negate(Constant 4))
val ans1 = eval(exp1) = 15

val ans2 = append([1, 2, 3], [4, 5, 6])