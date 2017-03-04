let rec sum_list = function
  | [] -> 0
  | x::xs -> x + sum_list xs
  
let ans1 = sum_list [1 .. 100]

let rec altsum = function
  | [] -> 0
  | [x] -> x
  | x1::x2::xs -> x1 - x2 + altsum xs
  
let ans2 = altsum [1; -2; 3]

// layered patterns
let rec succ_pairs = function
  | x1::(x2::_ as xs) -> (x1, x2) :: succ_pairs xs
  | _ -> []
  
// match on result of rec call
let rec sum_prod = function
  | [] -> (0, 1)
  | x::rest -> 
      let (rest_sum, rest_prod) = sum_prod rest
      (x+rest_sum, x*rest_prod)
      
let ans3 = sum_prod [1..5]

let rec mix = function
  | (x::xs, y::ys) -> x::y::(mix(xs, ys))
  | ([], []) -> []
  | _ -> failwith "mix: lengths are not equal"
  
let ans4 = mix([1..3], [4..6])