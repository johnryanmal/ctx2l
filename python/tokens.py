import sys
from antlr4 import *
from ctx2lLexer import ctx2lLexer


def main(path):
    input_stream = FileStream(path)
    lexer = ctx2lLexer(input_stream)
    for token in lexer.getAllTokens():
        type = lexer.symbolicNames[token.type]
        text = repr(token.text)[1:-1]
        print(f"{text:10}{type}")


if __name__ == '__main__':
    main(*sys.argv[1:])
