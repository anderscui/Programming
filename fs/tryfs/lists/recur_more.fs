let rec member_of x = function
  | y::ys -> x = y || (member_of x ys)
  | [] -> false
  
let ans1 = member_of 3 [1..10]