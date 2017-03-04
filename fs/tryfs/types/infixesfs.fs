// exclusive or
let (.||.) p q = (p || q) && (not (p && q))

let ans = (1 > 2) .||. (2 + 3 >= 5)
let ans1 = true .||. true

// prefix - reciprocal
let (~%%) x = 1.0 / x

let ans2 = %% 0.5
