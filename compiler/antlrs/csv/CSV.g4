grammar CSV;

file: row+;

row: value (Comma value)* LineBreak;

value: SimpleValue | QuotedValue;

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
