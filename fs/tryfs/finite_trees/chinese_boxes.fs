type Color = Red | Blue | Green | Yellow | Purple

type CBox = 
  | Nothing 
  | Cube of float * Color * CBox

let cube = Cube(2.0, Yellow, Cube(1.0, Green, Cube(0.5, Red, Nothing)))

let rec count_cubes = function
  | Nothing -> 0
  | Cube(s, c, cb) -> 1 + count_cubes cb

assert (count_cubes cube = 3)

let rec insert(r, c, cb) =
  if r <= 0.0 then failwith "non-positive length of box"
  else match cb with
       | Nothing -> Cube(r, c, Nothing)
       | Cube(r1, c1, cb1) -> 
         match compare r r1 with
         | t when t > 0 -> Cube(r, c, cb)
         | 0 -> failwith "equal length found"
         | _ -> Cube(r1, c1, insert(r, c, cb1))

let cube2 = insert(2.0, Yellow, insert(1.0, Green, Nothing))
let cube3 = insert(1.0, Yellow, insert(2.0, Green, Nothing))
