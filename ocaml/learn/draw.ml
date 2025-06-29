open Graphics

let left = 0.
let right = 300.
let down = 0.
let up = 200.

let ball = 5
let paddle = 50
let thick = 8

let gray = rgb 220 220 220

let init () =
  let s = Printf.sprintf " %dx%d" (truncate right) (truncate up) in
  open_graph s;
  (* activates the double buffering mode *)
  auto_synchronize false

let clear () =
  set_color gray;
  (* erase the canvas *)
  fill_rect 0 0 (truncate right) (truncate up)

let get_paddle_pos () =
  (* ensure the paddle does not go outside the game window *)
  let x = fst (mouse_pos ()) in
  max 0 (min x (truncate right - paddle))

let game x y =
  (* x, y is the position of ball *)
  clear ();
  set_color black;
  fill_circle (truncate x) (truncate y) ball;
  let x = get_paddle_pos () in
  fill_rect x 0 paddle thick;
  synchronize ();
  x
