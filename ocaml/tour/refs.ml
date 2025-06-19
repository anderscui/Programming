(* references *)
let x = ref 0

let swap a b =
  let t = !a in
    a := !b; b := t

(* ignore else part *)
(* let () = print_string (string_of_bool (0 = !x)) *)
let () = if !x = 0 then x := 1 else ()
let () = if !x = 0 then x := 2

let x = 1
let y = 2
let a = ref 0
let b = ref 1
let c = ref 2

(* use begin and end *)
let _ = if x = y then
  begin
    a := !a + 1;
    b := !b - 1
  end
else
  c := !c + 1

let () = for x = 1 to 5 do print_int x; print_string ", " done
let () = print_newline ()

let smallest_power2 x =
  let t = ref 1 in
    while !t < x do
      t := !t * 2
    done;
    !t

let () = assert (smallest_power2 37 = 64)

let print_histogram arr =
  print_string "char frequencies:\n";
  for i = 0 to 255 do
    if arr.(i) > 0 then
      begin
        print_string "for char '";
        print_char (char_of_int i);
        print_string "' (char number ";
        print_int i;
        print_string ") the count is ";
        print_int arr.(i);
        print_string ".\n"
      end
  done

let channel_stats ch_in =
  let lines = ref 0 in
  let chars = ref 0 in
  let words = ref 0 in
  let sents = ref 0 in
  let histogram = Array.make 256 0 in
    try
      while true do
        let line = input_line ch_in in
          lines := !lines + 1;
          chars := !chars + String.length line;
          String.iter
            (fun c -> 
              match c with
              | '.' | '?' | '!' -> sents := !sents + 1
              | ' ' -> words := !words + 1
              | _ -> ())
            line;
          String.iter
            (fun c ->
              let i = int_of_char c in
                histogram.(i) <- histogram.(i) + 1)
            line
      done
    with
      End_of_file ->
        print_string "There are ";
        print_int !lines;
        print_string " lines, making up ";
        print_int !chars;
        print_string " chars with ";
        print_int !words;
        print_string " words in ";
        print_int !sents;
        print_string " sentences.";
        print_newline ();
        print_histogram histogram

let file_stats filename =
  try
    let ch_in = open_in filename in
      channel_stats ch_in;
      close_in ch_in
  with
    _ -> raise (Failure "file_stats")

let () = file_stats "gregor.txt"
