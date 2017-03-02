// val a : char = 'a'
let a = 'a'

// val isLowerCaseVowel : c:char -> bool
let isLowerCaseVowel c =
  c = 'a' || c = 'e' || c = 'i' || c = 'o' || c = 'u'

let isLowerConsonant c =
  System.Char.IsLower c && not (isLowerCaseVowel c)
  
let ans1 = isLowerCaseVowel a
let ans2 = isLowerConsonant 'b'

(* string type *)
let s = "Hello, world"

// verbatim
let len = String.length s
let concat = "a" + "b"
let ch_in_str = s.[0] // H

// monadic op has higher precedence
let plus = "one" + string 1

