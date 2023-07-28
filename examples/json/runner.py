from antlr4 import *
from jsonLexer import jsonLexer
from jsonParser import jsonParser
from jsonVisitor import jsonVisitor
from jsonEvaluator import jsonEvaluator
from ThrowingErrorListener import ThrowingErrorListener


def _evaluate(input_stream, *args, **kwargs):
    lexer = jsonLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())
    stream = CommonTokenStream(lexer)
    parser = jsonParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())
    try:
        tree = parser.json()
    except ThrowingErrorListener.Exception as e:
        raise SyntaxError(str(e))
    evaluator = jsonEvaluator(*args, **kwargs)
    visitor = jsonVisitor(evaluator)
    result = visitor.visit(tree)
    return result

def evaluate(text, *args, **kwargs):
    return _evaluate(InputStream(text), *args, **kwargs)

def evaluate_file(path, *args, **kwargs):
    return _evaluate(FileStream(path), *args, **kwargs)
