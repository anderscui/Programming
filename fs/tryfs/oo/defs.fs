namespace oo

open System

type Person (id: Guid, name: string, age: int) = 
    new (name) = Person(Guid.NewGuid(), name, 18)
                 then printfn "Creating a person with default id and age."
    new () = Person("")
    member this.Id = id
    member this.Name = name
    member this.Age = age

// singleton
// lazy
type Greeter private () =
  static let _instance = lazy (Greeter())
  static member Instance with get() = _instance.Force()
  member x.SayHello() = printfn "hello"

// default value
// private field
// explicit property (in 2 ways)
// implicit property (Hobby)
type Person2() =
  [<DefaultValue>]
  val mutable private n : string
  [<DefaultValue>]
  val mutable private a : int

  member val Hobby = "" with get, set
  member x.Name
    with get() = x.n
    and set(v) = x.n <- v
  member x.Age with public get() = x.a
  member x.Age with internal set(value) = x.a <- value

type Sentence(initial: string) =
  let mutable words = initial.Split ' '
  let mutable text = initial
  member x.Item
    with get i = words.[i]
    and set i v =
      words.[i] <- v
      text <- String.Join(" ", words)