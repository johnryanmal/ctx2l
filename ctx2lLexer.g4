lexer grammar ctx2lLexer;

options {
	superClass = ctx2lLexerAdaptor;
}

import ANTLRv4Lexer;

// overwrite comments

fragment BlockComment
	: '!--' .*? ('---' ~ [\r\n]* | EOF)
	;

fragment DocComment
	: '?--' .*? ('---' ~ [\r\n]* | EOF)
	;
   
fragment LineComment
	: '--' ~ [\r\n]*
	;

// overwrite tokens

LBRACE: LBrace;
RBRACE: RBrace;