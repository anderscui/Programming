fun sum_list (xs: int list) =
	if null xs
	then 0
	else (hd xs) + sum_list(tl xs)

val s = sum_list([1, 2, 3])

fun countdown (x: int) =
	if x = 0
	then []
	else x :: countdown(x-1)

val cd = countdown(5);

fun append (xs: int list, ys: int list) =
	if null xs
	then ys
	else (hd xs) :: append((tl xs), ys)

val ap = append([1, 2, 3], [4, 5, 6])