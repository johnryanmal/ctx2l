# Generated from test/testParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .testParser import testParser
else:
    from testParser import testParser

# This class defines a complete generic visitor for a parse tree produced by testParser.

class testParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by testParser#expr.
    def visitExpr(self, ctx:testParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#sum__1.
    def visitSum__1(self, ctx:testParser.Sum__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#sum__2.
    def visitSum__2(self, ctx:testParser.Sum__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#sum__3.
    def visitSum__3(self, ctx:testParser.Sum__3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#prod__1.
    def visitProd__1(self, ctx:testParser.Prod__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#prod__2.
    def visitProd__2(self, ctx:testParser.Prod__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#prod__3.
    def visitProd__3(self, ctx:testParser.Prod__3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#pow__1.
    def visitPow__1(self, ctx:testParser.Pow__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#pow__2.
    def visitPow__2(self, ctx:testParser.Pow__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#value__1.
    def visitValue__1(self, ctx:testParser.Value__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#value__2.
    def visitValue__2(self, ctx:testParser.Value__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#ws.
    def visitWs(self, ctx:testParser.WsContext):
        return self.visitChildren(ctx)



del testParser