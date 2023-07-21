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

        filepath = Path(input_stream.fileName).resolve()
        snippet = input_stream.strdata.split('\n')[line-1]
        caret = ' '*column + '^'*length
        raise SystemExit(f'  File "{filepath}", line {line}, column {column+1}\n    {snippet}\n    {caret}\nSyntaxError: {msg}')
