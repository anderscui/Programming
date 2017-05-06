grammar CSV;

file returns [List<List<String>> data]
@init { $data = new ArrayList<List<String>>(); }
  : (row { $data.add($row.list); })+;

row returns [List<String> list]
@init { $list = new ArrayList<String>(); }
  : first=value { $list.add($first.val); } (Comma more=value { $list.add($more.val); })* (LineBreak | EOF);

value returns [String val]
  : SimpleValue { $val = $SimpleValue.text; }
  | QuotedValue {
      $val = $QuotedValue.text;
      $val = $val.substring(1, $val.length()-1);
      $val = $val.replace("\"\"", "\"");
    }
  ;

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
