let rec count_of_lines ch =
  try
    let _ = input_line ch in
      1 + count_of_lines ch
  with
    End_of_file -> 0

let count_of_lines_file filename =
  try
    let ch = open_in filename in
      let c = count_of_lines ch in
        close_in ch;
        c
  with
    _ -> raise (Failure "count_of_lines_file")

let () = assert (count_of_lines_file "times_table_6.txt" = 6)

let rec copy_channel ch_in ch_out =
  try
    let line_in = input_line ch_in in
      output_string ch_out line_in;
      output_string ch_out "\n";
      copy_channel ch_in ch_out
  with
    End_of_file -> ()

exception CopyFailed

let copy_file file_in file_out =
  try
    let ch_in = open_in file_in in
      let ch_out = open_out file_out in
        copy_channel ch_in ch_out;
        close_in ch_in;
        close_out ch_out
  with
    _ -> raise (Failure "copy_file")

let ok = copy_file "times_table_6.txt" "times_table_6_dup.txt"
