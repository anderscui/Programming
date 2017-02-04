fun max (xs: int list) =
	if null xs
	then 0
	else if null (tl xs)
	then hd xs
	else
		let val tl_max = max(tl xs)
		in
			if hd xs > tl_max
			then hd xs
			else tl_max
		end

fun countup(from: int, to: int) =
	if from = to
	then to :: []
	else from :: countup(from+1, to)

fun countdown (from: int, to: int) =
	if from = to
	then to :: []
	else from :: countdown(from-1, to)

val up = countup(2, 6)
val down = countdown(6, 1)

val ans1 = max(countup(1, 10000))
val ans2 = max(countdown(10000, 1))