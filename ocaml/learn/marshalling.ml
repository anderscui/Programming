let c = open_out "foo" in
  output_value c (1, 3.14, true);
  close_out c

let c = open_in "foo"
let v: int * float * bool = input_value c

