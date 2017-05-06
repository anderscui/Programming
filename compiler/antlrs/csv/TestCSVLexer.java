import org.antlr.v4.runtime.*;

public class TestCSVLexer {
  public static void main(String[] args) {
    // the input source
    String source =
        "value1,value2,\"value3.1,\"\",value3.2\"" + "\n" +
        "\"line\nbreak\",Bbb,end";

    CSVLexer lexer = new CSVLexer(new ANTLRInputStream(source));
    CommonTokenStream tokens = new CommonTokenStream(lexer);

    tokens.fill();

    int n = 1;
    for (Object o: tokens.getTokens()) {
      CommonToken token = (CommonToken)o;
      System.out.println("token(" + n + ") = " + token.getText().replace("\n", "\\n"));
      n++;
    }
  }
}
