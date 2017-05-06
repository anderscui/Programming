// Generated from TL.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TLParser}.
 */
public interface TLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TLParser#parse}.
	 * @param ctx the parse tree
	 */
	void enterParse(TLParser.ParseContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#parse}.
	 * @param ctx the parse tree
	 */
	void exitParse(TLParser.ParseContext ctx);
}