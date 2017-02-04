(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)
fun all_except_option (str: string, lst: string list) =
	let fun contains (str, slist) =
			case slist of
				[] => false
				| s :: ss => same_string(s, str) orelse contains(str, ss)
		val contains_str = contains(str, lst)
	in if contains_str
	   then SOME (List.filter (fn s => not(same_string(s, str))) lst)
	   else NONE
	end

fun get_substitutions1 (substitutions: string list list, s: string) =
	case substitutions of
		[] => []
		| hd :: sl_tl =>
			case all_except_option(s, hd) of
			   	NONE => get_substitutions1(sl_tl, s)
				| SOME filtered => filtered @ get_substitutions1(sl_tl, s)

fun get_substitutions2 (substitutions: string list list, s: string) =
	let fun collect(acc, subs) =
			case subs of
				[] => acc
				| hd :: sl_tl =>
					case all_except_option(s, hd) of
					   	NONE => collect(acc, sl_tl)
						| SOME filtered => collect(acc @ filtered, sl_tl)
	in
		collect([], substitutions)
	end

fun similar_names (substitutions: string list list, name) =
	case name of
		{first=f, middle=m, last=l} => let val first_names = f :: get_substitutions1(substitutions, f)
									   in
									       List.map (fn fname => {first=fname, middle=m, last=l}) first_names
									   end

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
fun card_color (c: card) =
	case c of
		(Clubs, _) => Black
		| (Spades, _) => Black
		| _ => Red

fun card_value (c: card) =
	case c of
		(_, Num n) => n
		| (_, Ace) => 11
		| _ => 10

fun remove_card (cs: card list, c, e) =
	case cs of
		[] => raise e
		| c' :: cs' => if c = c' then cs' else c' :: remove_card(cs', c, e)

fun all_same_color (cs: card list) =
	case cs of
		[] => true
		| c :: [] => true
		| c1 :: c2 :: cs' => card_color(c1) = card_color(c2) andalso all_same_color(c2 :: cs')

fun sum_cards (cs: card list) =
	let fun sum (acc, cards) =
			case cards of
				[] => acc
				| c :: cs' => sum(acc + card_value(c), cs')
	in
		sum(0, cs)
	end

fun score (cs, goal) =
	let val sum = sum_cards(cs)
		val pre_score = if sum > goal then 3 * (sum - goal) else (goal - sum)
	in
		if all_same_color(cs) then pre_score div 2 else pre_score
	end

fun officiate (cs: card list, ms: move list, goal: int) =
	let fun play (helds, cards, moves) =
		let val sum = sum_cards(helds)
		in
			if sum > goal
			then score(helds, goal)
			else
				case moves of
					[] => score(helds, goal)
					| m :: ms => case m of
								 	Draw => (case cards of
								 		[] => score(helds, goal)
								 		| c :: rest => play(c::helds, rest, ms))
								 	| Discard dc => play(remove_card(helds, dc, IllegalMove), cards, moves)
		end
	in
		play([], cs, ms)
	end

val ans1 = all_except_option("str", []) = NONE
		   andalso all_except_option("str", ["test"]) = NONE
		   andalso valOf(all_except_option("str", ["test", "str"])) = ["test"]

val ans2_1 = get_substitutions1([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], "Fred") 
				= ["Fredrick","Freddie","F"]
val ans2_2 = get_substitutions1([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]], "Jeff") 
				= ["Jeffrey","Geoff","Jeffrey"]

val ans3_1 = get_substitutions2([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], "Fred")
				= ["Fredrick","Freddie","F"]
val ans3_2 = get_substitutions2([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]], "Jeff") 
				= ["Jeffrey","Geoff","Jeffrey"]

val ans4 = similar_names ([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], 
							{first="Fred", middle="W", last="Smith"}) 
				= [{first="Fred", last="Smith", middle="W"}, {first="Fredrick", last="Smith", middle="W"},
	     		   {first="Freddie", last="Smith", middle="W"}, {first="F", last="Smith", middle="W"}]

val ans5 = card_color (Clubs, Num 2) = Black
		   andalso card_color (Hearts, Num 2) = Red

val ans6 = card_value (Clubs, Num 2) = 2
		   andalso card_value (Spades, Ace) = 11
		   andalso card_value (Diamonds, Queen) = 10

val ans7 = remove_card ([(Hearts, Ace)], (Hearts, Ace), IllegalMove) = []

val ans8 = all_same_color [(Hearts, Ace), (Hearts, Ace)] = true

val ans9 = sum_cards [(Clubs, Num 2),(Clubs, Num 2)] = 4

val ans10 = score ([(Hearts, Num 2),(Clubs, Num 4)],10) = 4


val ans11 = officiate ([(Hearts, Num 2),(Clubs, Num 4)],[Draw], 15) = 6

val ans12 = officiate ([(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Ace)],
                        [Draw,Draw,Draw,Draw,Draw],
                        42)
             = 3

val ans13 = ((officiate([(Clubs,Jack),(Spades,Num(8))],
                         [Draw,Discard(Hearts,Jack)],
                         42);
               false) 
              handle IllegalMove => true)
