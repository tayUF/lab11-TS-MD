# https://github.com/tayUF/lab11-TS-MD
# Partner 1: Taylor Schwartz
# Partner 2: Magnus Donis
import math
from calculator import add, subtract, mul, div, logarithm, exp, hypotenuse, square_root

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 3) == -3
    assert subtract(-2, -2) == 0

def test_multiply():
    assert mul(5, 2) == 10
    assert mul(2, 2) == 4
    assert mul(4, 8) == 32
def test_divide():
    assert div(5, 2) == 2.5
    assert div(2, 2) == 1
    assert div(4, 8)  == 0.5

def test_divide_by_zero():
    try:
        div(5, 0)
    except ZeroDivisionError:
        raise ZeroDivisionError


def test_logarithm():
    assert math.isclose(logarithm(10, 100), 2)
    assert math.isclose(logarithm(2, 8), 3)

def test_log_invalid_argument():
    try:
        logarithm('hello', 5)
        logarithm(2, '5')
    except TypeError:
        raise TypeError

def test_hypotenuse():
    assert math.isclose(hypotenuse(3, 3), math.sqrt(18))
    assert math.isclose(hypotenuse(4, 4), math.sqrt(32))
    assert math.isclose(hypotenuse(5, 5), math.sqrt(50))

def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(36) == 6
def test_log_invalid_base():
    try:
        logarithm(-1, 5)
        logarithm(-2, 8)
        logarithm(2, -8)
    except ValueError:
        raise ValueError
