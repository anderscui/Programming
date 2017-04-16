case class Character(name: String, isThief: Boolean)
val h = Character("Hadrian", true)
val r = h.copy(name = "Royce")

h match {
  case Character(x, true) => s"$x is a thief"
  case Character(x, false) => s"$x is not a thief"
}