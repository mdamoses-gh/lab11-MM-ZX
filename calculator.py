"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # Convention: divide a by b (a / b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def logarithm(a, b):
    """
    Compute log base a of b, i.e. log_a(b).
    We must reject invalid values:
    - base a <= 0
    - base a == 1
    - argument b <= 0
    """
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)


def exponent(a, b):
    # a raised to the power of b
    return a ** b

