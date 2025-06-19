type ptype = TNormal | TFire | TWater
type mon = {name: string; hp: int; ptype: ptype}

let r = {name = "Charmander"; hp = 39; ptype = TFire}

(* let _ = (print_string r.name) *)

let hp = 
  match r with
  | {name = n; hp = h; ptype = t} -> h
let () = assert (hp = r.hp)

let hp = 
  match r with
  | {name; ptype; hp;} -> hp
let () = assert (hp = r.hp)


let x = match (1, 2, 3) with
  | (x, y, z) -> x + y + z
let () = assert (x = 6)

let x = (1, 2)

