type Equation = float * float * float
type Solution = float * float

exception Solve

let solve (a, b, c) =
  let d = b*b-4.0*a*c
  //if d < 0.0 || a = 0.0 then raise Solve
  if d < 0.0 || a = 0.0 then failwith "discriminant is negative or a = 0.0"
  else ((-b + sqrt(d))/(2.0*a),
        (-b - sqrt(d))/(2.0*a))
        
//let ans1 = solve(1.0, 0.0, 1.0)
let ans2 = solve(1.0, 1.0, -2.0)