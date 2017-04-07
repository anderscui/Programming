package parsers

import scala.util.parsing.combinator.syntactical.StandardTokenParsers

/**
  * Created by andersc on 4/6/17.
  */
class ExprParser2 extends StandardTokenParsers {
  lexical.delimiters += ("+", "-", "*", "(", ")")

  def expr: Parser[Any] = term ~ rep(("+" | "-") ~ term)
  def term: Parser[Any] = factor ~ rep("*" ~> factor)
  def factor: Parser[Any] = numericLit | "(" ~> expr <~ ")"

  def parseAll[T](p: Parser[T], in: String): ParseResult[T] =
    phrase(p)(new lexical.Scanner(in))
}

object TestExprParser2 {
  def main(args: Array[String]): Unit = {
    val parser = new ExprParser
    parser.parseAll()
  }
}