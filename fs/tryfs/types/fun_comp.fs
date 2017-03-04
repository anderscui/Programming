let f = fun y -> y + 3
let g = fun x -> x * x
let h = f << g // f o g

let ans1 = h 3