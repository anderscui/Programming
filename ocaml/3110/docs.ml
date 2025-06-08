(** [sum lst] is sum of the elements of [lst] *)
let rec sum lst =
  match lst with
  | [] -> 0
  | x :: xs -> x + sum xs

let _ = print_endline "Camels" in
let _ = print_endline "are" in
print_endline "bae"

let () = print_endline "Camels" in
let () = print_endline "are" in
print_endline "bae"

print_endline "Camels";
print_endline "are";
print_endline "bae"
