type ptype = TNormal | TFire | TWater
type mon = {name: string; hp: int; ptype: ptype}

let m = {name = "Charmander"; hp = 39; ptype = TFire}

let get_hp m = match m with {name = n; hp = h; ptype = t } -> h
let _ = Printf.printf "hp = %d\n" (get_hp m)

let get_hp m = match m with {name = _; hp = h; ptype = _ } -> h
let _ = Printf.printf "hp = %d\n" (get_hp m)

let get_hp m = match m with {name; hp; ptype} -> hp
let _ = Printf.printf "hp = %d\n" (get_hp m)

let get_hp m = match m with { hp } -> hp
let _ = Printf.printf "hp = %d\n" (get_hp m)

let get_hp m = m.hp
let _ = Printf.printf "hp = %d\n" (get_hp m)

let fst (x, _) = x
let snd (_, y) = y
let () = assert (fst (1, 2) = 1)
let () = assert (snd (1, 2) = 2)

(* OK *)
let third t = match t with x, y, z -> z

(* good *)
let third t = let x, y, z = t in z

(* better *)
let third t = let _, _, z = t in z
let () = assert (third (1, 2, 3) = 3)

(* best *)
let third (_, _, z) = t
let () = assert (third (1, 2, 3) = 3)
