let base = int_of_string Sys.argv.(1)

let list_of_string s =
  let digits = ref [] in
  for i = 0 to String.length s - 1 do
    digits := s.[i] :: !digits
  done;
  !digits

let digit_of_char c =
  match c with
  | '0'..'9' -> Char.code c - Char.code '0'
  | 'A'..'Z' -> 10 + Char.code c - Char.code 'A'
  | c -> Printf.eprintf "invalid char %c\n" c;
  exit 1

let check_digit d =
  if d < 0 || d >= base then begin
    Printf.eprintf "invalid digit %d\n" d;
    exit 1
  end

let () =
  while true do
    let s = read_line () in
    let chars = list_of_string s in
    let digits = List.map digit_of_char chars in
    List.iter check_digit digits;
    let v = List.fold_right (fun d acc -> d + base * acc) digits 0 in
    Printf.printf " -> %d\n" v
  done
