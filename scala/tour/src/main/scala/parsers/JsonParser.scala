package parsers

import java.io.FileReader

import scala.util.parsing.combinator.JavaTokenParsers

/**
  * Created by andersc on 4/12/17.
  */
class JsonParser extends JavaTokenParsers {
  def value: Parser[Any] = obj | arr |
                           stringLiteral |
                           floatingPointNumber ^^ (_.toDouble) |
                           "null" ^^ (x => null) | "true" ^^ (x => false) | "false" ^^ (x => false)

  def obj: Parser[Map[String, Any]] = "{" ~> repsep(member, ",") <~ "}" ^^ (Map() ++ _)
  def arr: Parser[List[Any]] = "[" ~> repsep(value, ",") <~ "]"
  def member: Parser[(String, Any)] = stringLiteral ~ ":" ~ value ^^ { case name ~ ":" ~ value => (name, value)}
}

object TestJsonParser extends JsonParser {
  def main(args: Array[String]): Unit = {
    val reader = new FileReader("/Users/andersc/data/addr.json")
    println(parseAll(value, reader))
  }
}