// "each of" type
// declare a constructor
type Shape = 
  | Circle of float
  | Square of float
  | Triangle of float * float * float
  
let c = Circle 1.1

// ordering
let ans1 = Circle 1.0 < Circle 1.1
let ans2 = Circle 5.0 < Square 1.0

// patterns
let isShape = function
  | Circle r -> r > 0.0
  | Square a -> a > 0.0
  | Triangle(a, b, c) -> 
      a > 0.0 && b > 0.0 && c > 0.0
      && a < b + c && b < c + a && c < a + b
      
let area x =
  if not (isShape x)
  then failwith "not a legal shape"
  else match x with
       | Circle r -> System.Math.PI * r * r
       | Square a -> a * a
       | Triangle(a, b, c) -> 
           let s = (a+b+c)/2.0
           sqrt(s*(s-a)*(s-b)*(s-c))