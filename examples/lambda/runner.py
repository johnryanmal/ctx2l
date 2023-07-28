from antlr4 import *
from lambdaLexer import lambdaLexer
from lambdaParser import lambdaParser
from lambdaVisitor import lambdaVisitor
from lambdaEvaluator import lambdaEvaluator
from ThrowingErrorListener import ThrowingErrorListener


def _evaluate(input_stream, *args, **kwargs):
    lexer = lambdaLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())
    stream = CommonTokenStream(lexer)
    parser = lambdaParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())
    try:
        tree = parser.calculus()
    except ThrowingErrorListener.Exception as e:
        raise SyntaxError(str(e))
    evaluator = lambdaEvaluator(*args, **kwargs)
    visitor = lambdaVisitor(evaluator)
    result = visitor.visit(tree)
    return result

def evaluate(text, *args, **kwargs):
    return _evaluate(InputStream(text), *args, **kwargs)

def evaluate_file(path, *args, **kwargs):
    return _evaluate(FileStream(path), *args, **kwargs)
