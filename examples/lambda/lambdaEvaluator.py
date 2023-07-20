from lambdaVisitorEvaluator import lambdaVisitorEvaluator


class lambdaEvaluator(lambdaVisitorEvaluator):
    def symbol(self, name):
        return {
            'type': 'symbol',
            'name': name
        }

    def abstract(self, bind, expr):
        return {
            'type': 'abstract',
            'bind': bind,
            'expr': expr
        }

    def apply(self, func, arg):
        return {
            'type': 'apply',
            'func': func,
            'arg': arg
        }

    def eval(self, ast):
        return lambdaEval(ast)


def lambdaEval(ast):

    class Abstraction:
        def __init__(self, bind, expr, env):
            self.bind = bind
            self.expr = expr
            self.env = env

        def __call__(self, arg):
            return _lambdaEval(self.expr, {**self.env, self.bind: arg})

        def __repr__(self):
            return f'\\{self.bind}.{self.__call__(self.bind)}'


    class Application:
        def __init__(self, func, arg):
            self.func = func
            self.arg = arg
        
        def __repr__(self):
            if type(self.arg) in [Abstraction, Application]:
                return f'{self.func} ({self.arg})'
            else:
                return f'{self.func} {self.arg}'


    def _lambdaEval(node, env):
        eval_type = node['type']

        if eval_type == 'symbol':
            name = node['name']

            return env[name] if name in env else name

        elif eval_type == 'abstract':
            bind = node['bind']
            expr = node['expr']

            return Abstraction(bind, expr, env)

        elif eval_type == 'apply':
            func = node['func']
            arg = node['arg']

            eval_func = _lambdaEval(func, env)
            eval_arg = _lambdaEval(arg, env)

            if type(eval_func) is Abstraction:
                return eval_func(eval_arg)
            else:
                return Application(eval_func, eval_arg)

        else:
            raise ValueError('Invalid lambda AST node')

    return _lambdaEval(ast, {})
