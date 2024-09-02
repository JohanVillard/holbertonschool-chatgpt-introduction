#!/usr/bin/python3
import sys


def factorial(n):
    """
    Compute the factorial of n.

    Function Description:
    ----------------------
    This function calculates the factorial of a non-negative integer n using recursion.
    The factorial of a number n (denoted as n!) is the product of all positive integers
    less than or equal to n. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.

    Parameters:
    -----------
    n : int
        A non-negative integer whose factorial is to be computed.
        Must be an integer greater than or equal to 0.

    Returns:
    --------
    int
        The factorial of the input integer n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Read the command-line argument, compute the factorial, and print the result.
f = factorial(int(sys.argv[1]))
print(f)
