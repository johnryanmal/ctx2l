import sys
from antlr4 import *
from ctx2lLexer import ctx2lLexer
from ctx2lParser import ctx2lParser
from ctx2lVisitor import ctx2lVisitor
from ctx2lEvaluator import ctx2lEvaluator
from pprint import pprint


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ctx2lLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ctx2lParser(stream)
    tree = parser.program()
    visitor = ctx2lVisitor()
    ast = visitor.visit(tree)
    pprint(ast)
    evaluator = ctx2lEvaluator()
    tokens, rules = evaluator.eval(ast)
    print('=== lexer.g4 ===')
    print(tokens)
    print('=== parser.g4 ===')
    print(rules)


if __name__ == '__main__':
    main(sys.argv)