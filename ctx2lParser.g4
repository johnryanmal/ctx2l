parser grammar ctx2lParser;

options {
	tokenVocab = ctx2lLexer;
	contextSuperClass = RuleContextWithAltNum;
}

@parser::header {
from RuleContextWithAltNum import RuleContextWithAltNum
}

import ANTLRv4Parser;

program: (ruleDef | tokenDef)+ EOF;
ruleDef: RULE_REF COLON OR? ruleAlts;
tokenDef: TOKEN_REF (DIRECT tokenCommands)? COLON OR? tokenAlts;
tokenCommands: lexerCommand (COMMA lexerCommand)*;

ruleSub: LPAREN OR? ruleAlts RPAREN;
tokenSub: LPAREN OR? tokenAlts RPAREN;
ruleAlts: ruleAlt (OR ruleAlt)*;
tokenAlts: tokenAlt (OR tokenAlt)*;
ruleAlt: ruleAtom+ (RARROW expr)?;
tokenAlt: tokenAtom+;

ruleAtom: label? ruleTerm ebnfSuffix?;
ruleTerm: ruleSub | ruleRef | ruleLiteral;
ruleRef: RULE_REF | TOKEN_REF;
ruleLiteral: STRING_LITERAL;

expr: DOLLAR? identifier call?;
call: LPAREN args? RPAREN;
args: expr (COMMA expr)* COMMA?;

tokenAtom: label? tokenTerm ebnfSuffix?;
tokenTerm: tokenSub | tokenRef | tokenLiteral;
tokenRef: TOKEN_REF;
tokenLiteral: STRING_LITERAL | LEXER_CHAR_SET;

label: identifier assign;
assign: ASSIGN | PLUS_ASSIGN;