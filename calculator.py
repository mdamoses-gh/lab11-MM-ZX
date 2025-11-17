"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/mdamoses-gh/lab11-MM-ZX.git
# Partner 1: Moises Miranda Manzanedo
# Partner 2: Ziyue Xu
import math
# First example
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        pass

def exp(a, b):
    return a ** b
