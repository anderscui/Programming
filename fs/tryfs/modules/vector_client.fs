#r @"vector.dll"

open MyLib.Vector

let a = make(1.0, -2.0)
let b = make(3.0, 4.0)
let c = 2.0 *. a -. b