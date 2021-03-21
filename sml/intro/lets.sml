let
    val x = 1
in
    x + 1
end;

fun factorial n =
    let
        fun fact n a = if n = 0 then a
                       else fact (n-1) (n*a)
    in
        fact n 1
    end;

