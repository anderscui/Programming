import org.antlr.v4.runtime.*;

public class TestTL {
  public static void main(String[] args) throws Exception {
    TLLexer lexer = new TLLexer(new ANTLRFileStream(args[0]));
    CommonTokenStream tokens = new CommonTokenStream(lexer);
    TLParser parser = new TLParser(tokens);
    parser.parse();
    System.out.println("Done");
  }
}
