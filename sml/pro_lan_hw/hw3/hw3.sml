(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let 
	val r = g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here ****)
fun only_capitals (strs) =
	List.filter (fn s => Char.isUpper(String.sub(s, 0))) strs

fun longest_string1 (strs) =
	List.foldl (fn (s1, s2) => if String.size(s1) > String.size(s2) then s1 else s2) "" strs

fun longest_string2 (strs) =
	List.foldl (fn (s1, s2) => if String.size(s1) >= String.size(s2) then s1 else s2) "" strs

fun longest_string_helper f strs =
	List.foldl (fn (s1, s2) => if f(String.size(s1), String.size(s2)) then s1 else s2) "" strs

val longest_string3 = longest_string_helper (fn (i, j) => i > j)

val longest_string4 = longest_string_helper (fn (i, j) => i >= j)

val longest_capitalized = longest_string1 o only_capitals

fun rev_string (s) =
	String.implode(rev(String.explode(s)))

fun first_answer f lst =
	case lst of
		[] => raise NoAnswer
		| x :: rest => case f(x) of
					     NONE => first_answer f rest
					     | SOME v => v

fun all_answers f lst =
	let fun collect(acc, f, elems) =
			case elems of
				[] => acc
				| e :: rest => case f(e) of
								NONE => collect(acc, f, rest)
								| SOME v => collect(acc @ v, f, rest)
		val collected = collect([], f, lst)
	in
		if (null collected) andalso not(null lst)
		then NONE
		else SOME collected
	end

fun count_wildcards p =
	g (fn () => 1) (fn x => 0) p

fun count_wild_and_variable_lengths p =
	g (fn () => 1) (fn x => String.size(x)) p

fun count_some_var (s, p) =
	g (fn () => 0) (fn x => if x = s then 1 else 0) p

fun check_pat p =
	let fun collect_strs(acc, p) =
			case p of
				Variable s => acc @ [s]
				| TupleP ps => List.foldl (fn (p, a) => a @ collect_strs([], p)) acc ps
				| ConstructorP(_, p) => acc @ collect_strs([], p)
				| _ => acc
		val collected = collect_strs([], p)
		fun unique (strs: string list) =
			case strs of
				[] => true
				| s :: rest => not(List.exists (fn str => str = s) rest) andalso unique(rest)
	in
		unique(collected)
	end

fun match (v: valu, p: pattern) =
	case p of
		Wildcard => SOME []
		| Variable s => SOME [(s, v)]
		| UnitP => (case v of
					Unit => SOME []
					| _ => NONE)
		| ConstP i => (case v of
						Const j => if i = j then SOME [] else NONE
						| _ => NONE)
		| TupleP ps => (case v of
							Tuple vs => (if List.length(ps) = List.length(vs) 
										 then (all_answers match (ListPair.zip(vs, ps)))
										 else NONE)
							| _ => NONE)
		| ConstructorP (s1, p) => (case v of
								   Constructor (s2, v) => if s1 = s2 then match(v, p) else NONE
								   | _ => NONE)

fun first_match (v: valu, ps: pattern list) =
	SOME (first_answer (fn p => match(v, p)) ps)
	handle NoAnswer => NONE