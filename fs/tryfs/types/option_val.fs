let rec factorial = function
  | 0 -> Some 1
  | n when n > 0 -> Some(n * Option.get(factorial(n-1)))
  | _ -> None

