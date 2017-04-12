package parsers

import scala.util.parsing.combinator.JavaTokenParsers

/**
  * Created by andersc on 4/6/17.
  */
class Arith extends JavaTokenParsers {
  def expr: Parser[Any] = term ~ rep("+" ~ term | "-" ~ term)
  def term: Parser[Any] = factor ~ rep("*" ~ factor | "/" ~ factor)
  def factor: Parser[Any] = floatingPointNumber | "(" ~ expr ~ ")"
}

object TestArith extends Arith {
  def main(args: Array[String]): Unit = {
    println(parseAll(expr, "2 * (3 + 7)"))
  }
}