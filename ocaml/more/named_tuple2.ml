(* times *)
let string_of_month m =
  match m with
  | 0 -> "January"
  | 1 -> "February"
  | 2 -> "March"
  | 3 -> "April"
  | 4 -> "May"
  | 5 -> "June"
  | 6 -> "July"
  | 7 -> "August"
  | 8 -> "September"
  | 9 -> "October"
  | 10 -> "November"
  | 11 -> "December"
  | _ -> raise (Invalid_argument "string_of_month")

  let string_of_day d =
  match d with
  | 0 -> "Sunday"
  | 1 -> "Monday"
  | 2 -> "Tuesday"
  | 3 -> "Wednesday"
  | 4 -> "Thursday"
  | 5 -> "Friday"
  | 6 -> "Saturday"
  | _ -> raise (Invalid_argument "string_of_day")

let string_of_time () =
  let {
    Unix.tm_min;
    Unix.tm_hour;
    Unix.tm_mday;
    Unix.tm_mon;
    Unix.tm_year;
    Unix.tm_wday
  } = Unix.localtime (Unix.time ()) in
  "It is "
  ^ string_of_int tm_hour
  ^ ":"
  ^ string_of_int tm_min
  ^ " on "
  ^ string_of_day tm_wday
  ^ " "
  ^ string_of_int tm_mday
  ^ " "
  ^ string_of_month tm_mon
  ^ " "
  ^ string_of_int (tm_year + 1900)

let () =
  let v = string_of_time () in
  print_string v;
  print_newline ()
