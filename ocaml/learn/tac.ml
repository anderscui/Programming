let lines = ref []

let () =
  try
    while true do
      lines := read_line () :: !lines
    done
  with End_of_file ->
    ()

let rec print l =
  match l with
  | [] -> ()
  | h :: t -> print_endline h; print t

let () = print !lines

(* the above 5 lines could be replaced with *)
(* let () = List.iter print_endline !lines *)

let rec length = function
| [] -> 0
| _ :: t -> 1 + length t

let () = Printf.printf "%d lines read\n" (length !lines)
