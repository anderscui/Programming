fun compose(f, g) = fn x => f(g x)

val sqrt = Math.sqrt o Real.fromInt o abs

infix |>

fun x |> f = f x

fun sqrt2 i = i |> abs |> Real.fromInt |> Math.sqrt

fun backup1 (f, g) = fn x => case f x of
								NONE => g x
								| SOME y => y

fun backup2 (f, g) = fn x => f x handle _ => g x

val ans1 = sqrt 9;
val ans2 = sqrt 5;
val ans3 = sqrt2 5;