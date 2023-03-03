import sys
from antlr4 import *
from testLexer import testLexer
from testParser import testParser
from testVisitor import testVisitor


def main(path):
    input_stream = FileStream(path)
    lexer = testLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = testParser(stream)
    tree = parser.expr()
    visitor = testVisitor()
    result = visitor.visit(tree)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
