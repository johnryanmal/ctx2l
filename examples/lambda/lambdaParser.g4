parser grammar lambdaParser;

options {
    tokenVocab = lambdaLexer;
}

calculus
  : V=terms EOF
  ;

terms
  : F=terms V=term #terms__1
  | V=term #terms__2
  ;

term
  : '(' V=terms ')' #term__1
  | LAMBDA X=SYMBOL DOT Y=terms #term__2
  | V=SYMBOL #term__3
  ;