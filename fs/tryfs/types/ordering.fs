// val ordTest : x:'a -> y:'a -> string when 'a : comparison
let ordTest x y =
  if x > y
  then "greater"
  else if x = y then "equal" else "less"
  
let ordTest2 x y = match compare x y with
                    | t when t > 0 -> "greater"
                    | 0 -> "equal"
                    | _ -> "less"

