import pytest
from classes.calculator import Calculator, State
from classes.log import Log

class TestCalculatorWithLog:

    @pytest.fixture
    def setup(self):
        return Calculator(), Log()
    
    def test_calculator_operations_saved_to_log(self, setup):
        calc, log = setup
        
        result1 = calc.add(5, 3)
        result2 = calc.division(10, 2)
        
        log.add_operation('+', 5, 3, result1)
        log.add_operation('/', 10, 2, result2)
        
        assert len(log.get_all_operations()) == 2
    
    def test_operations_order(self, setup):
        calc, log = setup
        
        operations = [
            (calc.add, '+', 2, 3),
            (calc.multiplication, '*', 4, 5), 
            (calc.division, '/', 20, 4)
        ]
        
        for calc_method, op_symbol, a, b in operations:
            result = calc_method(a, b)
            log.add_operation(op_symbol, a, b, result)
        
        assert log.get_last_operation()['operation'] == '/'
        assert log.get_last_operation()['a'] == 20
        assert log.get_last_operation()['b'] == 4
        assert log.get_last_operation()['result'] == 5.0

    def test_error_operations_not_saved(self, setup):
        calc, log = setup
        result = calc.division(10, 0)
        
        if result != State.Error:
            log.add_operation('/', 10, 0, result)
        
        assert len(log.get_all_operations()) == 0