lexer grammar jsonLexer;

STRING
  : '"' [a-zA-Z_0-9 ]* '"'
  ;

NUMBER
  : [0-9]
  | [1-9] [0-9]*
  ;

WS
  : [ \t\r\n\f]+
  ;

LITERAL__1
  : 'false'
  ;

LITERAL__2
  : 'null'
  ;

LITERAL__3
  : 'true'
  ;

LITERAL__4
  : ','
  ;

LITERAL__5
  : ':'
  ;

LITERAL__6
  : '['
  ;

LITERAL__7
  : ']'
  ;

LITERAL__8
  : '{'
  ;

LITERAL__9
  : '}'
  ;