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

    result = evaluate_file(*sys.argv[1:], env)
    
    if result:
        print(result)
