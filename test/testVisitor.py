from testParserVisitor import testParserVisitor
from testEvaluator import add, div, mul, num, pow, sub


class testVisitor(testParserVisitor):
    def visitExpr(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitSum__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitSum__2(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return add(L, R)
    
    def visitSum__3(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return sub(L, R)
    
    def visitProd__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitProd__2(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return mul(L, R)
    
    def visitProd__3(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return div(L, R)
    
    def visitPow__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitPow__2(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return pow(L, R)
    
    def visitValue__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitValue__2(self, ctx):
        V = ctx.V.text
        return num(V)
    
    def visitWs(self, ctx):
        return type('ws', (), {})()