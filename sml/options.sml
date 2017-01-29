fun max1 (xs: int list) =
	if null xs
	then NONE
	else
		let val tl_max = max1(tl xs)
		in if isSome tl_max andalso (valOf tl_max) > (hd xs)
		   then tl_max
		   else SOME (hd xs)
		end

fun countup(from: int, to: int) =
	if from = to
	then to :: []
	else from :: countup(from+1, to)

fun countdown (from: int, to: int) =
	if from = to
	then to :: []
	else from :: countdown(from-1, to)

val ans1 = max1(countup(1, 10000))
val ans2 = max1(countdown(10000, 1))
val ans3 = max1([])