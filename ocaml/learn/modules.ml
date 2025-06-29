module type I = sig
  val a: int
  val f: int -> int
end

module M: I = struct
  let a = 42
  let b = 3
  let f x = a * x + b
end

let () = print_int M.a
