# Generated from examples/calculator/calculatorLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,46,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,4,0,21,8,0,11,0,12,0,22,1,1,4,1,26,8,1,
        11,1,12,1,27,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,
        1,7,1,7,1,8,1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,
        0,2,1,0,48,57,3,0,9,10,12,13,32,32,47,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,
        1,0,0,0,0,17,1,0,0,0,1,20,1,0,0,0,3,25,1,0,0,0,5,31,1,0,0,0,7,34,
        1,0,0,0,9,36,1,0,0,0,11,38,1,0,0,0,13,40,1,0,0,0,15,42,1,0,0,0,17,
        44,1,0,0,0,19,21,7,0,0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,
        0,22,23,1,0,0,0,23,2,1,0,0,0,24,26,7,1,0,0,25,24,1,0,0,0,26,27,1,
        0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,6,1,0,0,30,
        4,1,0,0,0,31,32,5,42,0,0,32,33,5,42,0,0,33,6,1,0,0,0,34,35,5,40,
        0,0,35,8,1,0,0,0,36,37,5,41,0,0,37,10,1,0,0,0,38,39,5,42,0,0,39,
        12,1,0,0,0,40,41,5,43,0,0,41,14,1,0,0,0,42,43,5,45,0,0,43,16,1,0,
        0,0,44,45,5,47,0,0,45,18,1,0,0,0,3,0,22,27,1,6,0,0
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
    LITERAL__7 = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'**'", "'('", "')'", "'*'", "'+'", "'-'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "DIGITS", "WS", "LITERAL__1", "LITERAL__2", "LITERAL__3", "LITERAL__4", 
            "LITERAL__5", "LITERAL__6", "LITERAL__7" ]

    ruleNames = [ "DIGITS", "WS", "LITERAL__1", "LITERAL__2", "LITERAL__3", 
                  "LITERAL__4", "LITERAL__5", "LITERAL__6", "LITERAL__7" ]

    grammarFileName = "calculatorLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


