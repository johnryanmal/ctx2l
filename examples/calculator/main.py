#!/usr/bin/env python3
import sys
from runner import evaluate_file


if __name__ == '__main__':
    result = evaluate_file(*sys.argv[1:])
    
    if result:
        print(result)
