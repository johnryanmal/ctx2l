from lambdaParserVisitor import lambdaParserVisitor
from lambdaEvaluator import lambdaEvaluator


class lambdaVisitor(lambdaParserVisitor):
    def __init__(self):
        self.evaluator = lambdaEvaluator()
    
    def visitCalculus(self, ctx):
        V = self.visit(ctx.V)
        return self.evaluator.eval(V)
    
    def visitTerms__1(self, ctx):
        F = self.visit(ctx.F)
        V = self.visit(ctx.V)
        return self.evaluator.apply(F, V)
    
    def visitTerms__2(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitTerm__1(self, ctx):
        V = self.visit(ctx.V)
        return V
    
    def visitTerm__2(self, ctx):
        X = ctx.X.text
        Y = self.visit(ctx.Y)
        return self.evaluator.abstract(X, Y)
    
    def visitTerm__3(self, ctx):
        V = ctx.V.text
        return self.evaluator.symbol(V)
