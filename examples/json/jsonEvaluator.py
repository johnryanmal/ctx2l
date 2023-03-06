from jsonVisitorEvaluator import jsonVisitorEvaluator

class jsonEvaluator(jsonVisitorEvaluator):
    def pair(self, key, value):
        return key, value
    
    def dict(self, pairs):
        return dict(pairs)

    def unquote(self, str):
        return str[1:-1]
