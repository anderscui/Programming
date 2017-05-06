import java.util.HashMap;
import java.util.Map;

import org.antlr.v4.runtime.ANTLRFileStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

public class Main {
    public static void main(String[] args) {
        try {
            TLLexer lexer = new TLLexer(new ANTLRFileStream("test.tl"));
            TLParser parser = new TLParser(new CommonTokenStream(lexer));
            parser.setBuildParseTree(true);
            ParseTree tree = parser.parse();

            // Pass 1: collect functions
            Map<String, Function> functions = new HashMap<String, Function>();
            SymbolVisitor symbolVisitor = new SymbolVisitor(functions);
            symbolVisitor.visit(tree);

            // Pass 2: evaluation
            Scope scope = new Scope();
            EvalVisitor visitor = new EvalVisitor(scope, functions);
            visitor.visit(tree);

        } catch (Exception e) {
            if ( e.getMessage() != null) {
                System.err.println(e.getMessage());
            } else {
                e.printStackTrace();
            }
        }
    }
}
