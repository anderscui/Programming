fun fact n =
	let fun aux (n, acc) =
		if n = 0 then acc else aux(n-1, acc*n)
	in
		aux(n, 1)
	end

fun sum xs =
	let fun aux (lst, acc) =
		case lst of
			[] => acc
			| x :: xs' => aux(xs', acc+x)
	in
		aux(xs, 0)
	end

fun rev xs =
	let fun aux (lst, acc) =
		case lst of
			[] => acc
			| x :: xs' => aux(xs', x :: acc)
	in
		aux(xs, [])
	end

val ans1 = fact(5) = 120;
val ans2 = sum [1, 2, 3] = 6;
val ans3 = (rev [1, 2, 3]) = [3, 2, 1];

fun map f [] = []
  | map f (x::xs) = f(x) :: map f xs