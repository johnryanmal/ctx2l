import sys
from pathlib import Path
from antlr4 import *
from ctx2lLexer import ctx2lLexer
from ctx2lParser import ctx2lParser
from ctx2lVisitor import ctx2lVisitor
from ctx2lEvaluator import ctx2lEvaluator


def main(path):
    input_stream = FileStream(path)
    lexer = ctx2lLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ctx2lParser(stream)
    tree = parser.program()
    visitor = ctx2lVisitor()
    ast = visitor.visit(tree)
    evaluator = ctx2lEvaluator()
    tokens, rules = evaluator.eval(ast)

    name = Path(path).stem
    lexer_name = f'{name}Lexer'
    parser_name = f'{name}Parser'
    
    print(f'=== {lexer_name}.g4 ===')
    print(f'lexer grammar {lexer_name};\n')
    print(tokens)

    print()

    print(f'=== {parser_name}.g4 ===')
    print(f'parser grammar {parser_name};\n')
    print(f'options {{ tokenVocab = {lexer_name}; }}\n')
    print(rules)


if __name__ == '__main__':
    main(*sys.argv[1:])
