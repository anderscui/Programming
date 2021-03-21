(* lists *)
fun length L =
    case L of nil => 0
    | (h::t) => 1 + length t;

fun zip x =
    case x of (h1::t1, h2::t2) =>
        (h1, h2) :: zip (t1, t2)
    | _ => nil

fun unzip x =
    case x of (h1, h2) :: t =>
        let val (L1, L2) = unzip t
        in (h1::L1, h2::L2)
        end
    | _ => (nil, nil)

(*fun first L =
    case L of [x] => x
    | (h :: t) => h


fun last L =
    case L of [x] => x
    | (h :: t) => last t*)


fun foldr f Z nil = Z
    | foldr f Z (h :: t) = f(h, foldr f Z t)

