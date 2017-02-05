let f = fun r -> System.Math.PI * r * r

let daysOfMonth = function
	| 2 -> 28
	| 4|6|9|11 -> 30
	| _ -> 31

let d2 = daysOfMonth 2
let d12 = daysOfMonth 12