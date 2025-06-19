let extract o =
  match o with
  | Some i -> string_of_int i
  | None -> ""

let () = assert (extract (Some 42) = "42")
let () = assert (extract (None) = "")

let rec max_of_list lst =
  match lst with
  | [] -> None
  | h :: t -> begin
    match max_of_list t with
    | None -> Some h
    | Some m -> Some (max h m)
  end

let () = assert (max_of_list [1; 2; 3] = Some 3)
let () = assert (max_of_list [] = None)
