def extract(dict, keys):
    return {key: dict[key] for key in keys}

def retract(dict, keys):
    return extract(dict, dict.keys() - set(keys))

def destructure(dict, keys):
    return retract(dict, keys), *extract(dict, keys).values()

def spaces(n=1):
    return n*' '

def newlines(n=1):
    return n*'\n'

def indent(n, str):
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
        + spaced('|').join(map(spaced, alts))
        + spaced(')')
    )

class ctx2lEvaluator():
    def evalable(self, node):
        if type(node) is dict:
            return self.eval(node)
        else:
            return node

    def eval(self, node):
        node_, type_ = destructure(node, ['type'])
        attr = 'eval' + type_[0].upper() + type_[1:]
        if method := getattr(self, attr, None):
            return method(**node_)
        else:
            raise NotImplementedError(f'{repr(attr)} was not implemented in {self.__class__.__name__}')

    def evals(self, nodes):
        return tuple(self.eval(node) for node in nodes)

    def evalAtom(self, *, ebnf, suffix):
        return self.evalable(ebnf) + (suffix or '')

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
