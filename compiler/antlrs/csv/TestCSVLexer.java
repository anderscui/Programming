import java.util.List;

import org.antlr.v4.runtime.*;

public class TestCSVLexer {
  public static void main(String[] args) {
    // the input source
    String source =
        "value1,value2,\"value3.1,\"\",value3.2\"" + "\n" +
        "\"line\nbreak\",Bbb,end";

    CSVLexer lexer = new CSVLexer(new ANTLRInputStream(source));
    CommonTokenStream tokens = new CommonTokenStream(lexer);
    CSVParser parser = new CSVParser(tokens);

    // validate the grammar.
    //parser.file();

    List<List<String>> data = parser.file().data;
    for (int r = 0; r < data.size(); r++) {
      List<String> row = data.get(r);
      for (int c = 0; c < row.size(); c++) {
        System.out.println("(row=" + (r+1) + ", col=" + (c+1) + ") = " + row.get(c));
      }
    }
  }
}
