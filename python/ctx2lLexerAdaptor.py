from antlr4 import *
from LexerAdaptor import LexerAdaptor


class ctx2lLexerAdaptor(LexerAdaptor):

    def emit(self):
        if self._type == self.ID:
            firstChar = self._input.getText(self._tokenStartCharIndex, self._tokenStartCharIndex)
            if firstChar[0].isupper():
                self._type = self.TOKEN_REF
            else:
                self._type = self.RULE_REF

            if self._currentRuleType == Token.INVALID_TYPE:
                self._currentRuleType = self._type

        elif self._type == self.SEMI:
            self._currentRuleType = Token.INVALID_TYPE
        return Lexer.emit(self)
