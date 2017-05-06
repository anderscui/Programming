lexer grammar CSVLexer;

// lexer rules MUST start with a capital
Comma: ',';

LineBreak
  : '\r'? '\n'
  | '\r'
  ;

SimpleValue
  : ~(',' | '\r' | '\n' | '"')+
  ;

QuotedValue
  : '"' ('""' | ~'"')* '"'
  ;

