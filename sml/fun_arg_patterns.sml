fun full_name {first=x, middle=y, last=z} =
	x ^ " " ^ y ^ " " ^ z

(* every fun in ML takes exactly one arg *)
fun sum_triple (x, y, z) =
	x + y + z

val ans1 = full_name({first="Anders", middle="", last="Cui"});
val ans2 = sum_triple(1, 2, 3);