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


  }
}
