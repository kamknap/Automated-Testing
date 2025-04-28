import unittest
from calculator import Calculator
from test.data import deltaTestCases

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -3), -4)
        self.assertEqual(self.calc.add(-1, 500), 499)

    def test_substract(self):
        self.assertEqual(self.calc.substract(1, 2), -1)
        self.assertEqual(self.calc.substract(-1, -3), 2)
        self.assertEqual(self.calc.substract(-1, 500), -501)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(-2, -30), 60)
        self.assertEqual(self.calc.substract(-1, 500), -501)

    def test_divide(self):
        self.assertEqual(self.calc.divide(1, 2), 0.5)
        self.assertEqual(self.calc.divide(-30, -2), 15)
        with self.assertRaises(ValueError):
            self.calc.divide(1,0)

    def test_delta(self):
        for case in deltaTestCases:
            if len(case) == 3:
                with self.assertRaises(ValueError):
                    self.calc.delta(*case)
            elif len(case) == 4:
                a, b, c, expected = case
                self.assertEqual(self.calc.delta(a, b, c), expected)