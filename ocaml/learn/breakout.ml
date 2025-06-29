let bounce (x, y) (vx, vy) xp =
  (* x, y: position of ball *)
  (* vx, vy: velocity of ball *)
  (* xp: position of paddle *)
  let vx = 
    if x <= Draw.left || x >= Draw.right then -. vx else vx in
  let vy =
    if y <= float Draw.thick && x >= xp &&
       x <= xp +. float Draw.paddle || y >= Draw.up
    then -. vy else vy
in
(vx, vy)

let new_position (x, y) (vx, vy) = x +. vx, y +. vy

let rec play (x, y) (vx, vy) =
  if y <= Draw.down then begin
    Printf.printf "Game over!\n";
    exit 0
  end;
  let xp = Draw.game x y in
  let vx, vy = bounce (x, y) (vx, vy) (float xp) in
  let x', y' = new_position (x, y) (vx, vy) in
  play (x', y') (vx, vy)

let () =
  (* print_int (Draw.ball); *)
  Draw.init ();
  let speed = 1. in
  let vx = speed *. Random.float 1. in
  let vy = speed *. Random.float 1. in
  play (Draw.right /. 2., float Draw.thick) (vx, vy)
