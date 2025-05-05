#!/usr/bin/python3
import sys

def factorial(n):
        """
        Calculates the factorial of a given integer n.

        Args:
                n (int): The number to calculate the factorial of.

        Returns:
                int: The factorial of n.
        """
        if n == 0:
                return 1
        else:
                return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
