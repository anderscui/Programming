type ml = OCaml | StandardML

let lang = OCaml

type my_num = PlusInfinity | MinusInfinity | Real of float

let n1 = Real (-3.14)

type counter = { mutable num: int}
let c = { num = 0 }
let () = c.num <- 1
