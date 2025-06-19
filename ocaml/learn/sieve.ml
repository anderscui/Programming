let bound = read_int ()

let prime = Array.make (bound + 1) true

let () = 
  prime.(0) <- false;
  prime.(1) <- false;
  let limit = truncate (sqrt (float bound)) in
  for n = 2 to limit do
    if prime.(n) then begin
      let m = ref (n * n) in
      while !m <= bound do
        prime.(!m) <- false;
        m := !m + n
      done
    end
  done

let () = 
  for n = 2 to bound do
    if prime.(n) then Printf.printf "%d " n
  done;
