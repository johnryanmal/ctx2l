import sys
from antlr4 import *
from lambdaLexer import lambdaLexer
from lambdaParser import lambdaParser
from lambdaVisitor import lambdaVisitor


def main(path):
    input_stream = FileStream(path)
    lexer = lambdaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = lambdaParser(stream)
    tree = parser.calculus()
    visitor = lambdaVisitor()
    result = visitor.visit(tree)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
