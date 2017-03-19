open DataStructs

let x = StackNode(1,
          StackNode(2,
            StackNode(3, EmptyStack)))
            
let y = getRange 5 10

printfn "%A" x
printfn "%A" y

// compile: fsharpc  DataStructures.fs DsClient.fs --target:exe
// exe: mono DsClient.exe