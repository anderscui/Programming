fun f n =
    if n = 0 then 1
    else n * f (n - 1)

fun fib n =
    if n = 0 then 1
    else if n = 1 then 1
    else fib (n-1) + fib (n-2)

(* tail recursive ver of f*)
fun fact (n, a) =
    if n = 0 then a else fact (n-1, n*a)

fun factorial n = fact (n, 1);

val ans1 = factorial 5;

(* recursion and efficiency *)
fun fastFib n =
    let fun G(n, a, b) =
        if n = 0 then a
        else if n = 1 then b
        else G(n-1, b, a+b)
    in
        G(n, 1, 1)
    end

val ans2 = fastFib(5);
