package me.andersc

case class Delimiters(left: String, right: String)

object FrenchPunctuation {
  implicit val quoteDelimiters: Delimiters = Delimiters("<-", "->")
}
