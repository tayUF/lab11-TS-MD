# https://github.com/tayUF/lab11-TS-MD
# Partner 1: Taylor Schwartz
# Partner 2: Magnus Donis

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
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid base or argument for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b


