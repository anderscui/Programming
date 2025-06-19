(* approximate value of PI using the Monte-Carlo method. *)
let n_points = read_int ()

let () =
  (* introduce a `local variable` *)
  let p = ref 0 in
  for _ = 1 to n_points do
    let x = Random.float 1.0 in
    let y = Random.float 1.0 in
    if x *. x +. y *. y <= 1.0 then
      p := !p + 1
  done;
  let pi = 4.0 *. float !p /. float n_points in
  Printf.printf "%f\n" pi;

  let pi = 4. *. atan 1. in
  Printf.printf "use atan func: %f\n" pi
