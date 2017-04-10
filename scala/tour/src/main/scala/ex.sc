// ** util.Try
def loopAndFail(end: Int, failAt: Int): Int ={
  for (i <- 1 to end) {
    println(s"$i")
    if (i == failAt) throw new Exception("Too many iterations")
  }
  end
}

//loopAndFail(5, 3)

val t1 = util.Try(loopAndFail(5, 3))
// expression block
val t2 = util.Try { loopAndFail(2, 3) }

// ** future
import concurrent.ExecutionContext.Implicits.global

val f = concurrent.Future { Thread.sleep(2000); println("hi") }
//f.wait()
println("waiting")
