trait HtmlUtils {
  def removeMarkup(input: String) = {
    input.replaceAll("""</?\w[^>]*>""", "").replaceAll("<.*>", "")
  }
}

trait SafeStringUtils {
  def trimToNone(s: String): Option[String] = {
    Option(s) map (_.trim) filterNot (_.isEmpty)
  }
}

class Page(val s: String) extends SafeStringUtils with HtmlUtils {
  def asPlainText = {
    trimToNone(s) map removeMarkup getOrElse "n/a"
  }
}

new Page("<html><body><h1>Introduction</h1></body></html>").asPlainText
new Page("  ").asPlainText
new Page(null).asPlainText
