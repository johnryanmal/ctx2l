parser grammar calculatorParser;

options {
    tokenVocab = calculatorLexer;
}

expr
  : ws V=sum ws
  ;

sum
  : V=prod #sum__1
  | L=prod ws '+' ws R=sum #sum__2
  | L=prod ws '-' ws R=sum #sum__3
  ;

prod
  : V=pow #prod__1
  | L=pow ws '*' ws R=prod #prod__2
  | L=pow ws '/' ws R=prod #prod__3
  ;

pow
  : V=value #pow__1
  | L=value ws '**' ws R=pow #pow__2
  ;

value
  : '(' ws V=expr ws ')' #value__1
  | V=DIGITS #value__2
  ;

ws
  : WS?
  ;