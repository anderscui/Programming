open System

let createDisposable name =
  printfn "creating: %s" name
  { new IDisposable with 
    member x.Dispose() = printfn "disposing: %s" name 
}

let testDisposable() =
  use root = createDisposable "outer"
  for i in [1..2] do
    use nested = createDisposable (sprintf "inner %i" i)
    printfn "completing iteration %i" i
  printfn "leaving func"
  
