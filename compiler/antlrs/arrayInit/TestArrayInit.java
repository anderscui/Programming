import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class TestArrayInit {
  public static void main(String[] args) throws Exception {
    ANTLRInputStream input = new ANTLRInputStream(System.in);
    ArrayInitLexer lexer = new ArrayInitLexer(input);
    CommonTokenStream tokens = new CommonTokenStream(lexer);
    ArrayInitParser parser = new ArrayInitParser(tokens);
    ParseTree tree = parser.init(); // begin parsing at 'init rule'
    System.out.println(tree.toStringTree(parser));
  }
}
