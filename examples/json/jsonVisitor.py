from jsonParserVisitor import jsonParserVisitor
from jsonEvaluator import jsonEvaluator


class jsonVisitor(jsonParserVisitor):
    def __init__(self):
        self.evaluator = jsonEvaluator()
    
    def visitJson(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitValue__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitValue__2(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitValue__3(self, ctx):
        V = ctx.V.text
        return self.evaluator.unquote(V)
    
    def visitValue__4(self, ctx):
        V = ctx.V.text
        return V
    
    def visitValue__5(self, ctx):
        V = ctx.V.text
        return V
    
    def visitValue__6(self, ctx):
        V = ctx.V.text
        return V
    
    def visitValue__7(self, ctx):
        V = ctx.V.text
        return V
    
    def visitObject__1(self, ctx):
        return type('object__1', (), {})()
    
    def visitObject__2(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitMembers(self, ctx):
        VS = tuple(self.visit(rule) for rule in ctx.VS)
        return self.evaluator.dict(VS)
    
    def visitMember(self, ctx):
        K = ctx.K.text
        V = self.visit(ctx.V)
        return self.evaluator.pair(self.evaluator.unquote(K), V)
    
    def visitArray__1(self, ctx):
        return type('array__1', (), {})()
    
    def visitArray__2(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitElements(self, ctx):
        V = tuple(self.visit(rule) for rule in ctx.V)
        return V
    
    def visitElement(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitWs(self, ctx):
        return type('ws', (), {})()
