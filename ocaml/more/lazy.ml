type 'a lazylist = Cons of 'a * (unit -> 'a lazylist)

let rec lseq n =
  Cons (n, fun () -> lseq (n+1))

let lhd (Cons (n, _)) = n
let ltl (Cons (_, tf)) = tf ()

let rec ltake (Cons (h, tf)) n =
  match n with
  | 0 -> []
  | _ -> h :: ltake (tf ()) (n-1)

let rec ldrop (Cons (h, tf) as ll) n =
  match n with 
  | 0 -> ll
  | _ -> ldrop (tf ()) (n-1)

let () = assert (ltake (lseq 2) 5 = [2; 3; 4; 5; 6])
let () = assert (ltake (ldrop (lseq 2) 1) 5 = [3; 4; 5; 6; 7])

let rec lmap f (Cons (h, tf)) = 
  Cons (f h, fun () -> lmap f (tf ()))

let rec lfilter f (Cons (h, tf)) =
  if f h then
    Cons (h, fun () -> lfilter f (tf ()))
  else
    lfilter f (tf ())

let cubes =
  lfilter 
    (fun x -> x mod 5 = 0)
    (lmap (fun x -> x * x * x) (lseq 1))

let () = assert (ltake cubes 3 = [125; 1000; 3375])

let rec mkprimes (Cons (h, tf)) =
  Cons (h, fun () -> 
    mkprimes (lfilter (fun x -> x mod h <> 0) (tf ())))

let primes = mkprimes (lseq 2)
let () = assert (ltake primes 8 = [2; 3; 5; 7; 11; 13; 17; 19])

let rec interleave (Cons (h, tf)) lst = 
  Cons (h, fun () -> interleave lst (tf ()))

let () = assert (ltake (interleave (lseq 1) (lseq 2)) 6 = [1; 2; 2; 3; 3; 4])

let rec lconst n =
  Cons (n, fun () -> lconst n)

let () = assert (ltake (interleave (lconst 0) (lconst 1)) 6 = [0; 1; 0; 1; 0; 1])

let rec powers start power =
  Cons (start, fun () -> powers (start * power) power)

let () = assert (ltake (powers 1 2) 5 = [1; 2; 4; 8; 16])

