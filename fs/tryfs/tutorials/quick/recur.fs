#indent "off"

let rec factorial = function
	| 0 -> 1
	| n -> n * factorial(n-1)

let f5 = factorial 5