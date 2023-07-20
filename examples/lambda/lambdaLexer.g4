lexer grammar lambdaLexer;

LAMBDA
  : '\\'
  | '\u03BB'
  ;

SYMBOL
  : [A-Za-z_]+
  ;

DOT
  : '.'
  ;

WS:
  ( [ \t\r\n\f]+
  ) -> skip;

LITERAL__1
  : '('
  ;

LITERAL__2
  : ')'
  ;