import sys
from antlr4 import *
from calculatorLexer import calculatorLexer
from calculatorParser import calculatorParser
from calculatorVisitor import calculatorVisitor


def main(path):
    input_stream = FileStream(path)
    lexer = calculatorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = calculatorParser(stream)
    tree = parser.expr()
    visitor = calculatorVisitor()
    result = visitor.visit(tree)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
