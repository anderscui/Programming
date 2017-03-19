open System
open System.IO

try
  use file = File.OpenText "test.txt"
  file.ReadToEnd() |> printfn "%s"
with
  | :? FileNotFoundException as ex -> printfn "%s not found" ex.FileName
  | :? PathTooLongException
  | :? ArgumentNullException ->
    printfn "Invalid file name"
  | _ -> printfn "Error loading file"
         reraise()

let filename = "x"
if not (File.Exists filename) then
  raise <| FileNotFoundException("file not found...")