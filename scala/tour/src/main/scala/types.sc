// avoid using asInstanceOf, prefer the to<type> methods.
val isFiveLong = 5.asInstanceOf[Long]
val classOf = 5.0.isInstanceOf[Float]
val hash = 'A'.hashCode
val tobyte = 20.toByte

// tuples
val info = (5, "Korben", true)
val bln = info._3

// pair
val red = "red" -> "0xff0000"
val reversed = red._2 -> red._1

