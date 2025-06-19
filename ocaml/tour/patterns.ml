let is_vowel = function
  | 'a' | 'e' | 'i' | 'o' | 'u' -> true
  | _ -> false

let () = assert (is_vowel 'o')
let () = assert (not (is_vowel 'c'))

let is_lower c =
  match c with
  | 'a'..'z' -> true
  | _ -> false

let () = assert (is_lower 'a')
let () = assert (is_lower 'm')
let () = assert (is_lower 'z')
let () = assert (not (is_lower 'A'))
let () = assert (not (is_lower 'Z'))

let is_upper c =
  match c with
  | 'A'..'Z' -> true
  | _ -> false

