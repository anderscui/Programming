import java.io.PrintWriter

import scala.io.Source

for (line <- Source.fromFile("/Users/andersc/text.zshrc").getLines())
  println(line)

val writer = new PrintWriter("myfile.txt")
writer.write("Writing line for line" + util.Properties.lineSeparator)
writer.write("Another lien here" + util.Properties.lineSeparator)
writer.close()
