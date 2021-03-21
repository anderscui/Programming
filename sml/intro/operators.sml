fun power (m, n) =
    if m = 0 then 1
    else n * power(m-1, n);

infix 8 power;

val ans1 = 2 power 3 + 10;

(*op power;*)
op power(2, 3);
