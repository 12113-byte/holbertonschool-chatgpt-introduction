#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <non-negative integer>")
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)