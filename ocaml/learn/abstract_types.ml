module type INT31 = sig
  type t
  val create: int -> t
  val value: t -> int
end

module Int31: INT31 = struct
  type t = int
  let check x = if x < 0 || x > 30 then invalid_arg "Int31.create"
  let create x = check x; x
  let value x = x 
end
