from unittest.mock import patch, call
from classes.calculator import Calculator

class TestCalculatorWithMocks:
	@patch('builtins.input')
	@patch('builtins.print')
	def test_base_operations(self, mock_print, mock_input):
		calc = Calculator()
		mock_input.side_effect = [
			'+', '17', '8',
			'+', '3.9', '6.1',
			'-', '5', '7',
			'-', '-7.3', '-2.8',
			'*', '0.5', '0.25',
			'*', '-0.5', '-12',
			'/', '48', '6',
			'/', '-12', '-0.5',
			'/', '1234', '0',
			'q'
		]
		calc.run()

		expected_outputs = [
			call("Ответ: 25.0\n"),
			call("Ответ: 10.0\n"),
			call("Ответ: -2.0\n"),
			call("Ответ: -4.5\n"),
			call("Ответ: 0.125\n"),
			call("Ответ: 6.0\n"),
			call("Ответ: 8.0\n"),
			call("Ответ: 24.0\n"),
			call("Нельзя делить на ноль!\n"),
			call("Калькулятор окончил свою работу!\n")
		]

		assert len(mock_print.call_args_list) == len(expected_outputs)
		for i, expected_call in enumerate(expected_outputs):
			assert mock_print.call_args_list[i] == expected_call
	
	@patch('builtins.input')
	@patch('builtins.print')
	def test_base_exceptions(self, mock_print, mock_input):
		calc = Calculator()
		mock_input.side_effect = [
			'+', 'invalid_number', '5',
			'-', '12,3abc', '5',
			'*', '1.2.3', '5',
			'invalid_operation',
			'q'
		]
		calc.run()

		expected_outputs = [
			call("Невозможно преобразовать в число: 'invalid_number'\n"),
			call("Невозможно преобразовать в число: '12,3abc'\n"),
			call("Невозможно преобразовать в число: '1.2.3'\n"),
			call("Неккоректная операция!\n"),
			call("Калькулятор окончил свою работу!\n")
		]

		assert len(mock_print.call_args_list) == len(expected_outputs)
		for i, expected_call in enumerate(expected_outputs):
			assert mock_print.call_args_list[i] == expected_call