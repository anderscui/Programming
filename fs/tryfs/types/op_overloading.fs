// val square : x:int -> int
let square x = x * x

// val squaref : x:float -> float
// by parameter
let squaref (x: float) = x * x

// or by result type
let squaref2 x : float = x * x

// or by exp type
let squaref3 x = x * x : float