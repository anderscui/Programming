// declare a binding, immutable
let value = 1
// val value : int = 1

// equality
let equal = value = 2
// val equal : bool = false

// declare a fun
// use .NET Framework
(* Area of circle with radius r *)
/// Area of circle with radius r.
let circleArea r = System.Math.PI * r * r
// val circleArea : r:float -> float

// call a fun
let ca1 = circleArea 1.0
let ca2 = circleArea (2.0)
