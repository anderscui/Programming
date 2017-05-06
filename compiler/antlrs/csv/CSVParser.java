// Generated from CSV.g4 by ANTLR 4.7
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CSVParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Comma=1, LineBreak=2, SimpleValue=3, QuotedValue=4;
	public static final int
		RULE_file = 0, RULE_row = 1, RULE_value = 2;
	public static final String[] ruleNames = {
		"file", "row", "value"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "','"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "Comma", "LineBreak", "SimpleValue", "QuotedValue"
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
	public String getGrammarFileName() { return "CSV.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CSVParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class FileContext extends ParserRuleContext {
		public List<List<String>> data;
		public RowContext row;
		public List<RowContext> row() {
			return getRuleContexts(RowContext.class);
		}
		public RowContext row(int i) {
			return getRuleContext(RowContext.class,i);
		}
		public FileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVListener ) ((CSVListener)listener).enterFile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVListener ) ((CSVListener)listener).exitFile(this);
		}
	}

	public final FileContext file() throws RecognitionException {
		FileContext _localctx = new FileContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_file);
		 ((FileContext)_localctx).data =  new ArrayList<List<String>>(); 
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(6);
				((FileContext)_localctx).row = row();
				 _localctx.data.add(((FileContext)_localctx).row.list); 
				}
				}
				setState(11); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==SimpleValue || _la==QuotedValue );
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

	public static class RowContext extends ParserRuleContext {
		public List<String> list;
		public ValueContext first;
		public ValueContext more;
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public TerminalNode LineBreak() { return getToken(CSVParser.LineBreak, 0); }
		public TerminalNode EOF() { return getToken(CSVParser.EOF, 0); }
		public List<TerminalNode> Comma() { return getTokens(CSVParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(CSVParser.Comma, i);
		}
		public RowContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_row; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVListener ) ((CSVListener)listener).enterRow(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVListener ) ((CSVListener)listener).exitRow(this);
		}
	}

	public final RowContext row() throws RecognitionException {
		RowContext _localctx = new RowContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_row);
		 ((RowContext)_localctx).list =  new ArrayList<String>(); 
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			((RowContext)_localctx).first = value();
			 _localctx.list.add(((RowContext)_localctx).first.val); 
			setState(21);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(15);
				match(Comma);
				setState(16);
				((RowContext)_localctx).more = value();
				 _localctx.list.add(((RowContext)_localctx).more.val); 
				}
				}
				setState(23);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(24);
			_la = _input.LA(1);
			if ( !(_la==EOF || _la==LineBreak) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class ValueContext extends ParserRuleContext {
		public String val;
		public Token SimpleValue;
		public Token QuotedValue;
		public TerminalNode SimpleValue() { return getToken(CSVParser.SimpleValue, 0); }
		public TerminalNode QuotedValue() { return getToken(CSVParser.QuotedValue, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVListener ) ((CSVListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVListener ) ((CSVListener)listener).exitValue(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_value);
		try {
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SimpleValue:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				((ValueContext)_localctx).SimpleValue = match(SimpleValue);
				 ((ValueContext)_localctx).val =  (((ValueContext)_localctx).SimpleValue!=null?((ValueContext)_localctx).SimpleValue.getText():null); 
				}
				break;
			case QuotedValue:
				enterOuterAlt(_localctx, 2);
				{
				setState(28);
				((ValueContext)_localctx).QuotedValue = match(QuotedValue);

				      ((ValueContext)_localctx).val =  (((ValueContext)_localctx).QuotedValue!=null?((ValueContext)_localctx).QuotedValue.getText():null);
				      ((ValueContext)_localctx).val =  _localctx.val.substring(1, _localctx.val.length()-1);
				      ((ValueContext)_localctx).val =  _localctx.val.replace("\"\"", "\"");
				    
				}
				break;
			default:
				throw new NoViableAltException(this);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6#\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\3\2\3\2\3\2\6\2\f\n\2\r\2\16\2\r\3\3\3\3\3\3\3\3\3\3\3\3\7"+
		"\3\26\n\3\f\3\16\3\31\13\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4!\n\4\3\4\2\2\5"+
		"\2\4\6\2\3\3\3\4\4\2\"\2\13\3\2\2\2\4\17\3\2\2\2\6 \3\2\2\2\b\t\5\4\3"+
		"\2\t\n\b\2\1\2\n\f\3\2\2\2\13\b\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16"+
		"\3\2\2\2\16\3\3\2\2\2\17\20\5\6\4\2\20\27\b\3\1\2\21\22\7\3\2\2\22\23"+
		"\5\6\4\2\23\24\b\3\1\2\24\26\3\2\2\2\25\21\3\2\2\2\26\31\3\2\2\2\27\25"+
		"\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32\33\t\2\2\2\33\5"+
		"\3\2\2\2\34\35\7\5\2\2\35!\b\4\1\2\36\37\7\6\2\2\37!\b\4\1\2 \34\3\2\2"+
		"\2 \36\3\2\2\2!\7\3\2\2\2\5\r\27 ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}