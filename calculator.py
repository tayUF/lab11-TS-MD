"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError as valError:
        raise valError
def hypotenuse(a, b):
    try:
        return math.sqrt(a**2 + b**2)
    except ValueError as valError:
        raise valError
# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as zeroDivError:
        raise zeroDivError
def log(a, b):
    try:
        return math.log(b, a)
    except ValueError as valError:
        raise valError
def exp(a, b):
    return a ** b

square_root(-5)

