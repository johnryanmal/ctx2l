# Generated from test//testParser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,69,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,46,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,55,8,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,64,8,4,1,5,3,5,67,8,5,1,5,0,0,6,0,2,4,6,8,10,0,0,
        69,0,12,1,0,0,0,2,30,1,0,0,0,4,45,1,0,0,0,6,54,1,0,0,0,8,63,1,0,
        0,0,10,66,1,0,0,0,12,13,3,10,5,0,13,14,3,2,1,0,14,15,3,10,5,0,15,
        16,5,0,0,1,16,1,1,0,0,0,17,31,3,4,2,0,18,19,3,4,2,0,19,20,3,10,5,
        0,20,21,5,7,0,0,21,22,3,10,5,0,22,23,3,2,1,0,23,31,1,0,0,0,24,25,
        3,4,2,0,25,26,3,10,5,0,26,27,5,8,0,0,27,28,3,10,5,0,28,29,3,2,1,
        0,29,31,1,0,0,0,30,17,1,0,0,0,30,18,1,0,0,0,30,24,1,0,0,0,31,3,1,
        0,0,0,32,46,3,6,3,0,33,34,3,6,3,0,34,35,3,10,5,0,35,36,5,6,0,0,36,
        37,3,10,5,0,37,38,3,4,2,0,38,46,1,0,0,0,39,40,3,6,3,0,40,41,3,10,
        5,0,41,42,5,8,0,0,42,43,3,10,5,0,43,44,3,4,2,0,44,46,1,0,0,0,45,
        32,1,0,0,0,45,33,1,0,0,0,45,39,1,0,0,0,46,5,1,0,0,0,47,55,3,8,4,
        0,48,49,3,8,4,0,49,50,3,10,5,0,50,51,5,3,0,0,51,52,3,10,5,0,52,53,
        3,6,3,0,53,55,1,0,0,0,54,47,1,0,0,0,54,48,1,0,0,0,55,7,1,0,0,0,56,
        57,5,4,0,0,57,58,5,2,0,0,58,59,3,0,0,0,59,60,5,2,0,0,60,61,5,5,0,
        0,61,64,1,0,0,0,62,64,5,1,0,0,63,56,1,0,0,0,63,62,1,0,0,0,64,9,1,
        0,0,0,65,67,5,2,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,11,1,0,0,0,5,
        30,45,54,63,66
    ]

class testParser ( Parser ):

    grammarFileName = "testParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'**'", "'('", 
                     "')'", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "DIGITS", "WS", "LITERAL__1", "LITERAL__2", 
                      "LITERAL__3", "LITERAL__4", "LITERAL__5", "LITERAL__6" ]

    RULE_expr = 0
    RULE_sum = 1
    RULE_prod = 2
    RULE_pow = 3
    RULE_value = 4
    RULE_ws = 5

    ruleNames =  [ "expr", "sum", "prod", "pow", "value", "ws" ]

    EOF = Token.EOF
    DIGITS=1
    WS=2
    LITERAL__1=3
    LITERAL__2=4
    LITERAL__3=5
    LITERAL__4=6
    LITERAL__5=7
    LITERAL__6=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.V = None # SumContext

        def ws(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.WsContext)
            else:
                return self.getTypedRuleContext(testParser.WsContext,i)


        def EOF(self):
            return self.getToken(testParser.EOF, 0)

        def sum_(self):
            return self.getTypedRuleContext(testParser.SumContext,0)


        def getRuleIndex(self):
            return testParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = testParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.ws()
            self.state = 13
            localctx.V = self.sum_()
            self.state = 14
            self.ws()
            self.state = 15
            self.match(testParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_sum

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Sum__2Context(SumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.SumContext
            super().__init__(parser)
            self.L = None # ProdContext
            self.R = None # SumContext
            self.copyFrom(ctx)

        def ws(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.WsContext)
            else:
                return self.getTypedRuleContext(testParser.WsContext,i)

        def LITERAL__5(self):
            return self.getToken(testParser.LITERAL__5, 0)
        def prod(self):
            return self.getTypedRuleContext(testParser.ProdContext,0)

        def sum_(self):
            return self.getTypedRuleContext(testParser.SumContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum__2" ):
                return visitor.visitSum__2(self)
            else:
                return visitor.visitChildren(self)


    class Sum__1Context(SumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.SumContext
            super().__init__(parser)
            self.V = None # ProdContext
            self.copyFrom(ctx)

        def prod(self):
            return self.getTypedRuleContext(testParser.ProdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum__1" ):
                return visitor.visitSum__1(self)
            else:
                return visitor.visitChildren(self)


    class Sum__3Context(SumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.SumContext
            super().__init__(parser)
            self.L = None # ProdContext
            self.R = None # SumContext
            self.copyFrom(ctx)

        def ws(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.WsContext)
            else:
                return self.getTypedRuleContext(testParser.WsContext,i)

        def LITERAL__6(self):
            return self.getToken(testParser.LITERAL__6, 0)
        def prod(self):
            return self.getTypedRuleContext(testParser.ProdContext,0)

        def sum_(self):
            return self.getTypedRuleContext(testParser.SumContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum__3" ):
                return visitor.visitSum__3(self)
            else:
                return visitor.visitChildren(self)



    def sum_(self):

        localctx = testParser.SumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sum)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = testParser.Sum__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                localctx.V = self.prod()
                pass

            elif la_ == 2:
                localctx = testParser.Sum__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                localctx.L = self.prod()
                self.state = 19
                self.ws()
                self.state = 20
                self.match(testParser.LITERAL__5)
                self.state = 21
                self.ws()
                self.state = 22
                localctx.R = self.sum_()
                pass

            elif la_ == 3:
                localctx = testParser.Sum__3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                localctx.L = self.prod()
                self.state = 25
                self.ws()
                self.state = 26
                self.match(testParser.LITERAL__6)
                self.state = 27
                self.ws()
                self.state = 28
                localctx.R = self.sum_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_prod

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Prod__3Context(ProdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ProdContext
            super().__init__(parser)
            self.L = None # PowContext
            self.R = None # ProdContext
            self.copyFrom(ctx)

        def ws(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.WsContext)
            else:
                return self.getTypedRuleContext(testParser.WsContext,i)

        def LITERAL__6(self):
            return self.getToken(testParser.LITERAL__6, 0)
        def pow_(self):
            return self.getTypedRuleContext(testParser.PowContext,0)

        def prod(self):
            return self.getTypedRuleContext(testParser.ProdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProd__3" ):
                return visitor.visitProd__3(self)
            else:
                return visitor.visitChildren(self)


    class Prod__2Context(ProdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ProdContext
            super().__init__(parser)
            self.L = None # PowContext
            self.R = None # ProdContext
            self.copyFrom(ctx)

        def ws(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.WsContext)
            else:
                return self.getTypedRuleContext(testParser.WsContext,i)

        def LITERAL__4(self):
            return self.getToken(testParser.LITERAL__4, 0)
        def pow_(self):
            return self.getTypedRuleContext(testParser.PowContext,0)

        def prod(self):
            return self.getTypedRuleContext(testParser.ProdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProd__2" ):
                return visitor.visitProd__2(self)
            else:
                return visitor.visitChildren(self)


    class Prod__1Context(ProdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ProdContext
            super().__init__(parser)
            self.V = None # PowContext
            self.copyFrom(ctx)

        def pow_(self):
            return self.getTypedRuleContext(testParser.PowContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProd__1" ):
                return visitor.visitProd__1(self)
            else:
                return visitor.visitChildren(self)



    def prod(self):

        localctx = testParser.ProdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_prod)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = testParser.Prod__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                localctx.V = self.pow_()
                pass

            elif la_ == 2:
                localctx = testParser.Prod__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                localctx.L = self.pow_()
                self.state = 34
                self.ws()
                self.state = 35
                self.match(testParser.LITERAL__4)
                self.state = 36
                self.ws()
                self.state = 37
                localctx.R = self.prod()
                pass

            elif la_ == 3:
                localctx = testParser.Prod__3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                localctx.L = self.pow_()
                self.state = 40
                self.ws()
                self.state = 41
                self.match(testParser.LITERAL__6)
                self.state = 42
                self.ws()
                self.state = 43
                localctx.R = self.prod()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_pow

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Pow__2Context(PowContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.PowContext
            super().__init__(parser)
            self.L = None # ValueContext
            self.R = None # PowContext
            self.copyFrom(ctx)

        def ws(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.WsContext)
            else:
                return self.getTypedRuleContext(testParser.WsContext,i)

        def LITERAL__1(self):
            return self.getToken(testParser.LITERAL__1, 0)
        def value(self):
            return self.getTypedRuleContext(testParser.ValueContext,0)

        def pow_(self):
            return self.getTypedRuleContext(testParser.PowContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow__2" ):
                return visitor.visitPow__2(self)
            else:
                return visitor.visitChildren(self)


    class Pow__1Context(PowContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.PowContext
            super().__init__(parser)
            self.V = None # ValueContext
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(testParser.ValueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow__1" ):
                return visitor.visitPow__1(self)
            else:
                return visitor.visitChildren(self)



    def pow_(self):

        localctx = testParser.PowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pow)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = testParser.Pow__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                localctx.V = self.value()
                pass

            elif la_ == 2:
                localctx = testParser.Pow__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                localctx.L = self.value()
                self.state = 49
                self.ws()
                self.state = 50
                self.match(testParser.LITERAL__1)
                self.state = 51
                self.ws()
                self.state = 52
                localctx.R = self.pow_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Value__1Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ValueContext
            super().__init__(parser)
            self.V = None # ExprContext
            self.copyFrom(ctx)

        def LITERAL__2(self):
            return self.getToken(testParser.LITERAL__2, 0)
        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(testParser.WS)
            else:
                return self.getToken(testParser.WS, i)
        def LITERAL__3(self):
            return self.getToken(testParser.LITERAL__3, 0)
        def expr(self):
            return self.getTypedRuleContext(testParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__1" ):
                return visitor.visitValue__1(self)
            else:
                return visitor.visitChildren(self)


    class Value__2Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ValueContext
            super().__init__(parser)
            self.V = None # Token
            self.copyFrom(ctx)

        def DIGITS(self):
            return self.getToken(testParser.DIGITS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__2" ):
                return visitor.visitValue__2(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = testParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = testParser.Value__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(testParser.LITERAL__2)
                self.state = 57
                self.match(testParser.WS)
                self.state = 58
                localctx.V = self.expr()
                self.state = 59
                self.match(testParser.WS)
                self.state = 60
                self.match(testParser.LITERAL__3)
                pass
            elif token in [1]:
                localctx = testParser.Value__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                localctx.V = self.match(testParser.DIGITS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self):
            return self.getToken(testParser.WS, 0)

        def getRuleIndex(self):
            return testParser.RULE_ws

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWs" ):
                return visitor.visitWs(self)
            else:
                return visitor.visitChildren(self)




    def ws(self):

        localctx = testParser.WsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ws)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 65
                self.match(testParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





