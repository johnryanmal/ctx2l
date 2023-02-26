from ctx2lParserVisitor import ctx2lParserVisitor


class ctx2lVisitor(ctx2lParserVisitor):
    def visits(self, ctxs):
        return tuple(self.visit(ctx) for ctx in ctxs)

    def visitable(self, ctx):
        if ctx:
            return self.visit(ctx)
        else:
            return ctx

    def visitRuleLiteral(self, ctx):
        return dict(
            type='literal',
            text=ctx.getText()
        )

    def visitTokenLiteral(self, ctx):
        return dict(
            type='literal',
            text=ctx.getText()
        )

    def visitRuleRef(self, ctx):
        return dict(
            type='ref',
            name=ctx.getText()
        )

    def visitTokenRef(self, ctx):
        return dict(
            type='ref',
            name=ctx.getText()
        )

    def visitEbnfSuffix(self, ctx):
        return ctx.getText()

    def visitTokenAtom(self, ctx):
        return dict(
            type='atom',
            ebnf=self.visit(ctx.tokenEbnf()),
            suffix=self.visitable(ctx.ebnfSuffix())
        )

    def visitRuleAtom(self, ctx):
        return dict(
            type='atom',
            ebnf=self.visit(ctx.ruleEbnf()),
            suffix=self.visitable(ctx.ebnfSuffix())
        )

    def visitTokenAlt(self, ctx):
        return dict(
            type='alt',
            atoms=self.visits(ctx.tokenAtom())
        )

    def visitRuleAlt(self, ctx):
        return dict(
            type='alt',
            atoms=self.visits(ctx.ruleAtom())
        )

    def visitTokenAlts(self, ctx):
        return self.visits(ctx.tokenAlt())

    def visitRuleAlts(self, ctx):
        return self.visits(ctx.ruleAlt())

    def visitTokenSub(self, ctx):
        return dict(
            type='sub',
            alts=self.visit(ctx.tokenAlts())
        )

    def visitRuleSub(self, ctx):
        return dict(
            type='sub',
            alts=self.visit(ctx.ruleAlts())
        )

    def visitTokenDef(self, ctx):
        return dict(
            type='token',
            name=ctx.TOKEN_REF().getText(),
            alts=self.visit(ctx.tokenAlts())
        )

    def visitRuleDef(self, ctx):
        return dict(
            type='rule',
            name=ctx.RULE_REF().getText(),
            alts=self.visit(ctx.ruleAlts())
        )

    def visitProgram(self, ctx):
        return dict(
            type='program',
            tokens=self.visits(ctx.tokenDef()),
            rules=self.visits(ctx.ruleDef())
        )
