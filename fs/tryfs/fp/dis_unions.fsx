let show_option(v: _ option) =
  printfn "%s" (match v with
                | Some x -> x.ToString()
                | None -> "None")

let vi = Some 123 |> show_option
let si = Some "abc" |> show_option
let ni = None |> show_option

// represent simple object hierarchies.
type Shape =
| Circle of float
| Rectangle of float * float
| Triangle of float * float * float

type Shape2 =
| Circle of Radius : float
| Rectangle of Width : float * Height : float
| Triangle of Leg1 : float * Leg2 : float * Leg3 : float

let r = Rectangle(Width = 10.0, Height = 20.0)

// tree struct
type Markup =
| ContentElement of string * Markup list
| EmptyElement of string
| Content of string

// TODO: toHtml @page 127.
