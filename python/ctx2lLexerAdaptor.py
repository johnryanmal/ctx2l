from LexerAdaptor import LexerAdaptor


class ctx2lLexerAdaptor(LexerAdaptor):
    def handleBeginArgument(self):
        self.pushMode(self.LexerCharSet)
        self.more()
