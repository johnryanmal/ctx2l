from ctx2lParserVisitor import ctx2lParserVisitor

def spaces(n=1):
    return n*' '

def newlines(n=1):
    return n*'\n'

def indent(n, str):
    return '\n' + spaces(n) + str

def spaced(str):
    if str:
        return ' ' + str
    else:
        return str

def antlrRule(name, alts):
    return (
        name
        + indent(3, ':')
        + indent(3, '|').join(map(spaced, alts))
        + indent(3, ';')
    )

class ctx2lVisitor(ctx2lParserVisitor):
    def visits(self, *args):
        return tuple(self.visit(ctx) for ctx in args)

    def visitRuleLiteral(self, ctx):
        return ctx.getText()

    def visitTokenLiteral(self, ctx):
        return ctx.getText()

    def visitEbnfSuffix(self, ctx):
        return ctx.getText()

    def visitTokenEbnf(self, ctx):
        result = self.visitChildren(ctx)
        return result

    def visitTokenAtom(self, ctx):
        ebnf = ctx.tokenEbnf()
        suffix = ctx.ebnfSuffix()
        if suffix:
            return ''.join(self.visits(ebnf, suffix))
        else:
            return self.visit(ebnf)

    def visitRuleAtom(self, ctx):
        ebnf = ctx.ruleEbnf()
        suffix = ctx.ebnfSuffix()
        if suffix:
            return ''.join(self.visits(ebnf, suffix))
        else:
            return self.visit(ebnf)

    def visitTokenAlt(self, ctx):
        atoms = self.visits(*ctx.tokenAtom())
        return ' '.join(map(str, atoms))

    def visitRuleAlt(self, ctx):
        atoms = self.visits(*ctx.ruleAtom())
        return ' '.join(atoms)

    def visitTokenAlts(self, ctx):
        return self.visits(*ctx.tokenAlt())

    def visitRuleAlts(self, ctx):
        return self.visits(*ctx.ruleAlt())

    def visitTokenSub(self, ctx):
        alts = self.visit(ctx.tokenAlts())
        return (
            '('
            + spaced('|').join(map(spaced, alts))
            + spaced(')')
        )

    def visitRuleSub(self, ctx):
        alts = self.visit(ctx.ruleAlts())
        return (
            '('
            + spaced('|').join(map(spaced, alts))
            + spaced(')')
        )

    def visitTokenDef(self, ctx):
        name = ctx.TOKEN_REF().getText()
        alts = self.visit(ctx.tokenAlts())
        return antlrRule(name, alts)

    def visitRuleDef(self, ctx):
        name = ctx.RULE_REF().getText()
        alts = self.visit(ctx.ruleAlts())
        return antlrRule(name, alts)

    def visitProgram(self, ctx):
        ruleDefs = self.visits(*ctx.ruleDef())
        tokenDefs = self.visits(*ctx.tokenDef())
        ruleGrammar = newlines(2).join(ruleDefs)
        tokenGrammar = newlines(2).join(tokenDefs)
        return tokenGrammar, ruleGrammar
