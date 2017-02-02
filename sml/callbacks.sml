val cbs : (int -> unit) list ref = ref []

fun onKeyEvent f = cbs := f :: (!cbs)

fun onEvent i =
	let fun loop fs =
		case fs of
			[] => ()
			| f :: fs' => (f i; loop fs')

	in
		loop (!cbs)
	end

(* use callbacks *)
val timesPressed = ref 0
val _ = onKeyEvent (fn _ =>
					timesPressed := (!timesPressed) + 1)

fun printIfPressed i =
	onKeyEvent (fn j =>
		if i = j
		then print ("you pressed " ^ Int.toString i ^ "\n")
		else ())

val _ = printIfPressed 4;
val _ = printIfPressed 11;
val _ = printIfPressed 23;
val _ = printIfPressed 4;

val _ = onEvent 11;
val _ = onEvent 23;
val _ = onEvent 12;
val _ = onEvent 4;
print(Int.toString (!timesPressed));


