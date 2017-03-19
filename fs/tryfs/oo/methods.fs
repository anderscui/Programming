namespace oo

open System

type Circle(diameter) =
  let getRadius() = diameter / 2.0
  member private x.GetRadius() = diameter / 2.0
  member x.Diameter = diameter
  member x.GetArea() =
    let r = diameter / 2.0
    Math.PI * (r ** 2.0)