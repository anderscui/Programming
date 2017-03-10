module MyLib.Vector

type Vector

val ( ~-. ) : Vector -> Vector
val ( +. ) : Vector -> Vector -> Vector
val ( -. ) : Vector -> Vector -> Vector
val ( *. ) : float -> Vector -> Vector
val ( &. ) : Vector -> Vector -> Vector
val norm : Vector -> float
val make : float * float -> Vector
val coord : Vector -> float * float

// compile -> dll
// fsharpc -a vector.fsi vector.fs
