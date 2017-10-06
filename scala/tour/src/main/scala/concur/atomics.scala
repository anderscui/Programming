package concur

import java.util.concurrent.atomic.AtomicLong

import scala.annotation.tailrec

object AtomicUid extends App {
  private val uid = new AtomicLong(0L)

  def getUniqueId: Long = uid.incrementAndGet()

  execute { log(s"Uid async: $getUniqueId") }
  log(s"Got a uid: $getUniqueId")
}

object CasUid extends App {
  private val uid = new AtomicLong(0L)

  @tailrec
  def getUniqueId: Long = {
    val oldId = uid.get()
    val newId = oldId + 1
    if (uid.compareAndSet(oldId, newId)) newId else getUniqueId
  }

  execute { log(s"Uid async: $getUniqueId") }
  log(s"Got a uid: $getUniqueId")
}
