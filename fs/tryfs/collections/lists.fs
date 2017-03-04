// map
let addFsExt = List.map (fun s -> s + ".fs")

let files = addFsExt ["list"; "seq"; "set"]

// predicates: exists; forall; tryFind; filter
let exists = List.exists (fun s -> String.length s > 2) ["R"; "Python"; "F#"]
let odds = List.filter (fun i -> i % 2 = 1) [1..5]
let firstOdd = List.tryFind (fun i -> i % 2 = 1) [2..7]
let firstOdd2 = List.tryFind (fun i -> i % 2 = 1) [2..2]

let isMember x xs = List.exists (fun elem -> elem = x) xs

// fold: fun (acc, element) -> acc -> list
let sum = List.fold (fun acc i -> acc + i) 0 [1..100]
let sum2 = List.fold (+) 0 [1..100]

let rev xs = List.fold (fun rs x -> x::rs) [] xs
let reversed = rev [1..5]

// foldBack
let append ys zs = List.foldBack (fun x xs -> x::xs) ys zs
let appended = append [1..3] [4..6]
