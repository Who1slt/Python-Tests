import unittest
from classes.calculator import Calculator, State

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        """Тестирование операции сложения"""
        self.assertEqual(self.calc.add(17, 8), 25.0)
        self.assertEqual(self.calc.add(3.9, 6.1), 10.0)
        self.assertEqual(self.calc.add(-0.5, 30), 29.5)
    
    def test_subtraction(self):
        """Тестирование операции вычитания"""
        self.assertEqual(self.calc.subtraction(5, 7), -2.0)
        self.assertEqual(self.calc.subtraction(3.5, 3.5), 0.0)
        self.assertEqual(self.calc.subtraction(-7.3, -2.8), -4.5)
    
    def test_multiplication(self):
        """Тестирование операции умножения"""
        self.assertEqual(self.calc.multiplication(12, 2), 24.0)
        self.assertEqual(self.calc.multiplication(0.5, 0.25), 0.125)
        self.assertEqual(self.calc.multiplication(-0.5, -12), 6.0)
    
    def test_division(self):
        """Тестирование операции деления"""
        self.assertEqual(self.calc.division(48, 6), 8.0)
        self.assertEqual(self.calc.division(-0.5, 0.25), -2.0)
        self.assertEqual(self.calc.division(-12, -0.5), 24.0)
        self.assertEqual(self.calc.division(1234, 0), State.Error)