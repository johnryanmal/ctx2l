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

def pythonCall(func, *args):
    return f'{func}({listed(args)})'

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

def pythonDef(name, params=None, body=None):
    paramdef = '()' if params is None else pythonTuple(params)
    return (
        f'def {name}{paramdef}:'
        + pythonBlock(body)
    )

def pythonReturn(val):
    return f'return {val}'

def pythonClass(name, bases=None, body=None):
    inherit = '' if bases is None else pythonTuple(bases)
    return (
        f'class {name}{inherit}:'
        + pythonBlock(body)
    )

def pythonShebang():
    return '#!/usr/bin/env python3\n'

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

    def evalAtom(self, *, label='', term, suffix='', **_):
        if term['type'] == 'sub':
            return self.eval(term) + suffix
        else:
            return self.evalable(label) + self.eval(term) + suffix

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
        self.atomInfo['id'] = id
        self.atomInfo['kind'] = 'list' if op == '+=' else 'value'

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

    def evalAtom(self, *, label=None, term, **_):
        self.atomInfo = {
            'id': None,
            'kind': None
        }
        self.evalable(label)
        return self.eval(term)

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
        runner = 'runner'

        visitorModule = (
            newlines().join([
                pythonFileImport(parserVisitor)
            ])
            + newlines(3)
            + pythonClass(
                visitor,
                (parserVisitor,),
                (
                    'def __init__(self, evaluator):'
                    + block(
                        pythonAssign('self.evaluator', 'evaluator')
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
        runnerModule = (
            newlines().join([
                pythonImport('antlr4', '*'),
                pythonFileImport(lexer),
                pythonFileImport(parser),
                pythonFileImport(visitor),
                pythonFileImport(evaluator),
                *(pythonImport(module, key) for module, key in self.dependencies.items())
            ])
            + newlines(3)
            + newlines(2).join([
                pythonDef('_evaluate', ('input_stream', '*args', '**kwargs'), (
                    newlines().join([
                        pythonAssign('lexer', f'{lexer}(input_stream)'),
                        pythonCall('lexer.removeErrorListeners'),
                        pythonCall('lexer.addErrorListener', 'ThrowingErrorListener()'),
                        pythonAssign('stream', 'CommonTokenStream(lexer)'),
                        pythonAssign('parser', f'{parser}(stream)'),
                        pythonCall('parser.removeErrorListeners'),
                        pythonCall('parser.addErrorListener', 'ThrowingErrorListener()'),
                        'try:'
                        + pythonBlock(
                            pythonAssign('tree', f'parser.{start_rule}()'),
                        ),
                        'except ThrowingErrorListener.Exception as e:'
                        + pythonBlock(
                            'raise SyntaxError(e)'
                        ),
                        pythonAssign('evaluator', f'{evaluator}(*args, **kwargs)'),
                        pythonAssign('visitor', f'{visitor}(evaluator)'),
                        pythonAssign('result', 'visitor.visit(tree)'),
                        pythonReturn('result')
                    ])
                )),
                pythonDef('evaluate', ('text', '*args', '**kwargs'), (
                    pythonReturn(
                        pythonCall('_evaluate', pythonCall('InputStream', 'text'), '*args', '**kwargs')
                    )
                )),
                pythonDef('evaluate_file', ('path', '*args', '**kwargs'), (
                    pythonReturn(
                        pythonCall('_evaluate', pythonCall('FileStream', 'path'), '*args', '**kwargs')
                    )
                ))
            ])
            + '\n'
        )
        mainModule = (
            pythonShebang()
            + newlines().join([
                pythonImport('sys'),
                pythonImports(runner, ['evaluate', 'evaluate_file'])
            ])
            + newlines(3)
            + "if __name__ == '__main__':"
            + pythonBlock(
                newlines().join([
                    'if (files:=sys.argv[1:]):'
                    + pythonBlock(
                        'for file in files:'
                        + pythonBlock(
                            newlines().join([
                                pythonAssign('result', pythonCall('evaluate_file', 'file')),
                                'if result:'
                                + pythonBlock(
                                    pythonCall('print', 'result')
                                )
                            ])
                        )
                    )
                ])
                + newlines(2)
                + 'else:'
                + pythonBlock(
                    'while True:'
                    + pythonBlock(
                        newlines().join([
                            'try:'
                            + pythonBlock(
                                pythonAssign('text', pythonCall('input', "'> '"))
                            ),
                            'except KeyboardInterrupt:'
                            + pythonBlock(
                                pythonCall('print')
                            ),
                            'except EOFError:'
                            + pythonBlock(
                                newlines().join([
                                    pythonCall('print'),
                                    'break'
                                ])
                            ),
                            'else:'
                            + pythonBlock(
                                newlines().join([
                                    'try:'
                                    + pythonBlock(
                                        pythonAssign('result', pythonCall('evaluate', 'text'))
                                    ),
                                    'except SyntaxError as e:'
                                    + pythonBlock(
                                        pythonCall('print', 'e')
                                    ),
                                    'else:'
                                    + pythonBlock(
                                        newlines().join([
                                            'if result:'
                                            + pythonBlock(
                                                pythonCall('print', 'result')
                                            )
                                        ])
                                    )
                                ])
                            )

                        ])
                    )
                )
            )
            + '\n'
        )
        return visitorModule, visitorEvaluatorModule, runnerModule, mainModule
