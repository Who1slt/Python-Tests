import pytest
from classes.calculator import Calculator, State

class TestCalculator:
    @pytest.fixture(scope='session')
    def calc(self):
        return Calculator()

    @pytest.mark.parametrize("a,b,expected", [
        (17, 8, 25.0),
        (3.9, 6.1, 10.0),
        (-0.5, 30, 29.5),
    ])
    def test_add(self, calc, a, b, expected):
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("a,b,expected", [
        (5, 7, -2.0),
        (3.5, 3.5, 0.0),
        (-7.3, -2.8, -4.5),
    ])
    def test_subtraction(self, calc, a, b, expected):
        assert calc.subtraction(a, b) == expected

    @pytest.mark.parametrize("a,b,expected", [
        (12, 2, 24.0),
        (0.5, 0.25, 0.125),
        (-0.5, -12, 6.0),
    ])
    def test_multiplication(self, calc, a, b, expected):
        assert calc.multiplication(a, b) == expected

    @pytest.mark.parametrize("a,b,expected", [
        (48, 6, 8.0),
        (-0.5, 0.25, -2.0),
        (-12, -0.5, 24.0),
        (1234, 0, State.Error),
    ])
    def test_division(self, calc, a, b, expected):
        assert calc.division(a, b) == expected