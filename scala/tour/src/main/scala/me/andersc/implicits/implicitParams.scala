package me.andersc.implicits

import me.andersc.Delimiters

object implicitParams {
  def quote(what: String)(implicit delims: Delimiters) =
    s"${delims.left} $what ${delims.right}"

  def main(args: Array[String]): Unit = {
    println(quote("Bonjour le monde")(Delimiters("<<", ">>")))

    // import me.andersc.FrenchPunctuation._
    // println(quote("Bonjour le monde"))

    implicit val delim = Delimiters("<", ">")
    println(quote("hello"))
  }
}
