package parsers

import scala.util.matching.Regex
import scala.util.parsing.combinator.RegexParsers

/**
  * Created by andersc on 4/6/17.
  */
class ExprParser extends RegexParsers {
  val number: Regex = "[0-9]+".r

  def expr: Parser[Int] = term ~ opt(("+" | "-") ~ expr) ^^ {
    case t ~ None => t
    case t ~ Some("+" ~ e) => t + e
    case t ~ Some("-" ~ e) => t - e
  }
  def term: Parser[Int] = factor ~ rep("*" ~> factor) ^^ {
    case f ~ r => f * r.product
  }
  def factor: Parser[Int] = number ^^ { _.toInt } | "(" ~> expr <~ ")"
}

object TestExprParser {
  def main(args: Array[String]): Unit = {
    val parser = new ExprParser
    val result = parser.parseAll(parser.expr, "3-4*5")
    if (result.successful)
      println(result.get)
  }
}