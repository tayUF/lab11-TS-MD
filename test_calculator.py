# https://github.com/tayUF/lab11-TS-MD
# Partner 1: Taylor Schwartz
# Partner 2: Magnus Donis

import pytest
import math
from calculator import add, sub, mul, div, logarithm, exp, hypotenuse, square_root

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert sub(5, 2) == 3
    assert sub(0, 3) == -3
    assert sub(-2, -2) == 0

def test_multiply():
    assert mul(5, 2) == 10
    assert mul(2, 2) == 4
    assert mul(4, 8) == 32
def test_divide():
    assert div(5, 2) == 2.5
    assert div(2, 2) == 1
    assert div(4, 8)  == 0.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)

def test_logarithm():
    assert math.isclose(logarithm(10, 100), 2)
    assert math.isclose(logarithm(2, 8), 3)

def test_log_invalid_argument():
    with pytest.raises(TypeError):
        logarithm('hello', 5)
    with pytest.raises(TypeError):
        logarithm(2, '5')

def test_hypotenuse():
    assert math.isclose(hypotenuse(3, 3), math.sqrt(18))
    assert math.isclose(hypotenuse(4, 4), math.sqrt(32))
    assert math.isclose(hypotenuse(5, 5), math.sqrt(50))

def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(36) == 6
def test_log_invalid_base():
    with pytest.raises(ValueError):
        logarithm(-1, 5)
    with pytest.raises(ValueError):
        logarithm(-2, 8)
    with pytest.raises(ValueError):
        logarithm(2, -8)
