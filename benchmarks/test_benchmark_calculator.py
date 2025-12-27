import pytest
from calculator.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_benchmark_add(calc, benchmark):
    benchmark(calc.add, 123.456, 789.123)

def test_benchmark_subtract(calc, benchmark):
    benchmark(calc.subtract, 123.456, 789.123)

def test_benchmark_multiply(calc, benchmark):
    benchmark(calc.multiply, 123.456, 789.123)

def test_benchmark_divide(calc, benchmark):
    benchmark(calc.divide, 123.456, 789.123)
