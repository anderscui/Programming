type date = {
  day: int;
  month: int;
  year: int
}

let valentine's_day = { day = 14; month = 2; year = 2025 }

let () = assert (valentine's_day.month = 2)

let d2 = { valentine's_day with day = 15 }
let () = assert (d2.year = 2025 && d2.month = 2 && d2.day = 15)

(* order *)
let d3 = { year = d2.year; month = d2.month; day = d2.day }
let () = assert (d2 = d3)

(* use pattern to retrieve fields *)
let { day; month; _ } = valentine's_day
let () = assert (day = 14 && month = 2)

(* mutable fields *)
type student = { 
  number: int;
  mutable age: int
}

let birthday e =
  e.age <- e.age + 1

(* simulate traditional notion of mutable vars. *)
type var = {
  mutable value: int
}

let x = { value = 41 }
let () = x.value <- x.value + 1
let () = assert (x.value = 42)

(* the above `var` can be replaced with references *)
let x = ref 41
let () = assert (x.contents = 41)
let () = assert (!x = 41)

let () = x := !x + 1
let () = assert (!x = 42)

(* eval order *)
(* let x = (read_int (), read_int ()) *)
(* 2, 1 -> 1, 2 *)
(* let () = assert (x = (1, 2)) *)

(* a better way *)
let a = 
  let x = read_int () in
  let y = read_int () in
  (x, y)
let () = assert (a = (1, 2))
