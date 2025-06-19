type point = float * float
type vector = float list
type matrix = float list list

let get_x = fun (x, _) -> x

let p1: point = (1., 2.)
let p2: float * float = (1., 3.)

let () = assert (get_x p1 = 1.)
let () = assert (get_x p2 = 1.)
