package parsers

/**
  * Created by andersc on 4/5/17.
  */

import scala.util.parsing.combinator._

case class WordFreq(word: String, count: Int) {
  override def toString: String = "Word <" + word + ">" +
    "occurs with freq " + count
}

class SimpleParser extends RegexParsers {
  def word: Parser[String] = """[a-z]+""".r ^^ { _.toString }
  def number: Parser[Int] = """(0|[1-9]\d*)""".r ^^ { _.toInt }

  def freq: Parser[WordFreq] = word ~ number ^^ { case wd ~ fr => WordFreq(wd, fr) }
}

object WordFreqParser extends SimpleParser {
  def main(args: Array[String]): Unit = {
    parse(freq, "scala 121 python 100") match {
      case Success(matched, _) => println(matched)
      case Failure(msg, _) => println("FAILURE: " + msg)
      case Error(msg, _) => println("ERROR: " + msg)
    }
  }
}
