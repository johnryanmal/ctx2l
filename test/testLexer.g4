lexer grammar testLexer;

DIGITS
  : [0-9]+
  ;

WS
  : [ \t\r\n\f]+
  ;

LITERAL__1
  : '**'
  ;

LITERAL__2
  : '('
  ;

LITERAL__3
  : ')'
  ;

LITERAL__4
  : '*'
  ;

LITERAL__5
  : '+'
  ;

LITERAL__6
  : '-'
  ;