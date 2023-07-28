#!/usr/bin/env python3
import sys
from runner import evaluate, evaluate_file


if __name__ == '__main__':
    if (files:=sys.argv[1:]):
        for file in files:
            result = evaluate_file(file)
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
                    result = evaluate(text)
                except SyntaxError as e:
                    print(e)
                else:
                    if result:
                        print(result)
