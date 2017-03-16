module Vector

[<Sealed>]
type Vector =
  static member ( ~- ) : Vector -> Vector
  static member ( + ) : Vector * Vector -> Vector
  static member ( - ) : Vector * Vector -> Vector
  static member ( * ) : float * Vector -> Vector
  static member ( * ) : Vector * Vector -> float
  
val make : float * float -> Vector
val coord : Vector -> float * float
val norm : Vector -> float

// compile -> dll
// fsharpc -a vector.fsi vector.fs
