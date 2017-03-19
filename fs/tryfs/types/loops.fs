//let echoUserInput (getInput: unit -> string) =
//  let mutable input = getInput()
//  while not (input.ToUpper().Equals("QUIT")) do
//    printfn "You entered: %s" input
//    input <- getInput()
    
//echoUserInput (fun () -> printfn "Type sth and press enter"
//                         System.Console.ReadLine())
                         
for i = 0 to 2 do printfn "%i" i
for i = 10 downto 8 do printfn "%A" i