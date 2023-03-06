parser grammar jsonParser;

options {
    tokenVocab = jsonLexer;
}

json
  : V=element EOF
  ;

value
  : V=object #value__1
  | V=array #value__2
  | V=STRING #value__3
  | V=NUMBER #value__4
  | V='true' #value__5
  | V='false' #value__6
  | V='null' #value__7
  ;

object
  : '{' ws '}' #object__1
  | '{' V=members '}' #object__2
  ;

members
  : VS+=member ( ',' VS+=member )*
  ;

member
  : ws K=STRING ws ':' V=element
  ;

array
  : '[' ws ']' #array__1
  | '[' V=elements ']' #array__2
  ;

elements
  : V+=element ( ',' V+=element )*
  ;

element
  : ws V=value ws
  ;

ws
  : WS?
  ;