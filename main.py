import coverage
import pytest

detective = coverage.Coverage(
    source=['classes'],
    omit=[
		'*/__pycache__/*',
		'*/__init__.py'
	]
)
detective.start()

test_files = [
	'tests/test_pytest_final.py'
]

for test_file in test_files:
	pytest.main([test_file, '-v'])
detective.stop()
detective.save()

detective.report()