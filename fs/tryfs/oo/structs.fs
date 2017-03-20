namespace oo

open System

[<Struct>]
type Circle(diameter: float) =
  member x.getRadius() = diameter / 2.0
  member x.Diameter = diameter
  member x.GetArea() = Math.PI * (x.getRadius() ** 2.0)
