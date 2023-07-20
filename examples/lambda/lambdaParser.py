# Generated from examples/lambda/lambdaParser.g4 by ANTLR 4.13.0
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
        4,1,6,31,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        5,1,15,8,1,10,1,12,1,18,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,29,8,2,1,2,0,1,2,3,0,2,4,0,0,30,0,6,1,0,0,0,2,9,1,0,0,0,4,28,
        1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,6,1,-1,0,10,11,
        3,4,2,0,11,16,1,0,0,0,12,13,10,2,0,0,13,15,3,4,2,0,14,12,1,0,0,0,
        15,18,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,3,1,0,0,0,18,16,1,0,
        0,0,19,20,5,5,0,0,20,21,3,2,1,0,21,22,5,6,0,0,22,29,1,0,0,0,23,24,
        5,1,0,0,24,25,5,2,0,0,25,26,5,3,0,0,26,29,3,2,1,0,27,29,5,2,0,0,
        28,19,1,0,0,0,28,23,1,0,0,0,28,27,1,0,0,0,29,5,1,0,0,0,2,16,28
    ]

class lambdaParser ( Parser ):

    grammarFileName = "lambdaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'.'", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "LAMBDA", "SYMBOL", "DOT", "WS", "LITERAL__1", 
                      "LITERAL__2" ]

    RULE_calculus = 0
    RULE_terms = 1
    RULE_term = 2

    ruleNames =  [ "calculus", "terms", "term" ]

    EOF = Token.EOF
    LAMBDA=1
    SYMBOL=2
    DOT=3
    WS=4
    LITERAL__1=5
    LITERAL__2=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CalculusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.V = None # TermsContext

        def EOF(self):
            return self.getToken(lambdaParser.EOF, 0)

        def terms(self):
            return self.getTypedRuleContext(lambdaParser.TermsContext,0)


        def getRuleIndex(self):
            return lambdaParser.RULE_calculus

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculus" ):
                return visitor.visitCalculus(self)
            else:
                return visitor.visitChildren(self)




    def calculus(self):

        localctx = lambdaParser.CalculusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_calculus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            localctx.V = self.terms(0)
            self.state = 7
            self.match(lambdaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lambdaParser.RULE_terms

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Terms__2Context(TermsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermsContext
            super().__init__(parser)
            self.V = None # TermContext
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(lambdaParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerms__2" ):
                return visitor.visitTerms__2(self)
            else:
                return visitor.visitChildren(self)


    class Terms__1Context(TermsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermsContext
            super().__init__(parser)
            self.F = None # TermsContext
            self.V = None # TermContext
            self.copyFrom(ctx)

        def terms(self):
            return self.getTypedRuleContext(lambdaParser.TermsContext,0)

        def term(self):
            return self.getTypedRuleContext(lambdaParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerms__1" ):
                return visitor.visitTerms__1(self)
            else:
                return visitor.visitChildren(self)



    def terms(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lambdaParser.TermsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_terms, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = lambdaParser.Terms__2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 10
            localctx.V = self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 16
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = lambdaParser.Terms__1Context(self, lambdaParser.TermsContext(self, _parentctx, _parentState))
                    localctx.F = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terms)
                    self.state = 12
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 13
                    localctx.V = self.term() 
                self.state = 18
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lambdaParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Term__1Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermContext
            super().__init__(parser)
            self.V = None # TermsContext
            self.copyFrom(ctx)

        def LITERAL__1(self):
            return self.getToken(lambdaParser.LITERAL__1, 0)
        def LITERAL__2(self):
            return self.getToken(lambdaParser.LITERAL__2, 0)
        def terms(self):
            return self.getTypedRuleContext(lambdaParser.TermsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm__1" ):
                return visitor.visitTerm__1(self)
            else:
                return visitor.visitChildren(self)


    class Term__3Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermContext
            super().__init__(parser)
            self.V = None # Token
            self.copyFrom(ctx)

        def SYMBOL(self):
            return self.getToken(lambdaParser.SYMBOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm__3" ):
                return visitor.visitTerm__3(self)
            else:
                return visitor.visitChildren(self)


    class Term__2Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermContext
            super().__init__(parser)
            self.X = None # Token
            self.Y = None # TermsContext
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(lambdaParser.LAMBDA, 0)
        def DOT(self):
            return self.getToken(lambdaParser.DOT, 0)
        def SYMBOL(self):
            return self.getToken(lambdaParser.SYMBOL, 0)
        def terms(self):
            return self.getTypedRuleContext(lambdaParser.TermsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm__2" ):
                return visitor.visitTerm__2(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = lambdaParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = lambdaParser.Term__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(lambdaParser.LITERAL__1)
                self.state = 20
                localctx.V = self.terms(0)
                self.state = 21
                self.match(lambdaParser.LITERAL__2)
                pass
            elif token in [1]:
                localctx = lambdaParser.Term__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(lambdaParser.LAMBDA)
                self.state = 24
                localctx.X = self.match(lambdaParser.SYMBOL)
                self.state = 25
                self.match(lambdaParser.DOT)
                self.state = 26
                localctx.Y = self.terms(0)
                pass
            elif token in [2]:
                localctx = lambdaParser.Term__3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                localctx.V = self.match(lambdaParser.SYMBOL)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.terms_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terms_sempred(self, localctx:TermsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




