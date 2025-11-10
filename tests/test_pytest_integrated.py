import pytest
from classes.calculator import Calculator, State
from classes.log import Log

class TestCalculatorWithHistory:

    @pytest.fixture
    def setup(self):
        return Calculator(), Log()
    
    def test_calculator_operations_saved_to_history(self, setup):
        calc, history = setup
        
        result1 = calc.add(5, 3)
        result2 = calc.division(10, 2)
        
        history.add_operation('+', 5, 3, result1)
        history.add_operation('/', 10, 2, result2)
        
        assert len(history.get_all_operations()) == 2
    
    def test_operations_order(self, setup):
        calc, history = setup
        
        operations = [
            (calc.add, '+', 2, 3),
            (calc.multiplication, '*', 4, 5), 
            (calc.division, '/', 20, 4)
        ]
        
        for calc_method, op_symbol, a, b in operations:
            result = calc_method(a, b)
            history.add_operation(op_symbol, a, b, result)
        
        assert history.get_last_operation()['operation'] == '/'
        assert history.get_last_operation()['a'] == 20
        assert history.get_last_operation()['b'] == 4
        assert history.get_last_operation()['result'] == 5.0

    def test_error_operations_not_saved(self, setup):
        calc, history = setup
        result = calc.division(10, 0)
        
        if result != State.Error:
            history.add_operation('/', 10, 0, result)
        
        assert len(history.get_all_operations()) == 0