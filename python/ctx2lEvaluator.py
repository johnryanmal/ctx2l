from itertools import chain

def cap(str):
    return str[:1].upper() + str[1:]

def spaces(n=1):
    return n*' '

def newlines(n=1):
    return n*'\n'

def indent(n, str=''):
    return '\n' + spaces(n) + str

def spaced(str):
    if str:
        return ' ' + str
    else:
        return str

def antlrLabel(name, index):
    return f'__{name}__{index+1}'

def antlrLabeledAlt(name, index, alt):
    return f'{alt} #{antlrLabel(name, index)}'

def antlrLabeledAlts(name, alts):
    return tuple(antlrLabeledAlt(name, index, alt) for index, alt in enumerate(alts))

def antlrLabeledRule(name, alts):
    return antlrRule(name, antlrLabeledAlts(name, alts))

def antlrRule(name, alts):
    return (
        name
        + indent(3, ':')
        + indent(3, '|').join(map(spaced, alts))
        + indent(3, ';')
    )

def antlrSub(alts):
    return (
        '('
        + ' |'.join(map(spaced, alts))
        + ' )'
    )

def quote(str):
    return "'" + str + "'"

def pythonIndent(str=''):
    return indent(4, str)

def pythonBlock(str):
    return pythonIndent() + str.replace('\n', pythonIndent())

def pythonKeyValue(key, value):
    return f'{quote(key)}: {value},'

def pythonDict(items):
    pairs = tuple(pythonKeyValue(k, v) for k, v in items)
    if pairs:
        return (
            '{'
            + pythonBlock(newlines().join(pairs))
            + '\n}'
        )
    else:
        return '{}'

def pythonKwarg(key, value):
    return f'{key}={value},'

def pythonKwargs(kwargs):
    return newlines().join(pythonKwarg(k, v) for k, v in kwargs)

def pythonObject(name, items):
    return f"type('{name}', (), {pythonDict(items)})()"

def pythonVisit(name, attrs):
    return (
        f'def visit{cap(name)}(self, ctx):'
        + pythonBlock(
            'return ' + pythonObject(name, attrs)
        )
    )

def pythonAssign(key, value):
    return f'{key} = {value}'

def pythonVisitExpr(name, attrs, expr):
    return (
        f'def visit{cap(name)}(self, ctx):'
        + pythonBlock(
            newlines().join([*(pythonAssign(k, v) for k, v in attrs), 'return' + spaced(expr)])
        )
    )


class Evaluator:
    def eval(self, node):
        type_ = node['type']
        attr = 'eval' + cap(type_)

        try:
            method = getattr(self, attr)
        except AttributeError:
            raise NotImplementedError(f'{self.__class__.__name__}.{attr}() was not implemented -- could not evaluate node {repr(type_)}')

        return method(**node)

    def evals(self, nodes):
        return tuple(self.eval(node) for node in nodes)

    def evalable(self, node):
        if type(node) is dict:
            return self.eval(node)
        else:
            return node


class ctx2lEvaluator(Evaluator):
    def evalLiteral(self, *, text, **_):
        return text

    def evalRef(self, *, name, **_):
        return name

    def evalLabel(self, *, id, op, **_):
        return id + op

    def evalAtom(self, *, label='', ebnf, suffix='', **_):
        return self.evalable(label) + self.eval(ebnf) + suffix

    def evalAlt(self, *, atoms, **_):
        return spaces().join(self.evals(atoms))

    def evalSub(self, *, alts, **_):
        return antlrSub(self.evals(alts))

    def evalToken(self, *, name, alts, **_):
        return antlrRule(name, self.evals(alts))

    def evalRule(self, *, name, alts, **_):
        return antlrLabeledRule(name, self.evals(alts))

    def evalProgram(self, *, tokens, rules, **_):
        tokenGrammar = newlines(2).join(self.evals(tokens))
        ruleGrammar = newlines(2).join(self.evals(rules))
        return tokenGrammar, ruleGrammar


class ctx2lPythonEvaluator(Evaluator):
    def __init__(self):
        self.info = []

    def evalLabel(self, *, id, **_):
        return id

    def evalCall(self, *, args=[], **_):
        return '(' + ', '.join(self.evals(args)) + ')'

    def evalExpr(self, *, id, call='', **_):
        return id + self.evalable(call)

    def evalAtom(self, *, label=None, **_):
        if label:
            id = self.eval(label)
            return ((id, f'ctx.{id}()'),)
        return ()

    def evalAlt(self, *, atoms, expr=None, **_):
        attrs = tuple(chain.from_iterable(self.evals(atoms)))
        self.info.append((attrs, self.evalable(expr)))
        return attrs

    def evalSub(self, *, alts, **_):
        return chain.from_iterable(self.evals(alts))

    def evalRule(self, *, name, alts, **_):
        self.evals(alts)
        methods = []
        for index, args in enumerate(self.info):
            attrs, expr = args
            label = antlrLabel(name, index)
            if expr is None:
                methods.append(pythonVisit(label, attrs))
            else:
                methods.append(pythonVisitExpr(label, attrs, expr))
        self.info = []
        return methods

    def evalProgram(self, *, rules, **_):
        return pythonBlock(newlines(2).join(chain.from_iterable(self.evals(rules))))
