from itertools import chain

def cap(str):
    return str[:1].upper() + str[1:]

def spaces(n=1):
    return n*' '

def newlines(n=1):
    return n*'\n'

def indent(n=4, str=''):
    return '\n' + spaces(n) + str

def block(str):
    return indent() + str.replace('\n', indent())

def table(iterable):
    if items := tuple(iterable):
        return (
            '{'
            + block(newlines().join(items))
            + '\n}'
        )
    else:
        return '{}'

def listed(strs):
    return ', '.join(strs) if strs else ''

def spaced(str):
    if str:
        return ' ' + str
    else:
        return str

def antlrLabel(name, index):
    return f'{name}__{index+1}'

def antlrLabeledAlt(name, index, alt):
    return f'{alt} #{antlrLabel(name, index)}'

def antlrLabeledAlts(name, alts):
    return tuple(antlrLabeledAlt(name, index, alt) for index, alt in enumerate(alts))

def antlrLabeledRule(name, alts):
    return antlrRule(name, antlrLabeledAlts(name, alts))

def antlrRule(name, alts):
    return (
        name
        + indent(2, ':')
        + indent(2, '|').join(map(spaced, alts))
        + indent(2, ';')
    )

def antlrSub(alts):
    return (
        '('
        + ' |'.join(map(spaced, alts))
        + ' )'
    )

def antlrHeader(grammar, name):
    return f'{grammar} grammar {name};'

def antlrOption(key, value):
    return f'{key} = {value};'

def antlrOptions(title, items):
    return title + spaced(table(antlrOption(k, v) for k, v in items))

def quote(str):
    return "'" + str + "'"

def pythonKeyValue(key, value):
    return f'{quote(key)}: {value},'

def pythonDict(items):
    return table(pythonKeyValue(k, v) for k, v in items)

def pythonKwarg(key, value):
    return f'{key}={value},'

def pythonKwargs(kwargs):
    return newlines().join(pythonKwarg(k, v) for k, v in kwargs)

def pythonObject(name, items):
    return f"type('{name}', (), {pythonDict(items)})()"

def pythonVisit(name, attrs):
    return (
        f'def visit{cap(name)}(self, ctx):'
        + block(
            'return ' + pythonObject(name, attrs)
        )
    )

def pythonAssign(key, value):
    return f'{key} = {value}'

def pythonVisitExpr(name, attrs, expr):
    return (
        f'def visit{cap(name)}(self, ctx):'
        + block(
            newlines().join([
                *(pythonAssign(k, v) for k, v in attrs),
                'return' + spaced(expr)
            ])
        )
    )

def pythonImport(module, key=None):
    if key:
        return f'from {module} import {key}'
    else:
        return f'import {module}'

def pythonImports(module, keys):
    return pythonImport(module, listed(keys))

def pythonFileImport(file):
    return pythonImport(file, file)

def pythonTuple(strs):
    return '(' + listed(strs) + ')'

def pythonBlock(body):
    if body:
        return block(body)
    else:
        return indent('pass')

def pythonClass(name, bases=(), body=None):
    return (
        f'class {name}{pythonTuple(bases)}:'
        + pythonBlock(body)
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
    def __init__(self, name):
        self.name = name

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
        lexerName = f'{self.name}Lexer'
        parserName = f'{self.name}Parser'
        tokenGrammar = newlines(2).join([
            antlrHeader('lexer', lexerName),
            *self.evals(tokens)
        ])
        ruleGrammar = newlines(2).join([
            antlrHeader('parser', parserName),
            antlrOptions('options', {
                'tokenVocab': lexerName
            }.items()),
            *self.evals(rules)
        ])
        return tokenGrammar, ruleGrammar


class ctx2lPythonEvaluator(Evaluator):
    def __init__(self, name):
        self.name = name

    def evalLabel(self, *, id, **_):
        return id

    def evalCall(self, *, args=(), **_):
        return '(' + ', '.join(self.evals(args)) + ')'

    def evalExpr(self, *, id, call='', **_):
        if applied := self.evalable(call):
            self.programInfo['imports'].add(id)
            return id + applied
        else:
            return id

    def evalAtom(self, *, label=None, **_):
        if label:
            id = self.eval(label)
            return ((id, f'ctx.{id}'),)
        return ()

    def evalAlt(self, *, atoms, expr=None, **_):
        attrs = tuple(chain(*self.evals(atoms)))
        self.ruleInfo['visits'].append((attrs, self.evalable(expr)))
        return attrs

    def evalSub(self, *, alts, **_):
        return chain(*self.evals(alts))

    def evalRule(self, *, name, alts, **_):
        self.ruleInfo = {
            'visits': []
        }
        self.evals(alts)

        methods = []
        for index, visit in enumerate(self.ruleInfo['visits']):
            label = antlrLabel(name, index)
            attrs, expr = visit
            if expr is None:
                methods.append(pythonVisit(label, attrs))
            else:
                methods.append(pythonVisitExpr(label, attrs, expr))
        return methods

    def evalProgram(self, *, rules, **_):
        self.programInfo = {
            'imports': set()
        }
        visitorMethods = newlines(2).join(chain(*self.evals(rules)))

        visitor = f'{self.name}Visitor'
        parserVisitor = f'{self.name}ParserVisitor'
        evaluator = f'{self.name}Evaluator'

        return (
            newlines().join([
                pythonFileImport(parserVisitor),
                pythonImports(evaluator, self.programInfo['imports'])
            ])
            + newlines(3)
            + pythonClass(
                visitor,
                (parserVisitor,),
                visitorMethods
            )
        )
