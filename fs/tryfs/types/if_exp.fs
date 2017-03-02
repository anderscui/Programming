let even n = n % 2 = 0
let adjString s = if even(String.length s)
                  then s else " " + s

let ans1 = adjString "123"
let ans2 = adjString "1234"