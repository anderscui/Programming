type RGB = { R: byte; G: byte; B: byte }
type color = { R: byte; G: byte; B: byte }
             static member Red = { R = 255uy; G = 0uy; B = 0uy }
             member x.ToHexString() =
                sprintf "#%02X%02X%02X" x.R x.G x.B

let red = { R = 255uy; G = 0uy; B = 0uy }

// to avoid naming conflicts
let green = { RGB.R = 0uy; G = 255uy; B = 0uy }

// copy and update
let yellow = { red with G = 255uy }
let ans = yellow.ToHexString()