from calculatorVisitorEvaluator import calculatorVisitorEvaluator

class calculatorEvaluator(calculatorVisitorEvaluator):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def pow(self, x, y):
        return x ** y

    def num(self, str):
        return int(str)
