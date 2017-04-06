package parsers

/**
  * Created by andersc on 4/5/17.
  */
import scala.util.parsing.combinator.PackratParsers
import scala.util.parsing.combinator.syntactical._

object ArithmetricParser extends StandardTokenParsers with PackratParsers {
  lexical.delimiters ++= List(".", ";", "+", "-", "*", "/")

  lazy val num = numericLit

  lazy val expr: PackratParser[Int] = plus | minus | multi | div
  lazy val plus: PackratParser[Int] = num ~ "+" ~ num ^^ { case n1 ~ "+" ~ n2 => n1.toInt + n2.toInt }
  lazy val minus: PackratParser[Int] = num ~ "-" ~ num ^^ { case n1 ~ "-" ~ n2 => n1.toInt - n2.toInt }
  lazy val multi: PackratParser[Int] = num ~ "*" ~ num ^^ { case n1 ~ "*" ~ n2 => n1.toInt * n2.toInt }
  lazy val div: PackratParser[Int] = num ~ "/" ~ num ^^ { case n1 ~ "/" ~ n2 => n1.toInt / n2.toInt }

  def parse(input: String) = {
    val myread = new PackratReader(new lexical.Scanner(input))
    println("processing " + input)
    phrase(expr)(myread) match {
      case Success(result, _) => println("Success"); println(result); Some(result)
      case n => println(n); println("Err!"); None
    }
  }

  def main(args: Array[String]): Unit = {
    val prg = "6 *3" :: "24-/*abc*/4" :: "a+5" :: "21/3" :: Nil
    prg.map(parse)
  }
}
