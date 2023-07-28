#!/usr/bin/env python3
import sys
from runner import evaluate, evaluate_file
import lambdaEnv

if __name__ == '__main__':
    attrs = {
        name: getattr(lambdaEnv, name)
        for name in dir(lambdaEnv)
        if not name.startswith("__")
    }

    env = {}
    for name, value in attrs.items():
        env[name] = evaluate(value, env)

    if (files:=sys.argv[1:]):
        for file in files:
            result = evaluate_file(file, env)
            if result:
                print(result)

    else:
        while True:
            try:
                text = input('> ')
            except KeyboardInterrupt:
                print()
            except EOFError:
                print()
                break
            else:
                try:
                    result = evaluate(text, env)
                except SyntaxError as e:
                    print(e)
                else:
                    if result:
                        print(result)
