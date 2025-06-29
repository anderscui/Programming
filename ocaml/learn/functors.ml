module type X = sig
  val x : int
end

module IncX (M : X) = struct
  let x = M.x + 1
end

module A = struct let x = 0 end
module B = IncX (A)

let _ = assert (B.x = 1)

module C = IncX (struct let x = 41 end)
let _ = assert (C.x = 42)

module AddX (M : X) = struct
  let add y = M.x + y
end
module Add42 = AddX (struct let x = 42 end)

module type Add = sig
  val add: int -> int
end
module CheckAddX: X -> Add = AddX
