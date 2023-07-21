from calculatorParserVisitor import calculatorParserVisitor


class calculatorVisitor(calculatorParserVisitor):
    def __init__(self, evaluator):
        self.evaluator = evaluator
    
    def visitCalculation(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitExpr(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitSum__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitSum__2(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return self.evaluator.add(L, R)
    
    def visitSum__3(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return self.evaluator.sub(L, R)
    
    def visitProd__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitProd__2(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return self.evaluator.mul(L, R)
    
    def visitProd__3(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return self.evaluator.div(L, R)
    
    def visitPow__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitPow__2(self, ctx):
        L = self.visit(ctx.L)
        R = self.visit(ctx.R)
        return self.evaluator.pow(L, R)
    
    def visitValue__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitValue__2(self, ctx):
        V = ctx.V.text
        return self.evaluator.num(V)
