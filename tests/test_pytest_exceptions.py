import pytest
import math
from classes.calculator import Calculator, State

class TestCalculatorExceptionsAndBoundary:
    
    @pytest.fixture(scope="session")
    def calc(self):
        return Calculator()

    @pytest.mark.parametrize("a,b,expected_exception", [
        (None, 5, TypeError),
        ([1, 2], 3, TypeError),
        ("abc", 5, ValueError),
        ("12.34.56", 1, ValueError),
    ])
    def test_invalid_inputs_and_exceptions(self, calc, a, b, expected_exception):
        with pytest.raises(expected_exception):
            calc.add(a, b)

    @pytest.mark.parametrize("a,b,expected,operation", [
        ("5,5", "2.5", 8.0, "add"),
        ("  5  ", "  3  ", 8.0, "add"),
        (5, 0, State.Error, "division"),
        (float('inf'), 1000, float('inf'), "add"),
        (1e308, 1e308, float('inf'), "add"),
        (1e-323, 1e-323, 2e-323, "add")
    ])
    def test_boundary_values_and_special_cases(self, calc, a, b, expected, operation):
        method = getattr(calc, operation)
        result = method(a, b)
        
        if expected == State.Error:
            assert result == expected
            assert "Нельзя делить на ноль!" in calc.error
        elif isinstance(expected, float) and math.isnan(expected):
            assert math.isnan(result)
        else:
            assert result == expected