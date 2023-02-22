parser grammar ctx2lParser;

options {
	tokenVocab = ctx2lLexer;
}

import ANTLRv4Parser;

program: def+ EOF;

def: ruleDef | tokenDef;
ruleDef: RULE_REF COLON OR ruleAlts;
tokenDef: TOKEN_REF COLON OR tokenAlts;

ruleSub: LPAREN OR? ruleAlts RPAREN;
tokenSub: LPAREN OR? tokenAlts RPAREN;
ruleAlts: ruleAlt (OR ruleAlt)*;
tokenAlts: tokenAlt (OR tokenAlt)*;
ruleAlt: ruleAtom+;
tokenAlt: tokenAtom+;

ruleAtom: ruleEbnf ebnfSuffix?;
ruleEbnf: ruleSub | ruleLiteral;
ruleLiteral: RULE_REF | TOKEN_REF | STRING_LITERAL;

tokenAtom: tokenEbnf ebnfSuffix?;
tokenEbnf: tokenSub | tokenLiteral;
tokenLiteral: TOKEN_REF | LEXER_CHAR_SET;
