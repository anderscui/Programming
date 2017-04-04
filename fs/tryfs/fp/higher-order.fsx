let add x y = x + y
let add1 = add 1
let add2 = add 2

// composition
let add3 = add1 >> add2

printfn "3 + 7 = %i" (add3 7)

// list of funcs
let add6 = [add1; add2; add3] |> List.reduce (>>)