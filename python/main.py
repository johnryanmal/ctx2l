import sys
from pathlib import Path
from antlr4 import *
from ctx2lLexer import ctx2lLexer
from ctx2lParser import ctx2lParser
from ctx2lVisitor import ctx2lVisitor
from ctx2lEvaluator import ctx2lEvaluator, ctx2lPythonEvaluator


def main(path):
    input_stream = FileStream(path)
    lexer = ctx2lLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ctx2lParser(stream)
    tree = parser.program()
    visitor = ctx2lVisitor()
    ast = visitor.visit(tree)

    name = Path(path).stem
    evaluator = ctx2lEvaluator(name)
    generator = ctx2lPythonEvaluator(name)
    lexerFile, parserFile = evaluator.eval(ast)
    visitorFile = generator.eval(ast)
    
    print(f'=== {name}Lexer.g4 ===')
    print(lexerFile)

    print()

    print(f'=== {name}Parser.g4 ===')
    print(parserFile)

    print()

    print(f'=== {name}Visitor.py ===')
    print(visitorFile)


if __name__ == '__main__':
    main(*sys.argv[1:])
