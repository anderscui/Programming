(* text statistics *)
type stats = int * int * int * int

(* utility functions to retrieve parts of a stats value *)
let lines (l, _, _, _) = l

let characters (_, c, _, _) = c

let words (_, _, w, _) = w

let sentences (_, _, _, s) = s

let stats_from_channel ch_in = 
  let lines = ref 0 in
  let chars = ref 0 in
  let words = ref 0 in
  let sents = ref 0 in
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
            line
      done;
      (0, 0, 0, 0) (* just to make the type agree *)
    with
      End_of_file -> (!lines, !chars, !words, !sents)

let stats_from_file filename = 
  let channel = open_in filename in
    let result = stats_from_channel channel in
      close_in channel;
      result

