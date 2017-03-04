// element are ordered (balanced binary tree)
let names = set ["Anders"; "Bill"; "Cindy"]

let nums = set [3; 1; 9; 5; 7; 9; 1] // Set<int> = set [1; 3; 5; 7; 9]

let names2 = Set.add "Donald" names
let containing = Set.contains "Anders" names
let issubset = Set.isSubset names names2

// minElement and recursion
let rec tryFind pred s =
  if Set.isEmpty s then None
  else
    let minElem = Set.minElement s
    if pred minElem then Some minElem 
    else tryFind pred (Set.remove minElem s)
    
let greaterThan5 = tryFind (fun x -> x > 5) nums