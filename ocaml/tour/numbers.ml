type point = float * float

let make_vector (x1, y1) (x2, y2) =
  (x2 -. x1, y2 -. y1)

let vector_length (x, y) =
  sqrt (x *. x +. y *. y)

let offset_point (x, y) (px, py) =
  (px +. x, py +. y)

let scale_to_length l (x, y) =
  let cur_len = vector_length (x, y) in
    if cur_len = 0. then (x, y) else
      let factor = l /. cur_len in
        (x *. factor, y *. factor)

let v = (3., 4.)
let () = assert (vector_length v = 5.)

let v2 = scale_to_length 10. v
let () = assert (v2 = (6., 8.))

let round x =
  let c = ceil x in
    let f = floor x in
      if c -. x <= x -. f then c else f

let () = assert (round 2.0 = 2.0)
let () = assert (round 2.5 = 3.0)
let () = assert (round 2.499999 = 2.0)
let () = assert (round 0.0 = 0.0)
let () = assert (round (-1.0) = -1.0)
let () = assert (round (-1.5) = -1.0)
let () = assert (round (-1.50001) = -2.0)

let mid_point (x1, y1) (x2, y2) =
  ((x1 +. x2) /. 2., (y1 +. y2) /. 2.)

let rec parts_of_float x =
  if x < 0. then
    let a, b = parts_of_float (-. x) in
      (-.a, b)
  else
      (floor x, x -. floor x)

let () =
  let i, f = parts_of_float 1.1 in
  let i2, f2 = parts_of_float (-1.1) in
    Printf.printf "%f %f" i f;
    Printf.printf " %f %f" i2 f2;
    print_newline ()


