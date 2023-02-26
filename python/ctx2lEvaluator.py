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
    return quote(key) + ': ' + value + ','

def pythonDict(items):
    return (
        '{'
        + pythonBlock(
            newlines().join(pythonKeyValue(k, v) for k, v in items)
        )
        + '\n}'
    )

def pythonVisit(name, keys):
    return (
        f'def visit{cap(name)}(self, ctx):'
        + pythonBlock(
            'return ' + pythonDict((key, f'ctx.{key}') for key in keys)
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
        return tuple(self.eval(node) for node in nodes)


class ctx2lEvaluator(Evaluator):
    def evalLiteral(self, *, text):
        return text

    def evalAtom(self, *, ebnf, suffix):
        return self.eval(ebnf) + (suffix or '')

    def evalAlt(self, *, atoms):
        return spaces().join(self.evals(atoms))

    def evalSub(self, *, alts):
        return antlrSub(self.evals(alts))

    def evalToken(self, *, name, alts):
        return antlrRule(name, self.evals(alts))

    def evalRule(self, *, name, alts):
        return antlrRule(name, self.evals(alts))

    def evalProgram(self, *, tokens, rules):
        tokenDefs = self.evals(tokens)
        ruleDefs = self.evals(rules)
        tokenGrammar = newlines(2).join(tokenDefs)
        ruleGrammar = newlines(2).join(ruleDefs)
        return tokenGrammar, ruleGrammar


class ctx2lPythonEvaluator(Evaluator):
    def evalLiteral(self, *, text):
        return {text}

    def evalAtom(self, *, ebnf, suffix):
        return self.eval(ebnf)

    def evalAlt(self, *, atoms):
        return set.union(*self.evals(atoms))

    def evalSub(self, *, alts):
        return set.union(*self.evals(alts))

    def evalRule(self, *, name, alts):
        return pythonVisit(name, set.union(*self.evals(alts)))

    def evalProgram(self, *, tokens, rules):
        methods = newlines(2).join(self.evals(rules))
        return pythonBlock(methods)
