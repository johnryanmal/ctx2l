# Generated from examples/calculator/calculatorParser.g4 by ANTLR 4.12.0
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
        4,1,9,54,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,27,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,38,8,3,1,4,1,4,1,4,1,4,1,4,3,4,
        45,8,4,1,5,1,5,1,5,1,5,1,5,3,5,52,8,5,1,5,0,0,6,0,2,4,6,8,10,0,0,
        53,0,12,1,0,0,0,2,15,1,0,0,0,4,26,1,0,0,0,6,37,1,0,0,0,8,44,1,0,
        0,0,10,51,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,
        3,4,2,0,16,3,1,0,0,0,17,27,3,6,3,0,18,19,3,6,3,0,19,20,5,7,0,0,20,
        21,3,4,2,0,21,27,1,0,0,0,22,23,3,6,3,0,23,24,5,8,0,0,24,25,3,4,2,
        0,25,27,1,0,0,0,26,17,1,0,0,0,26,18,1,0,0,0,26,22,1,0,0,0,27,5,1,
        0,0,0,28,38,3,8,4,0,29,30,3,8,4,0,30,31,5,6,0,0,31,32,3,6,3,0,32,
        38,1,0,0,0,33,34,3,8,4,0,34,35,5,9,0,0,35,36,3,6,3,0,36,38,1,0,0,
        0,37,28,1,0,0,0,37,29,1,0,0,0,37,33,1,0,0,0,38,7,1,0,0,0,39,45,3,
        10,5,0,40,41,3,10,5,0,41,42,5,3,0,0,42,43,3,8,4,0,43,45,1,0,0,0,
        44,39,1,0,0,0,44,40,1,0,0,0,45,9,1,0,0,0,46,47,5,4,0,0,47,48,3,2,
        1,0,48,49,5,5,0,0,49,52,1,0,0,0,50,52,5,1,0,0,51,46,1,0,0,0,51,50,
        1,0,0,0,52,11,1,0,0,0,4,26,37,44,51
    ]

class calculatorParser ( Parser ):

    grammarFileName = "calculatorParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'**'", "'('", 
                     "')'", "'*'", "'+'", "'-'", "'/'" ]

    symbolicNames = [ "<INVALID>", "DIGITS", "WS", "LITERAL__1", "LITERAL__2", 
                      "LITERAL__3", "LITERAL__4", "LITERAL__5", "LITERAL__6", 
                      "LITERAL__7" ]

    RULE_calculation = 0
    RULE_expr = 1
    RULE_sum = 2
    RULE_prod = 3
    RULE_pow = 4
    RULE_value = 5

    ruleNames =  [ "calculation", "expr", "sum", "prod", "pow", "value" ]

    EOF = Token.EOF
    DIGITS=1
    WS=2
    LITERAL__1=3
    LITERAL__2=4
    LITERAL__3=5
    LITERAL__4=6
    LITERAL__5=7
    LITERAL__6=8
    LITERAL__7=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CalculationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.V = None # ExprContext

        def EOF(self):
            return self.getToken(calculatorParser.EOF, 0)

        def expr(self):
            return self.getTypedRuleContext(calculatorParser.ExprContext,0)


        def getRuleIndex(self):
            return calculatorParser.RULE_calculation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculation" ):
                return visitor.visitCalculation(self)
            else:
                return visitor.visitChildren(self)




    def calculation(self):

        localctx = calculatorParser.CalculationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_calculation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            localctx.V = self.expr()
            self.state = 13
            self.match(calculatorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.V = None # SumContext

        def sum_(self):
            return self.getTypedRuleContext(calculatorParser.SumContext,0)


        def getRuleIndex(self):
            return calculatorParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = calculatorParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            localctx.V = self.sum_()
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
            return calculatorParser.RULE_sum

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Sum__2Context(SumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.SumContext
            super().__init__(parser)
            self.L = None # ProdContext
            self.R = None # SumContext
            self.copyFrom(ctx)

        def LITERAL__5(self):
            return self.getToken(calculatorParser.LITERAL__5, 0)
        def prod(self):
            return self.getTypedRuleContext(calculatorParser.ProdContext,0)

        def sum_(self):
            return self.getTypedRuleContext(calculatorParser.SumContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum__2" ):
                return visitor.visitSum__2(self)
            else:
                return visitor.visitChildren(self)


    class Sum__1Context(SumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.SumContext
            super().__init__(parser)
            self.V = None # ProdContext
            self.copyFrom(ctx)

        def prod(self):
            return self.getTypedRuleContext(calculatorParser.ProdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum__1" ):
                return visitor.visitSum__1(self)
            else:
                return visitor.visitChildren(self)


    class Sum__3Context(SumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.SumContext
            super().__init__(parser)
            self.L = None # ProdContext
            self.R = None # SumContext
            self.copyFrom(ctx)

        def LITERAL__6(self):
            return self.getToken(calculatorParser.LITERAL__6, 0)
        def prod(self):
            return self.getTypedRuleContext(calculatorParser.ProdContext,0)

        def sum_(self):
            return self.getTypedRuleContext(calculatorParser.SumContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum__3" ):
                return visitor.visitSum__3(self)
            else:
                return visitor.visitChildren(self)



    def sum_(self):

        localctx = calculatorParser.SumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sum)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = calculatorParser.Sum__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                localctx.V = self.prod()
                pass

            elif la_ == 2:
                localctx = calculatorParser.Sum__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                localctx.L = self.prod()
                self.state = 19
                self.match(calculatorParser.LITERAL__5)
                self.state = 20
                localctx.R = self.sum_()
                pass

            elif la_ == 3:
                localctx = calculatorParser.Sum__3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                localctx.L = self.prod()
                self.state = 23
                self.match(calculatorParser.LITERAL__6)
                self.state = 24
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
            return calculatorParser.RULE_prod

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Prod__3Context(ProdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.ProdContext
            super().__init__(parser)
            self.L = None # PowContext
            self.R = None # ProdContext
            self.copyFrom(ctx)

        def LITERAL__7(self):
            return self.getToken(calculatorParser.LITERAL__7, 0)
        def pow_(self):
            return self.getTypedRuleContext(calculatorParser.PowContext,0)

        def prod(self):
            return self.getTypedRuleContext(calculatorParser.ProdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProd__3" ):
                return visitor.visitProd__3(self)
            else:
                return visitor.visitChildren(self)


    class Prod__2Context(ProdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.ProdContext
            super().__init__(parser)
            self.L = None # PowContext
            self.R = None # ProdContext
            self.copyFrom(ctx)

        def LITERAL__4(self):
            return self.getToken(calculatorParser.LITERAL__4, 0)
        def pow_(self):
            return self.getTypedRuleContext(calculatorParser.PowContext,0)

        def prod(self):
            return self.getTypedRuleContext(calculatorParser.ProdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProd__2" ):
                return visitor.visitProd__2(self)
            else:
                return visitor.visitChildren(self)


    class Prod__1Context(ProdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.ProdContext
            super().__init__(parser)
            self.V = None # PowContext
            self.copyFrom(ctx)

        def pow_(self):
            return self.getTypedRuleContext(calculatorParser.PowContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProd__1" ):
                return visitor.visitProd__1(self)
            else:
                return visitor.visitChildren(self)



    def prod(self):

        localctx = calculatorParser.ProdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_prod)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = calculatorParser.Prod__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                localctx.V = self.pow_()
                pass

            elif la_ == 2:
                localctx = calculatorParser.Prod__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                localctx.L = self.pow_()
                self.state = 30
                self.match(calculatorParser.LITERAL__4)
                self.state = 31
                localctx.R = self.prod()
                pass

            elif la_ == 3:
                localctx = calculatorParser.Prod__3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                localctx.L = self.pow_()
                self.state = 34
                self.match(calculatorParser.LITERAL__7)
                self.state = 35
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
            return calculatorParser.RULE_pow

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Pow__2Context(PowContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.PowContext
            super().__init__(parser)
            self.L = None # ValueContext
            self.R = None # PowContext
            self.copyFrom(ctx)

        def LITERAL__1(self):
            return self.getToken(calculatorParser.LITERAL__1, 0)
        def value(self):
            return self.getTypedRuleContext(calculatorParser.ValueContext,0)

        def pow_(self):
            return self.getTypedRuleContext(calculatorParser.PowContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow__2" ):
                return visitor.visitPow__2(self)
            else:
                return visitor.visitChildren(self)


    class Pow__1Context(PowContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.PowContext
            super().__init__(parser)
            self.V = None # ValueContext
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(calculatorParser.ValueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow__1" ):
                return visitor.visitPow__1(self)
            else:
                return visitor.visitChildren(self)



    def pow_(self):

        localctx = calculatorParser.PowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pow)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = calculatorParser.Pow__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                localctx.V = self.value()
                pass

            elif la_ == 2:
                localctx = calculatorParser.Pow__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                localctx.L = self.value()
                self.state = 41
                self.match(calculatorParser.LITERAL__1)
                self.state = 42
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
            return calculatorParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Value__1Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.ValueContext
            super().__init__(parser)
            self.V = None # ExprContext
            self.copyFrom(ctx)

        def LITERAL__2(self):
            return self.getToken(calculatorParser.LITERAL__2, 0)
        def LITERAL__3(self):
            return self.getToken(calculatorParser.LITERAL__3, 0)
        def expr(self):
            return self.getTypedRuleContext(calculatorParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__1" ):
                return visitor.visitValue__1(self)
            else:
                return visitor.visitChildren(self)


    class Value__2Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculatorParser.ValueContext
            super().__init__(parser)
            self.V = None # Token
            self.copyFrom(ctx)

        def DIGITS(self):
            return self.getToken(calculatorParser.DIGITS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__2" ):
                return visitor.visitValue__2(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = calculatorParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = calculatorParser.Value__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(calculatorParser.LITERAL__2)
                self.state = 47
                localctx.V = self.expr()
                self.state = 48
                self.match(calculatorParser.LITERAL__3)
                pass
            elif token in [1]:
                localctx = calculatorParser.Value__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                localctx.V = self.match(calculatorParser.DIGITS)
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





