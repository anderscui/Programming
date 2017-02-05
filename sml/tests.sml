

val x = 1
val xv = let val x = 3 * x
		in x end

val zips = ListPair.zip ([1, 2], ["a", "b"])

val len = List.length [1, 2]

val exists = List.exists (fn s => s = "a") ["ab", "b"]

val charlist = String.implode(rev(String.explode("abc")))
val sum = foldl (fn (x, y) => x + y) 0 [1, 2, 3, 4]
val f = foldl

val sub = Char.isUpper(String.sub("Hello", 0))

val ss = List.filter (fn s => String.size(s) = 3) ["abc", "ab"]

val a = not (1 = 2);

val optval = SOME "str"

val ans1 = case optval of
	NONE => "NONE"
	| SOME s => s

val divs = 13 div 2;

val xs = [(4,19), (1,20), (74,75)]
val xsp = case xs of
		(a, b)::rest => 1
		| _ => 0

(*fun isnull xs = xs = []*)
fun isnull xs = ((fn z => false) (hd xs)) handle List.Empty => true
val ans2 = isnull [] andalso isnull ["a"]

signature COUNTER =
sig
    type t
    val newCounter : int -> int
    val increment : t -> t
    val first_larger : t * t -> bool
end

