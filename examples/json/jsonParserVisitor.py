# Generated from examples/json/jsonParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsonParser import jsonParser
else:
    from jsonParser import jsonParser

# This class defines a complete generic visitor for a parse tree produced by jsonParser.

class jsonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsonParser#json.
    def visitJson(self, ctx:jsonParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#value__1.
    def visitValue__1(self, ctx:jsonParser.Value__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#value__2.
    def visitValue__2(self, ctx:jsonParser.Value__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#value__3.
    def visitValue__3(self, ctx:jsonParser.Value__3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#value__4.
    def visitValue__4(self, ctx:jsonParser.Value__4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#value__5.
    def visitValue__5(self, ctx:jsonParser.Value__5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#value__6.
    def visitValue__6(self, ctx:jsonParser.Value__6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#value__7.
    def visitValue__7(self, ctx:jsonParser.Value__7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#object__1.
    def visitObject__1(self, ctx:jsonParser.Object__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#object__2.
    def visitObject__2(self, ctx:jsonParser.Object__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#members.
    def visitMembers(self, ctx:jsonParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#member.
    def visitMember(self, ctx:jsonParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#array__1.
    def visitArray__1(self, ctx:jsonParser.Array__1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#array__2.
    def visitArray__2(self, ctx:jsonParser.Array__2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#elements.
    def visitElements(self, ctx:jsonParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#element.
    def visitElement(self, ctx:jsonParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#ws.
    def visitWs(self, ctx:jsonParser.WsContext):
        return self.visitChildren(ctx)



del jsonParser