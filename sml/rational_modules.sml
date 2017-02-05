structure Rational1 = 
struct

	exception BadFrac

	datatype rational1 = Whole of int | Frac of int * int

	fun gcd (x, y) =
		if x = y
		then x
		else if x < y
			 then gcd(x, y-x)
			 else gcd(y, x)

	fun reduce r =
		case r of
			Whole _ => r
			| Frac(x, y) =>
				if x = 0
				then Whole 0
				else let val d = gcd(abs x, y)
					 in if d = y
					 	then Whole (x div y)
					 	else Frac (x div d, y div d)
					 end

	fun make_frac (x, y) =
		if y = 0
		then raise BadFrac
		else if y < 0
			 then reduce(Frac(~x, ~y))
			 else reduce(Frac(x, y))
	fun add (r1, r2) =
		case (r1, r2) of
			(Whole i, Whole j) => Whole (i+j)
			| (Whole i, Frac (j, k)) => Frac (k*i + j, k)
			| (Frac (j, k), Whole i) => Frac (k*i + j, k)
			| (Frac (a, b), Frac (c, d)) => Frac (a*d+b*c, b*d)
	fun toString r =
		case r of
			Whole i => Int.toString i
			| Frac (i, j) => (Int.toString i) ^ "/" ^ (Int.toString j)
end

val f1 = Rational1.make_frac(9, 6)
val fs1 = Rational1.toString(f1)
val f2 = Rational1.make_frac(3, 1)
