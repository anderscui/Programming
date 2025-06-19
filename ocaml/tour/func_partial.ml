let () = assert (List.map (fun x -> x * 2) [10; 20; 30] = [20; 40; 60])
let () = assert (List.map (( * ) 2) [10; 20; 30] = [20; 40; 60])

let rec truncate_list n lst =
  if n <= 0 then []
  else match lst with
  | [] -> []
  | h :: t -> h :: truncate_list (n-1) t

let () = assert (truncate_list 2 [1; 2; 3] = [1; 2])

let truncate_lists n ls =
  List.map (truncate_list n) ls

let () = assert (truncate_lists 2 [[]; [1]; [1; 2]; [1; 2; 3]] = [[]; [1]; [1; 2]; [1; 2]])
