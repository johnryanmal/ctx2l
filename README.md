# ctx2l
ctx2l (pronounced "contextual") is a parser generator intended for use in small projects and prototypes.

ctx2l is an abstraction on top of [ANTLR](https://www.antlr.org/).
Its purpose is bind together parsing and evaluating in source code, so that both aspects are considered at the same time.

Rather than generating code directly, ctx2l is translated into a language agnostic ANTLR grammar and native code in a target language.
The grammar is used to generate a parser, and the native code is used to generate a visitor.
Because the parser generation is handled entirely by ANTLR, it may be more accurate to call ctx2l a "visitor generator."

## Installation
Currently, only python as a target language is supported.

### Python

1. Install ANTLR4

```shell
pip install antlr4-python3-runtime
pip install antlr4-tools
```

2. Clone the reponsitory
```shell
git clone https://github.com/johnryanmal/ctx2l ~/ctx2l
```

3. Update rc file

`.zshrc`
```zsh
echo 'alias ctx2l="python ~/ctx2l/python/main.py"' >> ~/.zshrc
```

After restarting your shell, you should be able to use the `ctx2l` command.

## Updating
1. Pull from the repository
```shell
git -C ~/ctx2l pull origin main
```

## Usage

### Command Line
`ctx2l <file> [output directory]`

Generates a lexer, parser, and visitor from a `.ctx2l` source file.

| Option | Description |
| --- | --- |
| `file` | The `.ctx2l` file to generate from. |
| `output directory` | The directory where all output is generated. |

### Source

At minimum, three files are needed to generate a working program.

- A ctx2l file (grammar)
- An evaluator file (functionality)
- An input file (text)

### Example ([source](/examples/calculator))

`calculator.ctx2l`

```antlr
expr:
| V=sum -> V

sum:
| V=prod -> V
| L=prod '+' R=sum -> $add(L, R)
| L=prod '-' R=sum -> $sub(L, R)

prod:
| V=pow -> V
| L=pow '*' R=prod -> $mul(L, R)
| L=pow '/' R=prod -> $div(L, R)

pow:
| V=value -> V
| L=value '**' R=pow -> $pow(L, R)

value:
| '(' V=expr ')' -> V
| V=DIGITS -> $num(V)

DIGITS:
| [0-9]+

WS >> skip:
| [ \t\r\n\f]+
```

`calculatorEvaluator.py`

```py
from calculatorVisitorEvaluator import calculatorVisitorEvaluator

class calculatorEvaluator(calculatorVisitorEvaluator):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def pow(self, x, y):
        return x ** y

    def num(self, str):
        return int(str)
```

`sample.txt`

```rb
14 / (2 + 5) - 7 * 3
```

With these three files in a single directory, a single command generates the needed files to make this work:
```shell
ctx2l calculator.ctx2l
```

The generated `main.py` file can be run like so:
```shell
python main.py sample.txt
```

And the correct output is given:
```shell
$ ctx2l calculator.ctx2l
$ python main.py sample.txt
-19.0
```
