let check_number value = 
  match value with
  | v when v < 0 -> printfn "%i is negative" v
  | v when v > 0 -> printfn "%i is positive" v
  | _ -> printfn "zero"

// pattern-matching function
// PMF is just a shortcut for lambda exp.
let test_op = function
  | Some(v) -> printfn "Some: %i" v
  | None -> printfn "None"

