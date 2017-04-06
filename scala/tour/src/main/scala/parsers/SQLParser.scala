package parsers

import scala.util.parsing.combinator._

class SQLParser extends JavaTokenParsers {

  def query: Parser[Query] = operation ~ from ~ opt(where) ~ opt(order) ^^ {
    case operation ~ from ~ where ~ order => Query(operation, from, where, order)
  }

  def operation: Parser[Operation] = {
    ("select" | "update" | "delete") ~ repsep(ident, ",") ^^ {
      case "select" ~ f => Select(f: _*)
      case _ => throw new IllegalArgumentException("Operation not implemented")
    }
  }

  def from: Parser[From] = "from" ~> ident ^^ (From(_))

  def where: Parser[Where] = "where" ~> rep(clause) ^^ (Where(_: _*))

  def clause: Parser[Clause] = (predicate | parens) * (
    "and" ^^^ { (a: Clause, b: Clause) => And(a, b) } |
      "or" ^^^ { (a: Clause, b: Clause) => Or(a, b) }
    )

  def parens: Parser[Clause] = "(" ~> clause <~ ")"

  def predicate = (
    ident ~ "=" ~ boolean ^^ { case f ~ "=" ~ b => BooleanEquals(f, b) }
      | ident ~ "=" ~ stringLiteral ^^ { case f ~ "=" ~ v => StringEquals(f, stripQuotes(v)) }
      | ident ~ "=" ~ wholeNumber ^^ { case f ~ "=" ~ i => NumberEquals(f, i.toInt) }

    )

  def boolean: Parser[Boolean] = "true" ^^^ true | "false" ^^^ false

  def order: Parser[Direction] = {
    "order" ~> "by" ~> ident ~ ("asc" | "desc") ^^ {
      case f ~ "asc" => Asc(f)
      case f ~ "desc" => Desc(f)
    }
  }

  def stripQuotes(s: String): String = s.substring(1, s.length - 1)

  def parse(sql: String): Option[Query] = {
    parseAll(query, sql) match {
      case Success(r, _) => Option(r)
      case x => println(x); None
    }
  }
}

object TestSQLParser extends SQLParser {
  def main(args: Array[String]): Unit = {
//    val q = Select("*") from "user"
//    println(q)
    val sql = """select name,age from select where name = "peter" and (active = true or age = 30)"""
    val query = parse(sql).get
    print(query)
  }
}