let print_dict_entry (k, v) =
  print_int k; 
  print_newline (); 
  print_string v; 
  print_newline ()

let () = print_dict_entry (1, "a")

let rec print_dict d =
  match d with
  | [] -> ()
  | h :: t -> print_dict_entry h; print_dict t

let rec iter f l =
  match l with
  | [] -> ()
  | h :: t -> f h; iter f t

let print_dict d =
  iter print_dict_entry d

let d =[(1, "one"); (2, "two"); (3, "three")]
let () = print_dict d

let rec read_dict() =
  try
    let i = read_int () in
      if i = 0 then [] else
        let name = read_line () in 
          (i, name) :: read_dict ()
  with
    Failure "int_of_string" ->
      print_string "This is not a valid integer. Please try again.";
      print_newline ();
      read_dict()


let () = print_newline ()
(* let () = print_dict (read_dict ()) *)

let entry_to_channel ch (k, v) =
  output_string ch (string_of_int k);
  output_char ch '\n';
  output_string ch v;
  output_char ch '\n'

let dict_to_channel ch d =
  iter (entry_to_channel ch) d

let dict_to_file filename d =
  let ch = open_out filename in
    dict_to_channel ch d;
    close_out ch

let data_file = "dict.txt"
let () = dict_to_file data_file d

(* load from file *)
let entry_of_channel ch =
  let n = input_line ch in
    let name = input_line ch in
      (int_of_string n, name)

let rec dict_of_channel ch =
  try
    let e = entry_of_channel ch in
      e :: dict_of_channel ch
  with
    End_of_file -> []

let dict_of_file filename =
  let ch = open_in filename in
    let d = dict_of_channel ch in
      close_in ch;
      d

let () = print_dict (dict_of_file data_file)

(* let rec read_triple () =
  try
    let i = read_int () in
      let j = read_int () in
        let k = read_int () in
          (i, j, k)
  with
    Failure "int_of_string" ->
      print_string "This is not a valid integer. Please try again.";
      print_newline ();
      read_triple () *)

(* let () =
  let x, y, z = read_triple() in
  Printf.printf "(%d, %d, %d)" x y z;
  print_newline () *)

let rec range from_n to_n =
  if from_n >= to_n then []
  else from_n :: range (from_n+1) to_n

let () = assert (range 1 2 = [1])
let () = assert (range 1 6 = [1; 2; 3; 4; 5])

let write_table_channel ch n =
  iter
    (fun x ->
      iter
        (fun i ->
          output_string ch (string_of_int i);
          output_string ch "\t")
        (List.map (( * ) x) (range 1 (n+1)));
      output_string ch "\n")
      (range 1 (n+1))

let () = write_table_channel stdout 5

exception FileProblem

let times_table filename n =
  if n <= 0 then raise (Invalid_argument "times_table") else
    try
      let ch = open_out filename in
        write_table_channel ch n;
        close_out ch
    with
      _ -> raise FileProblem

let () = times_table "times_table_6.txt" 6
