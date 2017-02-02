(* fold left *)
(* separate concerns: fold and other functions *)
fun fold (f, acc, xs) =
	case xs of
		[] => acc
		| x :: xs' => fold(f, f(acc, x), xs')

fun f1 xs = fold ((fn (x, y) => x + y), 0, xs)

fun f2 xs = fold ((fn (x, y) => x andalso y >= 0), true, xs)

fun f3 (xs, lo, hi) =
	fold ((fn (x, y) => 
			x + (if y >= lo andalso y <= hi then 1 else 0)),
		  0, xs)

fun f4 (xs, s) =
	let
		val i = String.size s
	in
		fold ((fn (x, y) => x andalso String.size y < i), true, xs)
	end

val ans1 = f1 [1, 2, 3, 4];
val ans2 = f2 [1, 2, 3]
		   andalso f2 [~1, 0, 1];
val ans3 = f3 ([1, 2, 3, 4, 5, 6], 2, 5);
val ans4 = not (f4 (["Python", "OCaml", "Java", "SML", "C#", "C"], "Java"))
			andalso f4 (["Python", "OCaml", "Java", "SML", "C#", "C"], "Language");