# Generated from examples/calculator/calculatorParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calculatorParser import calculatorParser
else:
    from calculatorParser import calculatorParser

# This class defines a complete generic visitor for a parse tree produced by calculatorParser.

class calculatorParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculatorParser#expr.
    def visitExpr(self, ctx:calculatorParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#sum__1.
    def visitSum__1(self, ctx:calculatorParser.Sum__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#sum__2.
    def visitSum__2(self, ctx:calculatorParser.Sum__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#sum__3.
    def visitSum__3(self, ctx:calculatorParser.Sum__3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#prod__1.
    def visitProd__1(self, ctx:calculatorParser.Prod__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#prod__2.
    def visitProd__2(self, ctx:calculatorParser.Prod__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#prod__3.
    def visitProd__3(self, ctx:calculatorParser.Prod__3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#pow__1.
    def visitPow__1(self, ctx:calculatorParser.Pow__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#pow__2.
    def visitPow__2(self, ctx:calculatorParser.Pow__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#value__1.
    def visitValue__1(self, ctx:calculatorParser.Value__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculatorParser#value__2.
    def visitValue__2(self, ctx:calculatorParser.Value__2Context):
        return self.visitChildren(ctx)



del calculatorParser