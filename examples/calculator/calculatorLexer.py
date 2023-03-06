# Generated from examples/calculator/calculatorLexer.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,40,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,4,0,19,8,0,11,0,12,0,20,1,1,4,1,24,8,1,11,1,12,
        1,25,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,0,0,8,1,
        1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,2,1,0,48,57,3,0,9,10,12,13,
        32,32,41,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,18,1,0,0,0,3,23,1,0,
        0,0,5,27,1,0,0,0,7,30,1,0,0,0,9,32,1,0,0,0,11,34,1,0,0,0,13,36,1,
        0,0,0,15,38,1,0,0,0,17,19,7,0,0,0,18,17,1,0,0,0,19,20,1,0,0,0,20,
        18,1,0,0,0,20,21,1,0,0,0,21,2,1,0,0,0,22,24,7,1,0,0,23,22,1,0,0,
        0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,4,1,0,0,0,27,28,5,
        42,0,0,28,29,5,42,0,0,29,6,1,0,0,0,30,31,5,40,0,0,31,8,1,0,0,0,32,
        33,5,41,0,0,33,10,1,0,0,0,34,35,5,42,0,0,35,12,1,0,0,0,36,37,5,43,
        0,0,37,14,1,0,0,0,38,39,5,45,0,0,39,16,1,0,0,0,3,0,20,25,0
    ]

class calculatorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DIGITS = 1
    WS = 2
    LITERAL__1 = 3
    LITERAL__2 = 4
    LITERAL__3 = 5
    LITERAL__4 = 6
    LITERAL__5 = 7
    LITERAL__6 = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'**'", "'('", "')'", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "DIGITS", "WS", "LITERAL__1", "LITERAL__2", "LITERAL__3", "LITERAL__4", 
            "LITERAL__5", "LITERAL__6" ]

    ruleNames = [ "DIGITS", "WS", "LITERAL__1", "LITERAL__2", "LITERAL__3", 
                  "LITERAL__4", "LITERAL__5", "LITERAL__6" ]

    grammarFileName = "calculatorLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


