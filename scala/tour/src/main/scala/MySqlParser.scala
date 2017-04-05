/**
  * Created by andersc on 4/5/17.
  */

import scala.util.parsing.combinator._
import scala.util.parsing.combinator.syntactical._

abstract class Direction
case class Asc(field: String*) extends Direction
case class Desc(field: String*) extends Direction

case class Select(fields: String*)
case class From(table: String)
case class Count(field: String)

class SqlParser extends JavaTokenParsers {

  // select * from users
  def selectAll: Parser[Select] = "select" ~ "*" ^^^ Select("*")
  def from: Parser[From] = "from" ~> ident ^^ (From(_))

  // select name, age from users
  def select: Parser[Select] = "select" ~ repsep(ident, ",") ^^ {
    case "select" ~ f => Select(f: _*)
  }

  // select count(name) from users
  def count: Parser[Count] = "select" ~ "count" ~> "(" ~> ident <~ ")" ^^ {
    case exp => Count(exp)
  }

  // select * from users order by age desc
  def order: Parser[Direction] = {
    "order" ~> "by" ~> ident ~ ("asc" | "desc") ^^ {
      case f ~ "asc" => Asc(f)
      case f ~ "desc" => Desc(f)
    }
  }


}


