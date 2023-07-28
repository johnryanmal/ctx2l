from antlr4 import *
from calculatorLexer import calculatorLexer
from calculatorParser import calculatorParser
from calculatorVisitor import calculatorVisitor
from calculatorEvaluator import calculatorEvaluator
from ThrowingErrorListener import ThrowingErrorListener


def _evaluate(input_stream, *args, **kwargs):
    lexer = calculatorLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())
    stream = CommonTokenStream(lexer)
    parser = calculatorParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())
    try:
        tree = parser.calculation()
    except ThrowingErrorListener.Exception as e:
        raise SyntaxError(e)
    evaluator = calculatorEvaluator(*args, **kwargs)
    visitor = calculatorVisitor(evaluator)
    result = visitor.visit(tree)
    return result

def evaluate(text, *args, **kwargs):
    return _evaluate(InputStream(text), *args, **kwargs)

def evaluate_file(path, *args, **kwargs):
    return _evaluate(FileStream(path), *args, **kwargs)
