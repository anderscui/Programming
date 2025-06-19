open Graphics

(* let n = read_int () *)
let n = 4

let read_pair () =
  let x = read_int () in
  let y = read_int () in
  (x, y)

(* let data = Array.init n (fun i -> read_pair ()) *)
(* let data = [| (2, 2); (10, 15); (20, 15); (30, 10) |] *)
let data = [| (2, 2); (50, 60); (100, 60); (150, 100) |]

let compare (x1, y1) (x2, y2) = x1 - x2
let () = Array.sort compare data

let () = 
  open_graph " 200x200";
  set_line_width 3;
  let (x0, y0) = data.(0) in moveto x0 y0;
  for i = 1 to n-1 do
    let (x, y) = data.(i) in
    lineto x y
  done;
  ignore (read_key ())
