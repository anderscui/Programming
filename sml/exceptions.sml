fun hd2 xs = 
	case xs of
		[] => raise List.Empty
		| x :: _ => x

exception MyUndesirableCondition
exception MyOtherException of int * int

fun mydiv (x, y) =
	if y = 0
	then raise MyUndesirableCondition
	else x div y

(* pass in an exception *)
fun maxlist (xs, ex) =
	case xs of 
		[] => raise ex
		| x :: [] => x
		| x :: xs' => Int.max(x, maxlist(xs', ex))

val ans1 = maxlist([1, 2, 3], MyUndesirableCondition)
val ans2 = maxlist([1, 2, 3], MyUndesirableCondition)
		   handle MyUndesirableCondition => 42
val ans3 = maxlist([], MyUndesirableCondition)
		   handle MyUndesirableCondition => 42