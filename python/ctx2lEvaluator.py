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
    if len(alts) > 1:
        return antlrRule(name, antlrLabeledAlts(name, alts))
    else:
        return antlrRule(name, alts)

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

def pythonAssign(key, value):
    return f'{key} = {value}'

def pythonVisitDefault(name, attrs):
    return (
        f'def visit{cap(name)}(self, ctx):'
        + block(
            'return ' + pythonObject(name, attrs)
        )
    )

def pythonVisitExpr(name, attrs, expr):
    return (
        f'def visit{cap(name)}(self, ctx):'
        + block(
            newlines().join([
                #f'print(\'{name}\')',
                *(pythonAssign(k, v) for k, v in attrs),
                'return' + spaced(expr)
            ])
        )
    )

def pythonVisit(name, attrs, expr=None):
    if expr is not None:
        return pythonVisitExpr(name, attrs, expr)
    else:
        return pythonVisitDefault(name, attrs)

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

    def evalLiteral(self, *, text, kind, **_):
        if kind == 'rule':
            self.programInfo['literal_tokens'].add(text)
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
        self.programInfo = {
            'literal_tokens': set()
        }
        tokenDefs = self.evals(tokens)
        ruleDefs = self.evals(rules)

        literals = sorted(self.programInfo['literal_tokens'])
        literals.sort(key=len, reverse=True)
        literalDefs = tuple(
            antlrRule(f'LITERAL__{index+1}', (literal,))
                for index, literal in enumerate(literals)
        )

        lexerName = f'{self.name}Lexer'
        parserName = f'{self.name}Parser'

        tokenGrammar = newlines(2).join([
            antlrHeader('lexer', lexerName),
            *tokenDefs,
            *literalDefs
        ])
        ruleGrammar = newlines(2).join([
            antlrHeader('parser', parserName),
            antlrOptions('options', {
                'tokenVocab': lexerName
            }.items()),
            *ruleDefs
        ])
        return tokenGrammar, ruleGrammar


class ctx2lPythonEvaluator(Evaluator):
    def __init__(self, name):
        self.name = name

    def evalLabel(self, *, id, **_):
        return id

    def evalCall(self, *, args=(), **_):
        return '(' + ', '.join(self.evals(args)) + ')'

    def evalExpr(self, *, external, id, call='', **_):
        if external:
            self.programInfo['imports'].add(id)
        return id + self.evalable(call)

    def evalLiteral(self, **_):
        id = self.atomInfo['id']
        return f'ctx.{id}.text'

    def evalRef(self, *, name, **_):
        id = self.atomInfo['id']
        if name[0].isupper():
            return f'ctx.{id}.text'
        else:
            return f'self.visit(ctx.{id})'

    def evalAtom(self, *, label=None, ebnf, **_):
        if label is None:
            return ()
        else:
            id = self.eval(label)
            self.atomInfo = {
                'id': id
            }
            value = self.eval(ebnf)
            return ((id, value),)

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

        visits = self.ruleInfo['visits']
        methods = []
        if len(visits) == 1:
            visit = visits[0]
            methods.append(pythonVisit(name, *visit))
        else:
            for index, visit in enumerate(self.ruleInfo['visits']):
                label = antlrLabel(name, index)
                methods.append(pythonVisit(label, *visit))

        return methods


    def evalProgram(self, *, rules, **_):
        self.programInfo = {
            'imports': set()
        }
        visitorMethods = newlines(2).join(chain(*self.evals(rules)))
        imports = sorted(self.programInfo['imports'])

        visitor = f'{self.name}Visitor'
        parserVisitor = f'{self.name}ParserVisitor'
        evaluator = f'{self.name}Evaluator'

        return (
            newlines().join([
                pythonFileImport(parserVisitor),
                pythonImports(evaluator, imports)
            ])
            + newlines(3)
            + pythonClass(
                visitor,
                (parserVisitor,),
                visitorMethods
            )
        )
