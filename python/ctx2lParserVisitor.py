# Generated from ./ctx2lParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ctx2lParser import ctx2lParser
else:
    from ctx2lParser import ctx2lParser

# This class defines a complete generic visitor for a parse tree produced by ctx2lParser.

class ctx2lParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ctx2lParser#program.
    def visitProgram(self, ctx:ctx2lParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleDef.
    def visitRuleDef(self, ctx:ctx2lParser.RuleDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#tokenDef.
    def visitTokenDef(self, ctx:ctx2lParser.TokenDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleSub.
    def visitRuleSub(self, ctx:ctx2lParser.RuleSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#tokenSub.
    def visitTokenSub(self, ctx:ctx2lParser.TokenSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleAlts.
    def visitRuleAlts(self, ctx:ctx2lParser.RuleAltsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#tokenAlts.
    def visitTokenAlts(self, ctx:ctx2lParser.TokenAltsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleAlt.
    def visitRuleAlt(self, ctx:ctx2lParser.RuleAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#tokenAlt.
    def visitTokenAlt(self, ctx:ctx2lParser.TokenAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleAtom.
    def visitRuleAtom(self, ctx:ctx2lParser.RuleAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleEbnf.
    def visitRuleEbnf(self, ctx:ctx2lParser.RuleEbnfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleRef.
    def visitRuleRef(self, ctx:ctx2lParser.RuleRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleLiteral.
    def visitRuleLiteral(self, ctx:ctx2lParser.RuleLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#expr.
    def visitExpr(self, ctx:ctx2lParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#call.
    def visitCall(self, ctx:ctx2lParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#args.
    def visitArgs(self, ctx:ctx2lParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#tokenAtom.
    def visitTokenAtom(self, ctx:ctx2lParser.TokenAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#tokenEbnf.
    def visitTokenEbnf(self, ctx:ctx2lParser.TokenEbnfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#tokenRef.
    def visitTokenRef(self, ctx:ctx2lParser.TokenRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#tokenLiteral.
    def visitTokenLiteral(self, ctx:ctx2lParser.TokenLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#label.
    def visitLabel(self, ctx:ctx2lParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#assign.
    def visitAssign(self, ctx:ctx2lParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#grammarSpec.
    def visitGrammarSpec(self, ctx:ctx2lParser.GrammarSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#grammarDecl.
    def visitGrammarDecl(self, ctx:ctx2lParser.GrammarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#grammarType.
    def visitGrammarType(self, ctx:ctx2lParser.GrammarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#prequelConstruct.
    def visitPrequelConstruct(self, ctx:ctx2lParser.PrequelConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#optionsSpec.
    def visitOptionsSpec(self, ctx:ctx2lParser.OptionsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#option.
    def visitOption(self, ctx:ctx2lParser.OptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#optionValue.
    def visitOptionValue(self, ctx:ctx2lParser.OptionValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#delegateGrammars.
    def visitDelegateGrammars(self, ctx:ctx2lParser.DelegateGrammarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#delegateGrammar.
    def visitDelegateGrammar(self, ctx:ctx2lParser.DelegateGrammarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#tokensSpec.
    def visitTokensSpec(self, ctx:ctx2lParser.TokensSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#channelsSpec.
    def visitChannelsSpec(self, ctx:ctx2lParser.ChannelsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#idList.
    def visitIdList(self, ctx:ctx2lParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#action_.
    def visitAction_(self, ctx:ctx2lParser.Action_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#actionScopeName.
    def visitActionScopeName(self, ctx:ctx2lParser.ActionScopeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#actionBlock.
    def visitActionBlock(self, ctx:ctx2lParser.ActionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#argActionBlock.
    def visitArgActionBlock(self, ctx:ctx2lParser.ArgActionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#modeSpec.
    def visitModeSpec(self, ctx:ctx2lParser.ModeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#rules.
    def visitRules(self, ctx:ctx2lParser.RulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleSpec.
    def visitRuleSpec(self, ctx:ctx2lParser.RuleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#parserRuleSpec.
    def visitParserRuleSpec(self, ctx:ctx2lParser.ParserRuleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#exceptionGroup.
    def visitExceptionGroup(self, ctx:ctx2lParser.ExceptionGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#exceptionHandler.
    def visitExceptionHandler(self, ctx:ctx2lParser.ExceptionHandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#finallyClause.
    def visitFinallyClause(self, ctx:ctx2lParser.FinallyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#rulePrequel.
    def visitRulePrequel(self, ctx:ctx2lParser.RulePrequelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleReturns.
    def visitRuleReturns(self, ctx:ctx2lParser.RuleReturnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#throwsSpec.
    def visitThrowsSpec(self, ctx:ctx2lParser.ThrowsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#localsSpec.
    def visitLocalsSpec(self, ctx:ctx2lParser.LocalsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleAction.
    def visitRuleAction(self, ctx:ctx2lParser.RuleActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleModifiers.
    def visitRuleModifiers(self, ctx:ctx2lParser.RuleModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleModifier.
    def visitRuleModifier(self, ctx:ctx2lParser.RuleModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleBlock.
    def visitRuleBlock(self, ctx:ctx2lParser.RuleBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleAltList.
    def visitRuleAltList(self, ctx:ctx2lParser.RuleAltListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#labeledAlt.
    def visitLabeledAlt(self, ctx:ctx2lParser.LabeledAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerRuleSpec.
    def visitLexerRuleSpec(self, ctx:ctx2lParser.LexerRuleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerRuleBlock.
    def visitLexerRuleBlock(self, ctx:ctx2lParser.LexerRuleBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerAltList.
    def visitLexerAltList(self, ctx:ctx2lParser.LexerAltListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerAlt.
    def visitLexerAlt(self, ctx:ctx2lParser.LexerAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerElements.
    def visitLexerElements(self, ctx:ctx2lParser.LexerElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerElement.
    def visitLexerElement(self, ctx:ctx2lParser.LexerElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#labeledLexerElement.
    def visitLabeledLexerElement(self, ctx:ctx2lParser.LabeledLexerElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerBlock.
    def visitLexerBlock(self, ctx:ctx2lParser.LexerBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerCommands.
    def visitLexerCommands(self, ctx:ctx2lParser.LexerCommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerCommand.
    def visitLexerCommand(self, ctx:ctx2lParser.LexerCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerCommandName.
    def visitLexerCommandName(self, ctx:ctx2lParser.LexerCommandNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerCommandExpr.
    def visitLexerCommandExpr(self, ctx:ctx2lParser.LexerCommandExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#altList.
    def visitAltList(self, ctx:ctx2lParser.AltListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#alternative.
    def visitAlternative(self, ctx:ctx2lParser.AlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#element.
    def visitElement(self, ctx:ctx2lParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#labeledElement.
    def visitLabeledElement(self, ctx:ctx2lParser.LabeledElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ebnf.
    def visitEbnf(self, ctx:ctx2lParser.EbnfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#blockSuffix.
    def visitBlockSuffix(self, ctx:ctx2lParser.BlockSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ebnfSuffix.
    def visitEbnfSuffix(self, ctx:ctx2lParser.EbnfSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#lexerAtom.
    def visitLexerAtom(self, ctx:ctx2lParser.LexerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#atom.
    def visitAtom(self, ctx:ctx2lParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#notSet.
    def visitNotSet(self, ctx:ctx2lParser.NotSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#blockSet.
    def visitBlockSet(self, ctx:ctx2lParser.BlockSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#setElement.
    def visitSetElement(self, ctx:ctx2lParser.SetElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#block.
    def visitBlock(self, ctx:ctx2lParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#ruleref.
    def visitRuleref(self, ctx:ctx2lParser.RulerefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#characterRange.
    def visitCharacterRange(self, ctx:ctx2lParser.CharacterRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#terminal.
    def visitTerminal(self, ctx:ctx2lParser.TerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#elementOptions.
    def visitElementOptions(self, ctx:ctx2lParser.ElementOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#elementOption.
    def visitElementOption(self, ctx:ctx2lParser.ElementOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ctx2lParser#identifier.
    def visitIdentifier(self, ctx:ctx2lParser.IdentifierContext):
        return self.visitChildren(ctx)



del ctx2lParser