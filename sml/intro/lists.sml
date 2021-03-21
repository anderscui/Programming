use "commons.sml";

fun range n =
    let
        fun f n L = if n = 0 then L
                    else f (n-1) (n::L)
    in
        f n nil
    end;

fun reverseRange n =
    if n = 0 then nil
    else n :: reverseRange (n-1)

val l1 = range 3;
val l2 = reverseRange 3;

(* pattern matching *)
val l1 = nil;
case l1 of nil => 0 | (h::t) => h;

val l2 = [1, 2];
case l2 of nil => 0 | (h::t) => h;

val len1 = length l1;
val len2 = length l2;

val zipped = zip ([1, 2], [1, 2, 3]);
val (l1, l2) = unzip [(1, 3), (2, 4)];
(*val f1 = first [1, 2];*)

(* built-ins *)
val concated = [1] @ [2, 3];
val isNull = null nil;
val head = hd [1, 2];
val tail = tl [1];
val reversed = rev [1, 2, 3];
val mapped = map (fn x => x + 1) [1, 2];

(* high-order *)
val sumList = foldr (fn (h, R) => h + R) 0;
val sum1 = sumList [1, 2, 3];
