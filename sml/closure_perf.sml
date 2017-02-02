fun filter (f, xs) =
	case xs of
		[] => []
		| x :: xs' => if f x
					  then x :: (filter(f, xs'))
					  else filter(f, xs')

fun short_than1(xs, s) =
	filter (fn x => String.size x < (print "!"; String.size s), xs)

fun short_than2(xs, s) =
	let 
		val i = (print "!"; String.size s)
	in
		filter (fn x => String.size x < i, xs)
	end

val ans1 = short_than1(["Python", "C", "R", "Java", "ML"], "C#");
val _ = print "\n";
val ans2 = short_than2(["Python", "C", "R", "Java", "ML"], "C#");
val _ = print "\n";
