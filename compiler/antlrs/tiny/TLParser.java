// Generated from TL.g4 by ANTLR 4.7
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Println=1, Print=2, Assert=3, Size=4, Def=5, If=6, Else=7, Return=8, For=9, 
		While=10, To=11, Do=12, End=13, In=14, Null=15, Or=16, And=17, Equals=18, 
		NEquals=19, GTEquals=20, LTEquals=21, Pow=22, Excl=23, GT=24, LT=25, Add=26, 
		Subtract=27, Multiply=28, Divide=29, Modulus=30, OBrace=31, CBrace=32, 
		OBracket=33, CBracket=34, OParen=35, CParen=36, SColon=37, Assign=38, 
		Comma=39, QMark=40, Colon=41, Bool=42, Number=43, Identifier=44, String=45, 
		Comment=46, Space=47;
	public static final int
		RULE_parse = 0;
	public static final String[] ruleNames = {
		"parse"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'println'", "'print'", "'assert'", "'size'", "'def'", "'if'", "'else'", 
		"'return'", "'for'", "'while'", "'to'", "'do'", "'end'", "'in'", "'null'", 
		"'||'", "'&&'", "'=='", "'!='", "'>='", "'<='", "'^'", "'!'", "'>'", "'<'", 
		"'+'", "'-'", "'*'", "'/'", "'%'", "'{'", "'}'", "'['", "']'", "'('", 
		"')'", "';'", "'='", "','", "'?'", "':'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "Println", "Print", "Assert", "Size", "Def", "If", "Else", "Return", 
		"For", "While", "To", "Do", "End", "In", "Null", "Or", "And", "Equals", 
		"NEquals", "GTEquals", "LTEquals", "Pow", "Excl", "GT", "LT", "Add", "Subtract", 
		"Multiply", "Divide", "Modulus", "OBrace", "CBrace", "OBracket", "CBracket", 
		"OParen", "CParen", "SColon", "Assign", "Comma", "QMark", "Colon", "Bool", 
		"Number", "Identifier", "String", "Comment", "Space"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "TL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ParseContext extends ParserRuleContext {
		public Token t;
		public TerminalNode EOF() { return getToken(TLParser.EOF, 0); }
		public ParseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parse; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TLListener ) ((TLListener)listener).enterParse(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TLListener ) ((TLListener)listener).exitParse(this);
		}
	}

	public final ParseContext parse() throws RecognitionException {
		ParseContext _localctx = new ParseContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_parse);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(6);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Println) | (1L << Print) | (1L << Assert) | (1L << Size) | (1L << Def) | (1L << If) | (1L << Else) | (1L << Return) | (1L << For) | (1L << While) | (1L << To) | (1L << Do) | (1L << End) | (1L << In) | (1L << Null) | (1L << Or) | (1L << And) | (1L << Equals) | (1L << NEquals) | (1L << GTEquals) | (1L << LTEquals) | (1L << Pow) | (1L << Excl) | (1L << GT) | (1L << LT) | (1L << Add) | (1L << Subtract) | (1L << Multiply) | (1L << Divide) | (1L << Modulus) | (1L << OBrace) | (1L << CBrace) | (1L << OBracket) | (1L << CBracket) | (1L << OParen) | (1L << CParen) | (1L << SColon) | (1L << Assign) | (1L << Comma) | (1L << QMark) | (1L << Colon) | (1L << Bool) | (1L << Number) | (1L << Identifier) | (1L << String) | (1L << Comment) | (1L << Space))) != 0)) {
				{
				{
				setState(2);
				((ParseContext)_localctx).t = matchWildcard();
				System.out.printf("text: %-7s  type: %s \n",
				           (((ParseContext)_localctx).t!=null?((ParseContext)_localctx).t.getText():null), tokenNames[(((ParseContext)_localctx).t!=null?((ParseContext)_localctx).t.getType():0)]);
				}
				}
				setState(8);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(9);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61\16\4\2\t\2\3\2"+
		"\3\2\7\2\7\n\2\f\2\16\2\n\13\2\3\2\3\2\3\2\2\2\3\2\2\2\2\r\2\b\3\2\2\2"+
		"\4\5\13\2\2\2\5\7\b\2\1\2\6\4\3\2\2\2\7\n\3\2\2\2\b\6\3\2\2\2\b\t\3\2"+
		"\2\2\t\13\3\2\2\2\n\b\3\2\2\2\13\f\7\2\2\3\f\3\3\2\2\2\3\b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}