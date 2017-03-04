// (+) is the non-fix op
let add = (+)

// currying
let inc = add 1
let three = inc 2

// partial; closure
let weight ro = fun s -> ro * s ** 3.0

let waterWeight = weight 1000.0
let methanolWeight = weight 786.5

let ans = methanolWeight 2.0

// better way
let weight2 ro s = ro * s ** 3.0