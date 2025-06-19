let is_nil = function
  | [] -> true
  | _ -> false

let rec length lst =
  match lst with
  | [] -> 0
  | _ :: t -> 1 + length t

let rec length_inner lst n =
  match lst with
  | [] -> n
  | _ :: t -> length_inner t (n+1)

let length lst = length_inner lst 0

let rec odd_elements lst =
  match lst with
  | a :: _ :: t -> a :: odd_elements t
  | _ -> lst

let () = assert (odd_elements [1;2;3] = [1;3])

let rec even_elements lst =
  match lst with
  | _ :: a :: t -> a :: even_elements t
  | _ -> []

let () = assert (even_elements [1] = [])
let () = assert (even_elements [1;2] = [2])
let () = assert (even_elements [1;2;3] = [2])
let () = assert (even_elements [1;2;3;4;5] = [2;4])

let rec append a b =
  match a with
  | [] -> b
  | h :: t -> h :: append t b

let rec rev lst =
  match lst with
  | [] -> []
  | h :: t -> rev t @ [h]

let () = assert (rev [1;2;3] = [3;2;1])
let () = assert (rev [1;2;3] = List.rev [1;2;3])

let rec take lst n =
  if n = 0 then [] else 
    match lst with
      | [] -> []
      | h :: t -> h :: take t (n-1)

let () = assert (take [1;2;3] 0 = [])
let () = assert (take [1;2;3] 1 = [1])
let () = assert (take [1;2;3] 3 = [1;2;3])
let () = assert (take [1;2;3] 100 = [1;2;3])
  
let rec drop lst n =
  if n = 0 then lst else
    match lst with
      | [] -> lst
      | h :: t -> drop t (n-1)

let () = assert (drop [1;2;3] 0 = [1;2;3])
let () = assert (drop [1;2;3] 1 = [2;3])
let () = assert (drop [1;2;3] 3 = [])
let () = assert (drop [1;2;3] 100 = [])

let rec count_true lst =
  match lst with
  | [] -> 0
  | true :: t -> 1 + count_true t
  | false :: t -> count_true t

let rec droplast lst =
  match lst with
  | [] -> []
  | [_] -> []
  | h :: t -> h :: droplast t
