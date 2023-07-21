from pathlib import Path
from antlr4.error.ErrorListener import *


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol:
            input_stream = offendingSymbol.getInputStream()
            length = offendingSymbol.stop - offendingSymbol.start + 1
        else:
            input_stream = recognizer.inputStream
            length = 1

        try:
            filename = input_stream.fileName
        except AttributeError:
            source = None
        else:
            filepath = Path(filename).resolve()
            source = f'File "{filepath}", line {line}, column {column+1}'
        
        snippet = input_stream.strdata.split('\n')[line-1]
        caret = ' '*column + '^'*length

        errmsg = ''
        if source:
            errmsg += ' '*2 + source + '\n'
        errmsg += ' '*4 + snippet + '\n'
        errmsg += ' '*4 + caret + '\n'
        errmsg += f'SyntaxError: {msg}'
        raise SystemExit(errmsg)
