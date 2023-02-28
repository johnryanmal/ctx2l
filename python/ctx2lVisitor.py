from ctx2lParserVisitor import ctx2lParserVisitor


def node(**kwargs):
    pairs = {}
    for k, v in kwargs.items():
        if v is not None:
            pairs[k] = v
    return pairs


class ctx2lVisitor(ctx2lParserVisitor):
    def visits(self, ctxs):
        return tuple(self.visit(ctx) for ctx in ctxs)

    def visitable(self, ctx):
        if ctx:
            return self.visit(ctx)
        else:
            return ctx

    def visitRuleLiteral(self, ctx):
        return node(
            type='literal',
            text=ctx.getText()
        )

    def visitTokenLiteral(self, ctx):
        return node(
            type='literal',
            text=ctx.getText()
        )

    def visitRuleRef(self, ctx):
        return node(
            type='ref',
            name=ctx.getText()
        )

    def visitTokenRef(self, ctx):
        return node(
            type='ref',
            name=ctx.getText()
        )

    def visitEbnfSuffix(self, ctx):
        return ctx.getText()

    def visitLabel(self, ctx):
        return ctx.getText()

    def visitArgs(self, ctx):
        return self.visits(ctx.expr())

    def visitCall(self, ctx):
        return node(
            type='call',
            args=self.visitable(ctx.args())
        )

    def visitExpr(self, ctx):
        return node(
            type='expr',
            id=self.visit(ctx.identifier()),
            call=self.visitable(ctx.call())
        )

    def visitTokenAtom(self, ctx):
        return node(
            type='atom',
            label=self.visitable(ctx.label()),
            ebnf=self.visit(ctx.tokenEbnf()),
            suffix=self.visitable(ctx.ebnfSuffix())
        )

    def visitRuleAtom(self, ctx):
        return node(
            type='atom',
            label=self.visitable(ctx.label()),
            ebnf=self.visit(ctx.ruleEbnf()),
            suffix=self.visitable(ctx.ebnfSuffix())
        )

    def visitTokenAlt(self, ctx):
        return node(
            type='alt',
            atoms=self.visits(ctx.tokenAtom()),
            expr=None
        )

    def visitRuleAlt(self, ctx):
        return node(
            type='alt',
            atoms=self.visits(ctx.ruleAtom()),
            expr=self.visitable(ctx.expr())
        )

    def visitTokenAlts(self, ctx):
        return self.visits(ctx.tokenAlt())

    def visitRuleAlts(self, ctx):
        return self.visits(ctx.ruleAlt())

    def visitTokenSub(self, ctx):
        return node(
            type='sub',
            alts=self.visit(ctx.tokenAlts())
        )

    def visitRuleSub(self, ctx):
        return node(
            type='sub',
            alts=self.visit(ctx.ruleAlts())
        )

    def visitTokenDef(self, ctx):
        return node(
            type='token',
            name=ctx.TOKEN_REF().getText(),
            alts=self.visit(ctx.tokenAlts())
        )

    def visitRuleDef(self, ctx):
        return node(
            type='rule',
            name=ctx.RULE_REF().getText(),
            alts=self.visit(ctx.ruleAlts())
        )

    def visitProgram(self, ctx):
        return node(
            type='program',
            tokens=self.visits(ctx.tokenDef()),
            rules=self.visits(ctx.ruleDef())
        )
