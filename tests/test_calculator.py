import pytest
from src.calculator import add, divide, multiply, subtract

# Replaces writing 4 identical test functions
@pytest.mark.parametrize("a, b, expected", [
    (2,   3,   5),    # positive
    (0,   0,   0),    # zeros
    (-1,  1,   0),    # negative
    (100, -50, 50),   # large values
])
def test_add_cases(a, b, expected):
    assert add(a, b) == expected

def test_division(division_cases):
    for a, b, exp in division_cases:
        assert divide(a, b) == exp

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
        