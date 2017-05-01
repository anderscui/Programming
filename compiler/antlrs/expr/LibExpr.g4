grammar Expr;
import CommonLexerRules; // includes all rules from CommonLexerRules.g4

/** the start rule; begin parisng here */
prog: stat+;

stat: expr NEWLINE
    | ID '=' expr NEWLINE
    | NEWLINE
    ;

expr: expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | INT
    | ID
    | '(' expr ')'
    ;
