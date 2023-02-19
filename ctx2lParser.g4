parser grammar ctx2lParser;

options {
	tokenVocab = ctx2lLexer;
}

import ANTLRv4Parser;

program: grammarSpec;