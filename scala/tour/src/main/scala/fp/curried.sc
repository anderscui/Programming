import java.io.{File, PrintWriter}

def curriedSum(x: Int)(y: Int) = x + y

// the underscore is pretty ugly:)
val first = curriedSum(1) _
first(2)

def withPrintWriter(file: File)(op: PrintWriter => Unit) = {
  val writer = new PrintWriter(file)
  try {
    op(writer)
  } finally {
    writer.close()
  }
}

// 'closures' enable a better 'control structure'
val file = new File("test.sbt")
withPrintWriter(file) { writer =>
  writer.println(new java.util.Date)
}

