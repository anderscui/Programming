signature MATH = 
sig

	val factorial : int -> int
	val pi : real
	val double : int -> int

end


structure MyMath :> MATH =
struct

	exception ValueOutOfRange

	fun factorial x =
		if x < 0
		then raise ValueOutOfRange
		else if x = 0
			 then 1
			 else x * factorial(x-1)

	val pi = Math.pi

	fun double y = y + y

end

val fact5 = MyMath.factorial 5
val two = MyMath.double 1
