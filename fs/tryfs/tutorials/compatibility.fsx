let success, i = System.Int32.TryParse("123")
if success 
then printfn "parsed as %i" i
else printfn "parse failed"

// extension method
type System.String with
  member this.StartsWithA = this.StartsWith "A"

let s = "Alice"
printfn "'%s' starts with an 'A' = %A" s s.StartsWithA