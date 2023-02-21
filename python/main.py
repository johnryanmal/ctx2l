import sys
from antlr4 import *
from ctx2lLexer import ctx2lLexer
from ctx2lParser import ctx2lParser
from ctx2lVisitor import ctx2lVisitor


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ctx2lLexer(input_stream)
    #print(list(lexer.symbolicNames[token.type] for token in lexer.getAllTokens()))
    stream = CommonTokenStream(lexer)
    parser = ctx2lParser(stream)
    tree = parser.program()
    visitor = ctx2lVisitor()
    ast = visitor.visitProgram(tree)
    print(ast)


if __name__ == '__main__':
    main(sys.argv)