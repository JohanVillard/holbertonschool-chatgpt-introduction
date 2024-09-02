#!/usr/bin/python3
import sys


def factorial(n):
    """Compute recursively."""
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


f = factorial(int(sys.argv[1]))
print(f)
