let l1 = [1; 2; 3; 4; 5]
let l2 = 1 :: 2 :: 3 :: 4 :: 5 :: []
let l3 = [1] @ [2; 3; 4] @ [5]

let rec product = function
  | [] -> 1
  | h :: t -> h * product t

let () = assert (product [] = 1)
let () = assert (product [1] = 1)
let () = assert (product [1; 2] = 2)
let () = assert (product [3; 6; 9] = 162)

let rec concat = function
  | [] -> ""
  | h :: t -> h ^ concat t

let () = assert (concat [] = "")
let () = assert (concat ["a"] = "a")
let () = assert (concat ["a"; "b"; "c"] = "abc")

let fifth_elem lst =
  if List.length lst >= 5
  then List.nth lst 4
  else 0

let () = assert (fifth_elem [] = 0)
let () = assert (fifth_elem [1;2;3;4;5;6] = 5)

let sort_list_desc lst =
  List.rev (List.sort Stdlib.compare lst)

let () = assert (sort_list_desc [2; 1; 3] = [3;2;1])
let () = assert (sort_list_desc ["c";"a";"b"] = ["c";"b";"a"])

type student = {first_name: string; last_name: string; gpa: float}

let s1 = {first_name = "anders"; last_name = "cui"; gpa = 3.9}
let get_name s = 
  match s with
  | {first_name; last_name} -> first_name, last_name

let create_student fn ln gpa = 
  {first_name=fn; last_name=ln; gpa=gpa}

