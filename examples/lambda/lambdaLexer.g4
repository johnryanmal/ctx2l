lexer grammar lambdaLexer;

LAMBDA
  : '\\'
  | '\u03BB'
  ;

SYMBOL
  : [A-Za-z_] [A-Za-z0-9_]*
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