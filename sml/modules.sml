structure MyMath = 
struct

exception ValueOutOfRange

fun factorial x =
	if x < 0
	then raise ValueOutOfRange
	else if x = 0
		 then 1
		 else x * factorial(x-1)

fun double y = y + y

end

val fact5 = MyMath.factorial 5
val two = MyMath.double 1