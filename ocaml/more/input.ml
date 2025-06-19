type input = {
  pos_in: unit -> int;
  seek_in: int -> unit;
  input_char: unit -> char;
  in_channel_length: int
}

let input_of_channel ch = {
  pos_in = (fun () -> pos_in ch);
  seek_in = seek_in ch;
  input_char = (fun () -> input_char ch);
  in_channel_length = in_channel_length ch
}

let input_of_string s =
  let pos = ref 0 in
    {pos_in = (fun () -> !pos);
     seek_in = (fun p -> 
                  if p < 0 then raise (Invalid_argument "seek before beginning");
                  pos := p);
     input_char=
       (fun () ->
         if !pos > String.length s - 1
           then raise End_of_file
           else (let c = s.[!pos] in pos := !pos + 1; c));
     in_channel_length = String.length s}

let input_of_char_array ca =
  let pos = ref 0 in
    {pos_in = (fun () -> !pos);
     seek_in = (fun p -> 
                  if p < 0 then raise (Invalid_argument "seek before beginning");
                  pos := p);
     input_char=
       (fun () ->
         if !pos > Array.length ca - 1
           then raise End_of_file
           else (let c = Array.get ca !pos in pos := !pos + 1; c));
     in_channel_length = Array.length ca} 

let rewind i =
  i.seek_in (i.pos_in () - 1)

let is_non_letter x =
  match x with
  | ' ' | '!' | '(' | ')' | '.' | ',' | ';' | ':' -> true
  | _ -> false

let rec skip_chars i = 
  if is_non_letter (i.input_char ())
    then skip_chars i
    else rewind i

let rec collect_chars b i =
  match 
    try Some (i.input_char ()) with End_of_file -> None
  with
  | None -> Buffer.contents b
  | Some c ->
    if is_non_letter c
      then Buffer.contents b
      else (Buffer.add_char b c; collect_chars b i)

let read_word i =
  try
    skip_chars i;
    Some (collect_chars (Buffer.create 20) i)
  with
    End_of_file -> None

let rec read_words_inner i a =
  match read_word i with
  | None -> List.rev (List.map String.lowercase_ascii a)
  | Some w -> read_words_inner i (w :: a)

let read_words i =
  read_words_inner i []

let words = read_words (input_of_string "There are four of them; more than before.")
let () = List.iter (fun item -> print_string item; print_newline ()) words

let words = read_words (input_of_string ".")
let () = assert (words = [])

(* read words from a char array *)
let words = read_words (input_of_char_array [| 'f'; 'a'; 'l'; 'l'; ' '; 'i'; 'n'; ' '; 'l'; 'o'; 'v'; 'e' |])
let () = assert (words = ["fall"; "in"; "love"])

(* more input examples *)
let rec input_string i n =
  if n > 0
  then
    match try Some (i.input_char ()) with End_of_file -> None
    with 
    | None -> ""
    | Some c ->
      (String.make 1 c) ^ input_string i (n-1)
  else ""

let sample_input = (input_of_string "There are four of them; more than before.")
let sent = input_string sample_input 5
let () = assert (sent = "There")

let sent = input_string sample_input 10
let () = assert (sent = " are four ")

let rec input_string2 i n =
  let b = Buffer.create 100 in
    try
      for x = 0 to n - 1 do
        Buffer.add_char b (i.input_char ())
      done;
      Buffer.contents b
    with
      End_of_file -> Buffer.contents b

let sample_input = (input_of_string "There are four of them; more than before.")
let sent = input_string2 sample_input 5
let () = assert (sent = "There")

let sent = input_string2 sample_input 10
let () = assert (sent = " are four ")

(* for output interface *)
type output = {
  output_char: char -> unit;
  out_channel_length: unit -> int
}

let output_int_list o ls =
  o.output_char '[';
  List.iter
    (fun n ->
      String.iter o.output_char (string_of_int n);
      o.output_char ';';
      o.output_char ' ')
    ls;
  o.output_char ']'

let output_of_channel ch = {
  output_char = (fun c -> output_byte ch (int_of_char c));
  out_channel_length = (fun () -> out_channel_length ch)
}

(* let output_of_string s =
  let pos = ref 0 in {
    output_char = 
      (fun c ->
        if !pos < String.length s
        then (s.[!pos] <- c; pos := !pos + 1)
      else raise End_of_file);
    out_channel_length = (fun () -> String.length s)
  } *)

let output_of_bytes b =
  let pos = ref 0 in {
    output_char = 
      (fun c ->
        if !pos < Bytes.length b
        then (Bytes.set b !pos c; pos := !pos + 1)
        else raise End_of_file);
    out_channel_length = (fun () -> Bytes.length b)
  }

let output_example () =
  print_endline "\nUsing output_int_list:";
  output_int_list (output_of_channel stdout) [1; 2; 3];
  print_endline ""

let () = output_example ()
