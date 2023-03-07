parser grammar calculatorParser;

options {
    tokenVocab = calculatorLexer;
}

expr
  : V=sum
  ;

sum
  : V=prod #sum__1
  | L=prod '+' R=sum #sum__2
  | L=prod '-' R=sum #sum__3
  ;

prod
  : V=pow #prod__1
  | L=pow '*' R=prod #prod__2
  | L=pow '/' R=prod #prod__3
  ;

pow
  : V=value #pow__1
  | L=value '**' R=pow #pow__2
  ;

value
  : '(' V=expr ')' #value__1
  | V=DIGITS #value__2
  ;