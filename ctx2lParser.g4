parser grammar ctx2lParser;

options {
	tokenVocab = ctx2lLexer;
}

import ANTLRv4Parser;

program: (ruleDef | tokenDef)+ EOF;
ruleDef: RULE_REF COLON OR ruleAlts;
tokenDef: TOKEN_REF COLON OR tokenAlts;

ruleSub: LPAREN OR? ruleAlts RPAREN;
tokenSub: LPAREN OR? tokenAlts RPAREN;
ruleAlts: ruleAlt (OR ruleAlt)*;
tokenAlts: tokenAlt (OR tokenAlt)*;
ruleAlt: ruleAtom+;
tokenAlt: tokenAtom+;

ruleAtom: ruleEbnf ebnfSuffix?;
ruleEbnf: ruleSub | ruleRef | ruleLiteral;
ruleRef: RULE_REF | TOKEN_REF;
ruleLiteral: STRING_LITERAL;

tokenAtom: tokenEbnf ebnfSuffix?;
tokenEbnf: tokenSub | tokenRef | tokenLiteral;
tokenRef: TOKEN_REF;
tokenLiteral: STRING_LITERAL | LEXER_CHAR_SET;
