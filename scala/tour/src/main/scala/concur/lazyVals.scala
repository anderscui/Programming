package concur

object LazyValsCreate extends App {
  lazy val obj = new AnyRef
  lazy val non = s"made by ${Thread.currentThread.getName}"

  execute {
    log(s"EC sees obj = $obj")
    log(s"EC sees non = $non")
  }

  log(s"Main sees obj = $obj")
  log(s"Main sees non = $non")

  Thread.sleep(200)
}

object LazyValsObject extends App {
  object Lazy { log("Running Lazy ctor.") }
  log("Main thread is about to reference Lazy.")
  Lazy
  log("Main thrad completed.")
}

object LazyValsUnderTheHood extends App {
  @volatile
  private var _bitmap = false

  private var _obj: AnyRef = _
  def obj = if (_bitmap) _obj else this.synchronized {
    if (!_bitmap) {
      _obj = new AnyRef
      _bitmap = true
    }
    _obj
  }
  log(s"$obj")
  log(s"$obj")
}
