package logs

import com.typesafe.scalalogging.{LazyLogging, Logger}
import org.slf4j.LoggerFactory

/**
  * Created by andersc on 6/4/17.
  */
object loggy extends LazyLogging {
  //val logger = Logger(loggy.getClass)
  //val logger = Logger("loggyLogger")
  def main(args: Array[String]): Unit = {
    logger.debug("logging lines")
  }
}
