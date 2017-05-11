package fp

import java.io.File

/**
  * Created by andersc on 11/05/2017.
  */
object FileMatcher {
  private def filesHere = (new File("./src/main/scala/")).listFiles()

  private def filesMatching(matcher: String => Boolean) = {
    for (file <- filesHere if matcher(file.getName))
      yield file.getName
  }

  def endsWith(query: String) = filesMatching(_.endsWith(query))
  def contains(query: String) = filesMatching(_.contains(query))
  def regex(query: String) = filesMatching(_.matches(query))
}

object TestFileMatcher {
  def main(args: Array[String]): Unit = {
    for (file <- FileMatcher.regex(".+\\.sc")) {
      println(file)
    }
  }
}