fun power1 (m, n) =
    if m = 0 then 1
    else n * power1(m-1, n);

fun power2 m n =
    if m = 0 then 1
    else n * power2 (m-1) n;

val ans1 = power1(3, 2);
val ans2 = power2 3 2;

(* power2 can take only one parameter *)
val cube = power2 3;
val ans3 = cube 2;

(* fun as parameters *)
fun sum f n =
    if n = 1 then f 1
    else f n + sum f (n-1)

val sumOfCubes = sum cube;
val ans4 = sumOfCubes 3;

val sumOfSquares = sum (power2 2);
val ans5 = sumOfSquares 5;
