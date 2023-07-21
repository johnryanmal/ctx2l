#!/usr/bin/env python3
import sys
from runner import evaluate, evaluate_file
import lambdaEnv

if __name__ == '__main__':
    env = {
        name: evaluate(getattr(lambdaEnv, name))
        for name
        in dir(lambdaEnv)
        if not name.startswith("__")
    }

    result = evaluate_file(*sys.argv[1:], env)
    
    if result:
        print(result)
