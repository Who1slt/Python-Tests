from classes.calculator import Calculator, State

def test_add():
    calc = Calculator()
    integer_test = calc.add(17, 8) == 25.0
    float_test = calc.add(3.9,6.1) == 10.0
    negative_test = calc.add(-0.5,30) == 29.5
    assert integer_test and float_test and negative_test

def test_subtraction():
    calc = Calculator()
    integer_test = calc.subtraction(5, 7) == -2.0
    float_test = calc.subtraction(3.5,3.5) == 0.0
    negative_test = calc.subtraction(-7.3,-2.8) == -4.5
    assert integer_test and float_test and negative_test

def test_multiplication():
    calc = Calculator()
    integer_test = calc.multiplication(12, 2) == 24.0
    float_test = calc.multiplication(0.5,0.25) == 0.125
    negative_test = calc.multiplication(-0.5,-12) == 6.0
    assert integer_test and float_test and negative_test

def test_division():
    calc = Calculator()
    integer_test = calc.division(48, 6) == 8.0
    float_test = calc.division(-0.5,0.25) == -2.0
    negative_test = calc.division(-12,-0.5) == 24.0
    zero_test = calc.division(1234,0) == State.Error
    assert integer_test and float_test and negative_test and zero_test