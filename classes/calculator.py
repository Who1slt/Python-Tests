from enum import Enum

class State(Enum):
	Running = 1
	Idle = 2
	Error = 4

class Calculator:
	def __init__(self):
		self.state = State.Idle
		self.operations = {
            '+': self.add,
            '-': self.subtraction,
            '*': self.multiplication,
            '/': self.division
        }
	
	def _validate_input(self, value):
		if isinstance(value, str):
			try:
				return float(value.replace(',', '.'))
			except ValueError:
				raise ValueError(f"Невозможно преобразовать в число: '{value}'")
	
		if not isinstance(value, (int, float)) or value is None:
			raise TypeError(f"Неподдерживаемый тип: {type(value).__name__}")
		
		return value

	def add(self, a, b):
		a = self._validate_input(a)
		b = self._validate_input(b)
		return a + b
	
	def subtraction(self, a, b):
		a = self._validate_input(a)
		b = self._validate_input(b)
		return a - b
	
	def multiplication(self, a, b):
		a = self._validate_input(a)
		b = self._validate_input(b)
		return a * b
	
	def division(self, a, b):
		a = self._validate_input(a)
		b = self._validate_input(b)

		if (b != 0):
			return a / b
		else:
			self.error = "Нельзя делить на ноль!"
			return State.Error
	
	def run(self):
		self.state = State.Running
		
		while (self.state == State.Running):
			operation = input("Введите операцию (+, -, *, /) или q для выхода: ")
			result = "Неккоректная операция!"

			if operation in self.operations:
				a = input("Введите первое число: ")
				b = input("Введите второе число: ")

				try:
					result = self.operations[operation](a, b)
					if (result != State.Error):
						result = f"Ответ: {self.operations[operation](a, b)}"
					else:
						result = self.error
				except (ValueError, TypeError) as e:
					result = str(e)
			elif operation.lower() == 'q':
				result = "Калькулятор окончил свою работу!"
				self.state = State.Idle
			
			print(f"{result}\n")