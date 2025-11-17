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
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        pass

def log(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        pass

def exp(a, b):
    return a ** b

