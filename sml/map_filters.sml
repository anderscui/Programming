fun filter (f, xs) =
	case xs of
		[] => []
		| x :: xs' => if f x
					  then x :: (filter(f, xs'))
					  else filter(f, xs')

fun is_even v = (v mod 2 = 0);
fun all_even xs =
	filter(is_even, xs)
fun all_even_snd xs =
	filter((fn (_, v) => is_even v), xs)

val ans1 = all_even [1, 2, 3, 4, 5];
val ans2 = all_even_snd [(1, 2), (2, 3), (3, 4), (4, 5)];