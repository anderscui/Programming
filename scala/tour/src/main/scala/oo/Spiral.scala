package oo

import Element.elem

/**
  * Created by andersc on 11/05/2017.
  */
object Spiral {
  val space = elem(" ")
  val corner = elem("+")

  def spiral(nEdges: Int, direction: Int): Element = {
    if (nEdges == 1)
      elem("+")
    else {
      val sp = spiral(nEdges - 1, (direction + 3) % 4)
      def verBar = elem('|', 1, sp.height)
      def horBar = elem('-', sp.width, 1)
      if (direction == 0)
        (corner beside horBar) above (sp beside space)
      else if (direction == 1)
        (sp beside space) beside (corner above verBar)
      else
        (verBar above corner) beside (space above sp)
    }
  }

  def main(args: Array[String]): Unit = {
    val nSides = 6
    println(spiral(nSides, 0))
  }
}
