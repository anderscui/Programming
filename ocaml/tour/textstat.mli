(* hide types, so the clients can only use interface funcs. *)
(* type stats = int * int * int * int *)
type stats

val lines: stats -> int
val characters: stats -> int
val words: stats -> int
val sentences: stats -> int

(* this is a internal function, hide it. *)
(* val stats_from_channel: in_channel -> stats *)
val stats_from_file: string -> stats
