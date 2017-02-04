val x = ref 42
val y = ref 42
val z = x

(* z is also changed. *)
val _ = x := 43
val w = (!y) + (!z);
