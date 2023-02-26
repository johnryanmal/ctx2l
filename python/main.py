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
    evaluator = ctx2lEvaluator()
    generator = ctx2lPythonEvaluator()
    lexerGrammar, parserGrammar = evaluator.eval(ast)
    visitorMethods = generator.eval(ast)

    name = Path(path).stem
    
    print(f'=== {name}Lexer.g4 ===')
    print(f'lexer grammar {name}Lexer;\n')
    print(lexerGrammar)

    print()

    print(f'=== {name}Parser.g4 ===')
    print(f'parser grammar {name}Parser;\n')
    print(f'options {{ tokenVocab = {name}Lexer; }}\n')
    print(parserGrammar)

    print()

    print(f'=== {name}Visitor.py ===')
    print(f'from {name}ParserVisitor import {name}ParserVisitor\n\n')
    print(f'class {name}Visitor({name}ParserVisitor):')
    print(visitorMethods)


if __name__ == '__main__':
    main(*sys.argv[1:])
