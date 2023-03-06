import sys
from antlr4 import *
from jsonLexer import jsonLexer
from jsonParser import jsonParser
from jsonVisitor import jsonVisitor


def main(path):
    input_stream = FileStream(path)
    lexer = jsonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = jsonParser(stream)
    tree = parser.json()
    visitor = jsonVisitor()
    result = visitor.visit(tree)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
