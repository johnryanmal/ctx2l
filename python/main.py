import sys
import subprocess
from pathlib import Path
from antlr4 import *
from ctx2lLexer import ctx2lLexer
from ctx2lParser import ctx2lParser
from ctx2lVisitor import ctx2lVisitor
from ctx2lEvaluator import ctx2lEvaluator, ctx2lPythonEvaluator
from ThrowingErrorListener import ThrowingErrorListener


class Writer:
    def __init__(self, path):
        self.path = path

    def write_file(self, filename, contentpath):
        with open(Path(__file__).parent / contentpath, 'r') as file:
            self.write(filename, file.read())

    def write(self, filename, content):
        with open(Path(self.path) / filename, 'w') as file:
            file.write(content)


def main(input_path, output_path=None):
    input_stream = FileStream(input_path)
    lexer = ctx2lLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(DiagnosticErrorListener())
    lexer.addErrorListener(ThrowingErrorListener())
    stream = CommonTokenStream(lexer)
    parser = ctx2lParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(DiagnosticErrorListener())
    parser.addErrorListener(ThrowingErrorListener())
    tree = parser.program()
    visitor = ctx2lVisitor()
    ast = visitor.visit(tree)

    src_path = Path(input_path)
    pathname = src_path.parent
    name = src_path.stem
    evaluator = ctx2lEvaluator(name)
    generator = ctx2lPythonEvaluator(name, dependencies={ 'ThrowingErrorListener': 'ThrowingErrorListener' })
    lexerFile, parserFile = evaluator.eval(ast)
    visitorFile, visitorEvaluatorFile, mainFile = generator.eval(ast)

    dest_path = Path(output_path or pathname)
    writer = Writer(dest_path)

    writer.write_file('ThrowingErrorListener.py', 'ThrowingErrorListener.py')

    writer.write(f'{name}Lexer.g4', lexerFile)
    writer.write(f'{name}Parser.g4', parserFile)
    writer.write(f'{name}Visitor.py', visitorFile)
    writer.write(f'{name}VisitorEvaluator.py', visitorEvaluatorFile)
    writer.write('main.py', mainFile)

    process = subprocess.run(['antlr4', '-v', '4.13.0', dest_path / f'{name}Lexer.g4', dest_path / f'{name}Parser.g4', '-no-listener', '-visitor', '-Dlanguage=Python3', '-package', 'test'], capture_output=True)

    if process.stdout:
        raise SystemExit(process.stdout.decode()[:-1])
    

if __name__ == '__main__':
    main(*sys.argv[1:])
