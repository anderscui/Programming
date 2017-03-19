#load "defs.fs"
open oo

let author = Person(System.Guid.NewGuid(), "Anders", 36)
let author2 = Person("Anderson")

let p2 = Person2()
let p2_name = p2.Name
let p2_hobby = p2.Hobby

let sent = Sentence("The book of F#")
printfn "%A" sent.[3]
sent.[3] <- "Python"
printfn "%A" sent.[3]