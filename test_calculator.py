# https://github.com/tayUF/lab11-TS-MD
# Partner 1: Taylor Schwartz
# Partner 2: Magnus Donis

import pytest
import math
from calculator import add, sub, mul, div, log, exp

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert sub(5, 2) == 3
    assert sub(0, 3) == -3
    assert sub(-2, -2) == 0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)

def test_logarithm():
    assert math.isclose(log(10, 100), 2)
    assert math.isclose(log(2, 8), 3)

def test_log_invalid_base():
    with pytest.raises(ValueError):
        log(1, 5)
    with pytest.raises(ValueError):
        log(-2, 8)
    with pytest.raises(ValueError):
        log(2, -8)
