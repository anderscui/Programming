let rec concat_lists lists =
  match lists with
  | [] -> []
  | h :: t -> h @ concat_lists t

let () = assert (concat_lists [[1; 2]; [3]; [4; 5]] = [1; 2; 3; 4; 5])

let rec concat_inner lists acc =
  match lists with
  | [] -> acc
  | h :: t -> concat_inner t (acc @ h)

let concat lists =
  concat_inner lists []

let () = assert (concat [[1; 2]; [3]; [4; 5]] = [1; 2; 3; 4; 5])

let rec all lst =
  match lst with
  | [] -> true
  | h :: t -> h && (all t)

let all_contains_true lists =
  not (List.mem false (List.map (List.mem true) lists))

let () = assert (all_contains_true [[true]; [false; true]; [true; true]])
let () = assert (not (all_contains_true [[true]; [false; true]; [false]]))

let count_exclamations s =
  let n = ref 0 in
    String.iter (function '!' -> n := !n + 1 | _ -> ()) s;
    !n

let () = assert (count_exclamations "hello! world!" = 2)
let () = assert (count_exclamations "hello, world!" = 1)
let () = assert (count_exclamations "hello, world." = 0)

let strs = ["hello"; " world"; "!"]
let () = assert (String.concat "" strs = "hello world!")
