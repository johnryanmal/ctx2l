# Generated from examples/json/jsonParser.g4 by ANTLR 4.13.0
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
        4,1,12,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,29,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,3,1,3,5,3,44,
        8,3,10,3,12,3,47,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,63,8,5,1,6,1,6,1,6,5,6,68,8,6,10,6,12,6,71,9,6,1,
        7,1,7,1,7,1,7,1,8,3,8,78,8,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,0,
        81,0,18,1,0,0,0,2,28,1,0,0,0,4,38,1,0,0,0,6,40,1,0,0,0,8,48,1,0,
        0,0,10,62,1,0,0,0,12,64,1,0,0,0,14,72,1,0,0,0,16,77,1,0,0,0,18,19,
        3,14,7,0,19,20,5,0,0,1,20,1,1,0,0,0,21,29,3,4,2,0,22,29,3,10,5,0,
        23,29,5,1,0,0,24,29,5,2,0,0,25,29,5,6,0,0,26,29,5,4,0,0,27,29,5,
        5,0,0,28,21,1,0,0,0,28,22,1,0,0,0,28,23,1,0,0,0,28,24,1,0,0,0,28,
        25,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,11,0,
        0,31,32,3,16,8,0,32,33,5,12,0,0,33,39,1,0,0,0,34,35,5,11,0,0,35,
        36,3,6,3,0,36,37,5,12,0,0,37,39,1,0,0,0,38,30,1,0,0,0,38,34,1,0,
        0,0,39,5,1,0,0,0,40,45,3,8,4,0,41,42,5,7,0,0,42,44,3,8,4,0,43,41,
        1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,7,1,0,0,0,47,
        45,1,0,0,0,48,49,3,16,8,0,49,50,5,1,0,0,50,51,3,16,8,0,51,52,5,8,
        0,0,52,53,3,14,7,0,53,9,1,0,0,0,54,55,5,9,0,0,55,56,3,16,8,0,56,
        57,5,10,0,0,57,63,1,0,0,0,58,59,5,9,0,0,59,60,3,12,6,0,60,61,5,10,
        0,0,61,63,1,0,0,0,62,54,1,0,0,0,62,58,1,0,0,0,63,11,1,0,0,0,64,69,
        3,14,7,0,65,66,5,7,0,0,66,68,3,14,7,0,67,65,1,0,0,0,68,71,1,0,0,
        0,69,67,1,0,0,0,69,70,1,0,0,0,70,13,1,0,0,0,71,69,1,0,0,0,72,73,
        3,16,8,0,73,74,3,2,1,0,74,75,3,16,8,0,75,15,1,0,0,0,76,78,5,3,0,
        0,77,76,1,0,0,0,77,78,1,0,0,0,78,17,1,0,0,0,6,28,38,45,62,69,77
    ]

class jsonParser ( Parser ):

    grammarFileName = "jsonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'false'", "'null'", "'true'", "','", "':'", "'['", 
                     "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "STRING", "NUMBER", "WS", "LITERAL__1", 
                      "LITERAL__2", "LITERAL__3", "LITERAL__4", "LITERAL__5", 
                      "LITERAL__6", "LITERAL__7", "LITERAL__8", "LITERAL__9" ]

    RULE_json = 0
    RULE_value = 1
    RULE_object = 2
    RULE_members = 3
    RULE_member = 4
    RULE_array = 5
    RULE_elements = 6
    RULE_element = 7
    RULE_ws = 8

    ruleNames =  [ "json", "value", "object", "members", "member", "array", 
                   "elements", "element", "ws" ]

    EOF = Token.EOF
    STRING=1
    NUMBER=2
    WS=3
    LITERAL__1=4
    LITERAL__2=5
    LITERAL__3=6
    LITERAL__4=7
    LITERAL__5=8
    LITERAL__6=9
    LITERAL__7=10
    LITERAL__8=11
    LITERAL__9=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.V = None # ElementContext

        def EOF(self):
            return self.getToken(jsonParser.EOF, 0)

        def element(self):
            return self.getTypedRuleContext(jsonParser.ElementContext,0)


        def getRuleIndex(self):
            return jsonParser.RULE_json

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson" ):
                return visitor.visitJson(self)
            else:
                return visitor.visitChildren(self)




    def json(self):

        localctx = jsonParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            localctx.V = self.element()
            self.state = 19
            self.match(jsonParser.EOF)
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
            return jsonParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Value__3Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ValueContext
            super().__init__(parser)
            self.V = None # Token
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(jsonParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__3" ):
                return visitor.visitValue__3(self)
            else:
                return visitor.visitChildren(self)


    class Value__4Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ValueContext
            super().__init__(parser)
            self.V = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(jsonParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__4" ):
                return visitor.visitValue__4(self)
            else:
                return visitor.visitChildren(self)


    class Value__1Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ValueContext
            super().__init__(parser)
            self.V = None # ObjectContext
            self.copyFrom(ctx)

        def object_(self):
            return self.getTypedRuleContext(jsonParser.ObjectContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__1" ):
                return visitor.visitValue__1(self)
            else:
                return visitor.visitChildren(self)


    class Value__2Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ValueContext
            super().__init__(parser)
            self.V = None # ArrayContext
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(jsonParser.ArrayContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__2" ):
                return visitor.visitValue__2(self)
            else:
                return visitor.visitChildren(self)


    class Value__7Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ValueContext
            super().__init__(parser)
            self.V = None # Token
            self.copyFrom(ctx)

        def LITERAL__2(self):
            return self.getToken(jsonParser.LITERAL__2, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__7" ):
                return visitor.visitValue__7(self)
            else:
                return visitor.visitChildren(self)


    class Value__5Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ValueContext
            super().__init__(parser)
            self.V = None # Token
            self.copyFrom(ctx)

        def LITERAL__3(self):
            return self.getToken(jsonParser.LITERAL__3, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__5" ):
                return visitor.visitValue__5(self)
            else:
                return visitor.visitChildren(self)


    class Value__6Context(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ValueContext
            super().__init__(parser)
            self.V = None # Token
            self.copyFrom(ctx)

        def LITERAL__1(self):
            return self.getToken(jsonParser.LITERAL__1, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue__6" ):
                return visitor.visitValue__6(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = jsonParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = jsonParser.Value__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                localctx.V = self.object_()
                pass
            elif token in [9]:
                localctx = jsonParser.Value__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                localctx.V = self.array()
                pass
            elif token in [1]:
                localctx = jsonParser.Value__3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                localctx.V = self.match(jsonParser.STRING)
                pass
            elif token in [2]:
                localctx = jsonParser.Value__4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                localctx.V = self.match(jsonParser.NUMBER)
                pass
            elif token in [6]:
                localctx = jsonParser.Value__5Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 25
                localctx.V = self.match(jsonParser.LITERAL__3)
                pass
            elif token in [4]:
                localctx = jsonParser.Value__6Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 26
                localctx.V = self.match(jsonParser.LITERAL__1)
                pass
            elif token in [5]:
                localctx = jsonParser.Value__7Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 27
                localctx.V = self.match(jsonParser.LITERAL__2)
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


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return jsonParser.RULE_object

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Object__1Context(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LITERAL__8(self):
            return self.getToken(jsonParser.LITERAL__8, 0)
        def ws(self):
            return self.getTypedRuleContext(jsonParser.WsContext,0)

        def LITERAL__9(self):
            return self.getToken(jsonParser.LITERAL__9, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject__1" ):
                return visitor.visitObject__1(self)
            else:
                return visitor.visitChildren(self)


    class Object__2Context(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ObjectContext
            super().__init__(parser)
            self.V = None # MembersContext
            self.copyFrom(ctx)

        def LITERAL__8(self):
            return self.getToken(jsonParser.LITERAL__8, 0)
        def LITERAL__9(self):
            return self.getToken(jsonParser.LITERAL__9, 0)
        def members(self):
            return self.getTypedRuleContext(jsonParser.MembersContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject__2" ):
                return visitor.visitObject__2(self)
            else:
                return visitor.visitChildren(self)



    def object_(self):

        localctx = jsonParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_object)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = jsonParser.Object__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(jsonParser.LITERAL__8)
                self.state = 31
                self.ws()
                self.state = 32
                self.match(jsonParser.LITERAL__9)
                pass

            elif la_ == 2:
                localctx = jsonParser.Object__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(jsonParser.LITERAL__8)
                self.state = 35
                localctx.V = self.members()
                self.state = 36
                self.match(jsonParser.LITERAL__9)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._member = None # MemberContext
            self.VS = list() # of MemberContexts

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsonParser.MemberContext)
            else:
                return self.getTypedRuleContext(jsonParser.MemberContext,i)


        def LITERAL__4(self, i:int=None):
            if i is None:
                return self.getTokens(jsonParser.LITERAL__4)
            else:
                return self.getToken(jsonParser.LITERAL__4, i)

        def getRuleIndex(self):
            return jsonParser.RULE_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = jsonParser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            localctx._member = self.member()
            localctx.VS.append(localctx._member)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 41
                self.match(jsonParser.LITERAL__4)
                self.state = 42
                localctx._member = self.member()
                localctx.VS.append(localctx._member)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.K = None # Token
            self.V = None # ElementContext

        def ws(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsonParser.WsContext)
            else:
                return self.getTypedRuleContext(jsonParser.WsContext,i)


        def LITERAL__5(self):
            return self.getToken(jsonParser.LITERAL__5, 0)

        def STRING(self):
            return self.getToken(jsonParser.STRING, 0)

        def element(self):
            return self.getTypedRuleContext(jsonParser.ElementContext,0)


        def getRuleIndex(self):
            return jsonParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = jsonParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.ws()
            self.state = 49
            localctx.K = self.match(jsonParser.STRING)
            self.state = 50
            self.ws()
            self.state = 51
            self.match(jsonParser.LITERAL__5)
            self.state = 52
            localctx.V = self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return jsonParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Array__1Context(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LITERAL__6(self):
            return self.getToken(jsonParser.LITERAL__6, 0)
        def ws(self):
            return self.getTypedRuleContext(jsonParser.WsContext,0)

        def LITERAL__7(self):
            return self.getToken(jsonParser.LITERAL__7, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray__1" ):
                return visitor.visitArray__1(self)
            else:
                return visitor.visitChildren(self)


    class Array__2Context(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsonParser.ArrayContext
            super().__init__(parser)
            self.V = None # ElementsContext
            self.copyFrom(ctx)

        def LITERAL__6(self):
            return self.getToken(jsonParser.LITERAL__6, 0)
        def LITERAL__7(self):
            return self.getToken(jsonParser.LITERAL__7, 0)
        def elements(self):
            return self.getTypedRuleContext(jsonParser.ElementsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray__2" ):
                return visitor.visitArray__2(self)
            else:
                return visitor.visitChildren(self)



    def array(self):

        localctx = jsonParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = jsonParser.Array__1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(jsonParser.LITERAL__6)
                self.state = 55
                self.ws()
                self.state = 56
                self.match(jsonParser.LITERAL__7)
                pass

            elif la_ == 2:
                localctx = jsonParser.Array__2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(jsonParser.LITERAL__6)
                self.state = 59
                localctx.V = self.elements()
                self.state = 60
                self.match(jsonParser.LITERAL__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._element = None # ElementContext
            self.V = list() # of ElementContexts

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsonParser.ElementContext)
            else:
                return self.getTypedRuleContext(jsonParser.ElementContext,i)


        def LITERAL__4(self, i:int=None):
            if i is None:
                return self.getTokens(jsonParser.LITERAL__4)
            else:
                return self.getToken(jsonParser.LITERAL__4, i)

        def getRuleIndex(self):
            return jsonParser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = jsonParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            localctx._element = self.element()
            localctx.V.append(localctx._element)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 65
                self.match(jsonParser.LITERAL__4)
                self.state = 66
                localctx._element = self.element()
                localctx.V.append(localctx._element)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.V = None # ValueContext

        def ws(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsonParser.WsContext)
            else:
                return self.getTypedRuleContext(jsonParser.WsContext,i)


        def value(self):
            return self.getTypedRuleContext(jsonParser.ValueContext,0)


        def getRuleIndex(self):
            return jsonParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = jsonParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.ws()
            self.state = 73
            localctx.V = self.value()
            self.state = 74
            self.ws()
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
            return self.getToken(jsonParser.WS, 0)

        def getRuleIndex(self):
            return jsonParser.RULE_ws

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWs" ):
                return visitor.visitWs(self)
            else:
                return visitor.visitChildren(self)




    def ws(self):

        localctx = jsonParser.WsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ws)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 76
                self.match(jsonParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





