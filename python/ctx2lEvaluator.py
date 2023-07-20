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

def antlrDirectedRule(name, alts, commands):
    return (
        name + ':'
        + indent(2, '(')
        + indent(2, '|').join(map(spaced, alts))
        + indent(2, ')') + ' -> ' + listed(commands) + ';'
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

def pythonCall(func, arg=''):
    return f'{func}({arg})'

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
        return indent() + 'pass'

def pythonClass(name, bases=None, body=None):
    inherit = '' if bases is None else pythonTuple(bases)
    return (
        f'class {name}{inherit}:'
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
        if ebnf['type'] == 'sub':
            return self.eval(ebnf) + suffix
        else:
            return self.evalable(label) + self.eval(ebnf) + suffix

    def evalAlt(self, *, atoms, **_):
        return spaces().join(self.evals(atoms))

    def evalSub(self, *, alts, **_):
        return antlrSub(self.evals(alts))

    def evalToken(self, *, name, alts, cmds=None, **_):
        if cmds:
            return antlrDirectedRule(name, self.evals(alts), cmds)
        else:
            return antlrRule(name, self.evals(alts))

    def evalRule(self, *, name, alts, **_):
        return antlrLabeledRule(name, self.evals(alts))

    def evalProgram(self, *, tokens, rules, **_):
        self.programInfo = {
            'literal_tokens': set(),
            'unused_tokens': set()
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
    def __init__(self, name, dependencies={}):
        self.name = name
        self.dependencies = dependencies

    def evalLabel(self, *, id, op, **_):
        return id, ('list' if op == '+=' else 'value')

    def evalCall(self, *, args=(), **_):
        return '(' + ', '.join(self.evals(args)) + ')'

    def evalExpr(self, *, external, id, call='', **_):
        expr = id + self.evalable(call)
        if external:
            self.programInfo['externals'].add(id)
            return f'self.evaluator.{expr}'
        else:
            return expr

    def evalLiteral(self, **_):
        id = self.atomInfo['id']
        kind = self.atomInfo['kind']
        if kind == 'value':
            return (id, f'ctx.{id}.text'),
        elif kind == 'list':
            return (id, f'tuple(token.text for token in ctx.{id})'),
        else:
            return ()

    def evalRef(self, *, name, **_):
        if name[0].isupper():
            return self.evalLiteral()

        id = self.atomInfo['id']
        kind = self.atomInfo['kind']
        if kind == 'value':
            return (id, f'self.visit(ctx.{id})'),
        elif kind == 'list':
            return (id, f'tuple(self.visit(rule) for rule in ctx.{id})'),
        else:
            return ()

    def evalAtom(self, *, label=None, ebnf, **_):
        if label is None:
            id, kind = None, None
        else:
            id, kind = self.eval(label)

        self.atomInfo = {
            'id': id,
            'kind': kind
        }
        return self.eval(ebnf)

    def evalAlt(self, *, atoms, expr=None, **_):
        attrs = dict(chain(*self.evals(atoms))).items()
        return attrs, self.evalable(expr)

    def evalSub(self, *, alts, **_):
        id = self.atomInfo['id']
        alt_attrs, _ = zip(*self.evals(alts))
        attrs = dict(chain(*alt_attrs)).items()
        if id is not None:
            return (id, pythonObject(id, attrs)),
        else:
            return attrs

    def evalRule(self, *, name, alts, **_):
        if self.programInfo['start_rule'] is None:
            self.programInfo['start_rule'] = name

        visits = self.evals(alts)
        methods = []
        if len(visits) == 1:
            visit = visits[0]
            methods.append(pythonVisit(name, *visit))
        else:
            for index, visit in enumerate(visits):
                label = antlrLabel(name, index)
                methods.append(pythonVisit(label, *visit))

        return methods

    def evalProgram(self, *, rules, **_):
        self.programInfo = {
            'start_rule': None,
            'externals': set()
        }
        visitorMethods = newlines(2).join(chain(*self.evals(rules)))
        start_rule = self.programInfo['start_rule']
        externals = sorted(self.programInfo['externals'])

        lexer = f'{self.name}Lexer'
        parser = f'{self.name}Parser'
        parserVisitor = f'{self.name}ParserVisitor'
        visitor = f'{self.name}Visitor'
        visitorEvaluator = f'{self.name}VisitorEvaluator'
        evaluator = f'{self.name}Evaluator'

        visitorModule = (
            newlines().join([
                pythonFileImport(parserVisitor),
                pythonFileImport(evaluator),
            ])
            + newlines(3)
            + pythonClass(
                visitor,
                (parserVisitor,),
                (
                    'def __init__(self):'
                    + block(
                        pythonAssign('self.evaluator', f'{evaluator}()')
                    )
                    + newlines(2)
                    + visitorMethods
                )
            )
            + '\n'
        )
        visitorEvaluatorModule = (
            pythonClass(
                visitorEvaluator,
                (),
                (
                    newlines(2).join(
                        (
                            f'def {external}(self, *_):'
                            + block(
                                'raise NotImplementedError'
                            )
                        )
                        for external
                        in externals
                    )
                )
            )
            + '\n'
        )
        mainModule = (
            newlines().join([
                pythonImport('sys'),
                pythonImport('antlr4', '*'),
                pythonFileImport(lexer),
                pythonFileImport(parser),
                pythonFileImport(visitor),
                *(pythonImport(module, key) for module, key in self.dependencies.items())
            ])
            + newlines(3)
            + 'def main(path):'
            + block(
                newlines().join([
                    pythonAssign('input_stream', 'FileStream(path)'),
                    pythonAssign('lexer', f'{lexer}(input_stream)'),
                    pythonCall('lexer.removeErrorListeners'),
                    pythonCall('lexer.addErrorListener', 'ThrowingErrorListener()'),
                    pythonAssign('stream', 'CommonTokenStream(lexer)'),
                    pythonAssign('parser', f'{parser}(stream)'),
                    pythonCall('parser.removeErrorListeners'),
                    pythonCall('parser.addErrorListener', 'ThrowingErrorListener()'),
                    pythonAssign('tree', f'parser.{start_rule}()'),
                    pythonAssign('visitor', f'{visitor}()'),
                    pythonAssign('result', 'visitor.visit(tree)'),
                    pythonCall('print', 'result')
                ])
            )
            + newlines(3)
            + "if __name__ == '__main__':"
            + block(
                'main(*sys.argv[1:])'
            )
            + '\n'
        )
        return visitorModule, visitorEvaluatorModule, mainModule
