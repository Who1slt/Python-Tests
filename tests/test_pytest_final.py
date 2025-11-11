import pytest
from unittest.mock import patch, call
from classes.calculator import Calculator, State
from classes.log import Log

class TestCalculatorFinal:
	@pytest.fixture
	def calc(self):
		return Calculator()
	
	@pytest.fixture
	def log(self):
		return Log()

	@pytest.mark.parametrize("a,b,expected_exception", [
        (None, 5, TypeError),
        ([1, 2], 3, TypeError)
    ])
	def test_type_exceptions(self, calc, a, b, expected_exception):
		with pytest.raises(expected_exception):
			calc.add(a, b)
	
	def test_integration(self, calc, log):
		operations = [
            (calc.add, '+', 2, 3),
            (calc.multiplication, '*', 4, 5), 
            (calc.division, '/', 20, 4)
        ]
		log.max_size = 2

		for calc_method, op_symbol, a, b in operations:
			result = calc_method(a, b)
			log.add_operation(op_symbol, a, b, result)
		assert len(log.get_all_operations()) == 2

		assert log.get_last_operation()['operation'] == '/'
		assert log.get_last_operation()['a'] == 20
		assert log.get_last_operation()['b'] == 4
		assert log.get_last_operation()['result'] == 5.0
        
		if calc.division(10, 0) != State.Error:
			log.add_operation('/', 10, 0, result)
		assert len(log.get_all_operations()) == 2

		log.clear_history()
		assert len(log.get_all_operations()) == 0

		
	
	@patch('builtins.input')
	@patch('builtins.print')
	def test_base_workflow(self, mock_print, mock_input, calc):
		mock_input.side_effect = [
			'+', "-127", "11,4",
			'-', "15", "-3.5", 
			'*', "-0.25", "8",
			'/', " 24", "-3.2",

			'-', '1e308', '1e288',
			'+', '1e-323', '1e-171',
			'/', 'inf', '-125,3',
			'*', 'nan', '5',

			'-', '12,3abc', '8',
			'*', '1.2.3', '5',
			'/', '1234', ' 0 ',

			'invalid_operation', 
			'q'
		]
		calc.run()

		expected_outputs = [
			call("Ответ: -115.6\n"),
			call("Ответ: 18.5\n"),
			call("Ответ: -2.0\n"),
			call("Ответ: -7.5\n"),

			call("Ответ: 1e+308\n"),
			call("Ответ: 1e-171\n"),
			call("Ответ: -inf\n"),
			call("Ответ: nan\n"),

			call("Невозможно преобразовать в число: '12,3abc'\n"),
			call("Невозможно преобразовать в число: '1.2.3'\n"),
			call("Нельзя делить на ноль!\n"),

			call("Неккоректная операция!\n"),
			call("Калькулятор окончил свою работу!\n")
		]

		assert len(mock_print.call_args_list) == len(expected_outputs)
		for i, expected_call in enumerate(expected_outputs):
			assert mock_print.call_args_list[i] == expected_call