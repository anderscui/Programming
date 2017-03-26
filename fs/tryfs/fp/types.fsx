let point = 1.0, 2.0

let slope p1 p2 =
  let x1, y1 = p1
  let x2, y2 = p2
  (y1 - y2) / (x1 - x2)

let slope2 (x1, y1) (x2, y2) = 
  (y1 - y2) / (x1 - x2)

// out params
// v = 1, r = true
let r, v = System.Int32.TryParse "1"

