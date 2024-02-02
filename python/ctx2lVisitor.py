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
            kind='rule',
            text=ctx.getText()
        )

    def visitTokenLiteral(self, ctx):
        return node(
            type='literal',
            kind='token',
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

    def visitAssign(self, ctx):
        return ctx.getText()

    def visitIdentifier(self, ctx):
        return ctx.getText()

    def visitLabel(self, ctx):
        return node(
            type='label',
            id=ctx.identifier().getText(),
            op=self.visit(ctx.assign())
        )

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
            id=ctx.identifier().getText(),
            call=self.visitable(ctx.call()),
            external=ctx.DOLLAR() is not None
        )

    def visitTokenAtom(self, ctx):
        return node(
            type='atom',
            label=self.visitable(ctx.label()),
            term=self.visit(ctx.tokenTerm()),
            suffix=self.visitable(ctx.ebnfSuffix())
        )

    def visitRuleAtom(self, ctx):
        return node(
            type='atom',
            label=self.visitable(ctx.label()),
            term=self.visit(ctx.ruleTerm()),
            suffix=self.visitable(ctx.ebnfSuffix())
        )

    def visitTokenAlt(self, ctx):
        return node(
            type='alt',
            atoms=self.visits(ctx.tokenAtom())
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

    def visitLexerCommand(self, ctx):
        return ctx.getText()

    def visitTokenCommands(self, ctx):
        return self.visits(ctx.lexerCommand())

    def visitTokenDef(self, ctx):
        return node(
            type='token',
            name=ctx.TOKEN_REF().getText(),
            alts=self.visit(ctx.tokenAlts()),
            cmds=self.visitable(ctx.tokenCommands())
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
