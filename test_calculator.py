# https://github.com/tayUF/lab11-TS-MD
# Partner 1: Taylor Schwartz
# Partner 2: Magnus Donis
import math
import unittest
from calculator import add, subtract, mul, div, logarithm, exp, hypotenuse, square_root

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(0, 3), -3)
        self.assertEqual(subtract(-2, -2), 0)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(5, 5), 25)
        self.assertEqual(mul(2, 9), 18)
    def test_divide(self):
        self.assertEqual(div(5, 2), 2.5)
        self.assertEqual(div(2, 2), 1)
        self.assertEqual(div(4, 2), 2)

    def test_divide_by_zero(self):
            with self.assertRaises(ZeroDivisionError):
                div(5, 0)



    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)

    def test_log_invalid_argument(self):
            with self.assertRaises(TypeError):
                logarithm('hello', 5)
            with self.assertRaises(TypeError):
                logarithm(2, '5')

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 3), math.sqrt(18))
        self.assertAlmostEqual(hypotenuse(4, 4), math.sqrt(32))
        self.assertAlmostEqual(hypotenuse(5, 5), math.sqrt(50))

    def test_sqrt(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(36), 6)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 5)
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
        with self.assertRaises(ValueError):
            logarithm(2, -8)