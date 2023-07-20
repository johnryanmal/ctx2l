from pathlib import Path
from antlr4.error.ErrorListener import *


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        input_stream = recognizer.inputStream
        filepath = Path(input_stream.fileName).resolve()
        snippet = input_stream.strdata.split('\n')[line-1]

        if offendingSymbol:
            length = offendingSymbol.stop - offendingSymbol.start + 1
        else:
            length = 1

        caret = ' '*column + '^'*length
        raise SystemExit(f'  File "{filepath}", line {line}, column {column+1}\n    {snippet}\n    {caret}\nSyntaxError: {msg}')
