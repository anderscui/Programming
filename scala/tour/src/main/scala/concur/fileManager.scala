package concur

import java.io.File
import java.util.concurrent.{ConcurrentHashMap, LinkedBlockingQueue}
import java.util.concurrent.atomic.AtomicReference

import scala.annotation.tailrec
import scala.collection.JavaConverters._
import org.apache.commons.io.FileUtils

import scala.collection.concurrent

sealed trait State
class Idle extends State
class Creating extends State
class Copying(val n: Int) extends State
class Deleting extends State


class Entry(val isDir: Boolean) {
  val state = new AtomicReference[State](new Idle)
}

class FileSystem(root: String) {

  val rootDir = new File(root)
  val files: concurrent.Map[String, Entry] = new ConcurrentHashMap[String, Entry]().asScala
  for (f <- FileUtils.iterateFiles(rootDir, null, false).asScala) {
    println(f.getName)
    // put method is atomic
    files.put(f.getName, new Entry(false))
  }

  private val messages = new LinkedBlockingQueue[String]()

  val logger = new Thread {
    setDaemon(true)
    override def run() = while (true) {
      log(messages.take())
    }
  }
  logger.start()

  def logMessage(msg: String): Unit = messages.offer(msg)

  @tailrec
  private def prepareForDelete(entry: Entry): Boolean = {
    val s0 = entry.state.get()
    s0 match {
      case i: Idle =>
        if (entry.state.compareAndSet(s0, new Deleting))
          true
        else
          prepareForDelete(entry)
      case c: Creating =>
        logMessage("File currently created, cannot delete.")
        false
      case c: Copying =>
        logMessage("File currently copied, cannot delete.")
        false
      case d: Deleting =>
        false
    }
  }

  def deleteFile(filename: String): Unit = {
    files.get(filename) match {
      case None =>
        logMessage(s"Path '$filename' does not exist")
      case Some(entry) if entry.isDir =>
        logMessage(s"Path '$filename' is a dir")
      case Some(entry) => execute {
        if (prepareForDelete(entry)) {
          if (FileUtils.deleteQuietly(new File(filename)))
            files.remove(filename)
        }
      }
    }
  }

  @tailrec
  private def acquire(entry: Entry): Boolean = {
    val s0 = entry.state.get()
    s0 match {
      case _: Creating | _: Deleting =>
        logMessage("File inaccessible, cannot copy...")
        false
      case i: Idle =>
        if (entry.state.compareAndSet(s0, new Copying(1)))
          true
        else
          acquire(entry)
      case c: Copying =>
        if (entry.state.compareAndSet(s0, new Copying(c.n+1)))
          true
        else
          acquire(entry)
    }
  }

  @tailrec
  private def release(entry: Entry): Unit = {
    val s0 = entry.state.get()
    s0 match {
      case c: Creating =>
        if (!entry.state.compareAndSet(s0, new Idle))
          release(entry)
      case c: Copying =>
        val new_state = if (c.n == 1) new Idle else new Copying(c.n-1)
        if (!entry.state.compareAndSet(s0, new_state))
          release(entry)
    }
  }
}

object TestFileSystem {
  def main(args: Array[String]): Unit = {
    val fs = new FileSystem(".")
    //fs.logMessage("Testing log!")
    fs.deleteFile("test.txt")

    log("done")
    Thread.sleep(100)
  }
}

