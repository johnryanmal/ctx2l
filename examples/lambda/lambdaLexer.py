# Generated from examples/lambda/lambdaLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,35,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,1,2,1,3,4,3,26,8,3,
        11,3,12,3,27,1,3,1,3,1,4,1,4,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,
        6,1,0,4,2,0,92,92,955,955,3,0,65,90,95,95,97,122,4,0,48,57,65,90,
        95,95,97,122,3,0,9,10,12,13,32,32,36,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,15,1,
        0,0,0,5,22,1,0,0,0,7,25,1,0,0,0,9,31,1,0,0,0,11,33,1,0,0,0,13,14,
        7,0,0,0,14,2,1,0,0,0,15,19,7,1,0,0,16,18,7,2,0,0,17,16,1,0,0,0,18,
        21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,4,1,0,0,0,21,19,1,0,0,
        0,22,23,5,46,0,0,23,6,1,0,0,0,24,26,7,3,0,0,25,24,1,0,0,0,26,27,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,6,3,0,0,
        30,8,1,0,0,0,31,32,5,40,0,0,32,10,1,0,0,0,33,34,5,41,0,0,34,12,1,
        0,0,0,3,0,19,27,1,6,0,0
    ]

class lambdaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LAMBDA = 1
    SYMBOL = 2
    DOT = 3
    WS = 4
    LITERAL__1 = 5
    LITERAL__2 = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "LAMBDA", "SYMBOL", "DOT", "WS", "LITERAL__1", "LITERAL__2" ]

    ruleNames = [ "LAMBDA", "SYMBOL", "DOT", "WS", "LITERAL__1", "LITERAL__2" ]

    grammarFileName = "lambdaLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


