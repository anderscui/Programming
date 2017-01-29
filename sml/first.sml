(* comment *)

val x = 34;
(* 34 is an exp, this is creating a var binding *)
(* static env: x : int *)
(* dynamic env: x -> 34 *)

val y = 17;

(* run this file in REPL *)
(* use "first.sml"; *)

val z = y - x;
val abs_of_z = if z < 0 then 0 - z else z;

(* Syntax *)
(* Semantics: what sth. means *)
(* Type-checking *)
(* Evaluation *)

(* Every kind of exp has
1. Syntax
2. Type-checking rules
3. Eval rules
*)

(* Values
All values are exps;
Not all exps are values;
*)
