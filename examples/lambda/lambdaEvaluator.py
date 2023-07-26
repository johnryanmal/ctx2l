from lambdaVisitorEvaluator import lambdaVisitorEvaluator


class lambdaEvaluator(lambdaVisitorEvaluator):
    def __init__(self, env=None):
        self.env = env or {}

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
        return lambdaEval(ast, self.env)


def is_digit(char):
    return '0' <= char <= '9'

def mangle(name, env):
    if name not in env:
        return name
    cursor = len(name)
    while cursor >= 0 and is_digit(name[cursor-1]):
        cursor -= 1
    symbol = name[:cursor]
    index = name[cursor:] or '1'
    return symbol + str(int(index) + 1)


class Abstraction:
    def __init__(self, bind, expr, env):
        self.bind = bind
        self.expr = expr
        self.env = env

    def __call__(self, arg):
        return lambdaEval(self.expr, {**self.env, self.bind: arg})

    def repr(self, env):
        repr_bind = mangle(self.bind, env)
        repr_env = {**env, repr_bind: repr_bind}
        value = self(repr_bind)
        repr_expr = value if type(value) is str else value.repr(repr_env)
        return f'\\{repr_bind}.{repr_expr}'

    def __repr__(self):
        return self.repr({})


class Application:
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg

    def repr(self, env):
        repr_func = self.func if type(self.func) is str else self.func.repr(env)
        repr_arg = self.arg if type(self.arg) is str else self.arg.repr(env)
        if type(self.arg) in [Abstraction, Application]:
            return f'{repr_func} ({repr_arg})'
        else:
            return f'{repr_func} {repr_arg}'
    
    def __repr__(self):
        return self.repr({})


def lambdaEval(node, env):
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

        eval_func = lambdaEval(func, env)
        eval_arg = lambdaEval(arg, env)

        if type(eval_func) is Abstraction:
            return eval_func(eval_arg)
        else:
            return Application(eval_func, eval_arg)

    else:
        raise ValueError('Invalid lambda AST node')
