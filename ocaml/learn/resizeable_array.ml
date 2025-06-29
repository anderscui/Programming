module type ResizeableArray = sig
  type 'a t
  val length: 'a t -> int
  val make: int -> 'a -> 'a t
  val resize: 'a t -> int -> unit
  val get: 'a t -> int -> 'a
  val set: 'a t -> int -> 'a -> unit
end

type 'a t = {
  default: 'a;
  mutable size: int;
  mutable data: 'a array;
}

let length a = a.size

let make n d = {
  default=d;
  size=n;
  data = Array.make n d
}

let get a i =
  if i < 0 || i >= a.size then invalid_arg "get";
  a.data.(i)

let set a i v =
  if i < 0 || i >= a.size then invalid_arg "set";
  a.data.(i) <- v

let resize a s =
  if s <= a.size then
    Array.fill a.data s (a.size-s) a.default
  else begin
    let n = Array.length a.data in
    if s > n then begin
      let n' = max (2 * n) s in
      let a' = Array.make n' a.default in
      Array.blit a.data 0 a' 0 a.size;
      a.data <- a'
    end
  end;
  a.size <- s

let () =
  let arr = make 10 (-1) in
  set arr 0 1
