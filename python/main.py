import sys
from pathlib import Path
from antlr4 import *
from ctx2lLexer import ctx2lLexer
from ctx2lParser import ctx2lParser
from ctx2lVisitor import ctx2lVisitor
from ctx2lEvaluator import ctx2lEvaluator, ctx2lPythonEvaluator


class Writer:
    def __init__(self, path):
        self.path = path

    def write(self, filename, content):
        with open(Path(self.path, filename), 'w') as file:
            file.write(content)


def main(input_path, output_path):
    input_stream = FileStream(input_path)
    lexer = ctx2lLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ctx2lParser(stream)
    tree = parser.program()
    visitor = ctx2lVisitor()
    ast = visitor.visit(tree)

    name = Path(input_path).stem
    evaluator = ctx2lEvaluator(name)
    generator = ctx2lPythonEvaluator(name)
    lexerFile, parserFile = evaluator.eval(ast)
    visitorFile, visitorEvaluatorFile = generator.eval(ast)

    writer = Writer(output_path)
    writer.write(f'{name}Lexer.g4', lexerFile)
    writer.write(f'{name}Parser.g4', parserFile)
    writer.write(f'{name}Visitor.py', visitorFile)
    writer.write(f'{name}VisitorEvaluator.py', visitorEvaluatorFile)


if __name__ == '__main__':
    main(*sys.argv[1:])
