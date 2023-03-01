from itertools import chain

def extract(dict, keys):
    return {key: dict[key] for key in keys}

def retract(dict, keys):
    return extract(dict, dict.keys() - set(keys))

def destructure(dict, keys):
    return retract(dict, keys), *extract(dict, keys).values()

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

def pythonVisit(name, keys):
    return (
        f'def visit{cap(name)}(self, ctx):'
        + pythonBlock(
            'return ' + pythonObject(name, ((key, f'ctx.{key}()') for key in keys))
        )
    )


class Evaluator:
    def eval(self, node):
        node_, type_ = destructure(node, ['type'])
        attr = 'eval' + cap(type_)

        try:
            method = getattr(self, attr)
        except AttributeError:
            raise NotImplementedError(f'{self.__class__.__name__}.{attr}() was not implemented -- could not evaluate node {repr(type_)}')

        return method(**node_)

    def evals(self, nodes):
        return (self.eval(node) for node in nodes)

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
        return antlrRule(name, self.evals(alts))

    def evalProgram(self, *, tokens, rules, **_):
        tokenGrammar = newlines(2).join(self.evals(tokens))
        ruleGrammar = newlines(2).join(self.evals(rules))
        return tokenGrammar, ruleGrammar


class ctx2lPythonEvaluator(Evaluator):
    def evalLabel(self, *, id, **_):
        return id

    def evalAtom(self, *, label=None, **_):
        if label:
            return (self.eval(label),)
        return ()

    def evalAlt(self, *, atoms, **_):
        return chain.from_iterable(self.evals(atoms))

    def evalSub(self, *, alts, **_):
        return chain.from_iterable(self.evals(alts))

    def evalRule(self, *, name, alts, **_):
        items = set(chain.from_iterable(self.evals(alts)))
        return pythonVisit(name, items)

    def evalProgram(self, *, rules, **_):
        methods = newlines(2).join(self.evals(rules))
        return pythonBlock(methods)
