# Generated from examples/lambda/lambdaParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .lambdaParser import lambdaParser
else:
    from lambdaParser import lambdaParser

# This class defines a complete generic visitor for a parse tree produced by lambdaParser.

class lambdaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lambdaParser#calculus.
    def visitCalculus(self, ctx:lambdaParser.CalculusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#terms__2.
    def visitTerms__2(self, ctx:lambdaParser.Terms__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#terms__1.
    def visitTerms__1(self, ctx:lambdaParser.Terms__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#term__1.
    def visitTerm__1(self, ctx:lambdaParser.Term__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#term__2.
    def visitTerm__2(self, ctx:lambdaParser.Term__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#term__3.
    def visitTerm__3(self, ctx:lambdaParser.Term__3Context):
        return self.visitChildren(ctx)



del lambdaParser