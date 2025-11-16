# https://github.com/tayUF/lab11-TS-MD
# Partner 1: Taylor Schwartz
# Partner 2: Magnus Donis

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
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as zeroDivError:
        raise zeroDivError
def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError as valError:
        raise valError
def exp(a, b):
    return a ** b

