"""
Unit tests for the calculator library
"""

import os
import sys

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from src.utils import add, subtract, multiply, divide, exponent

class TestCalculator:
    """ Test class for calculator library """
    
    def test_addition(self):
        assert 4 == add(2, 2)
        assert 10 == add(5, 5)
        assert 0 == add(0, 0)
        assert -4 == add(-6, 2)
    
    def test_subtraction(self):
        assert 2 == subtract(4, 2)
        assert 0 == subtract(0, 0)
        assert -2 == subtract(2, 4)
        assert 8 == subtract(10, 2)
        
    def test_multiplication(self):
        assert 100 == multiply(10, 10)
        assert 0 == multiply(0, 100)
        assert 0 == multiply(100, 0)
        assert -5 == multiply(5, -1)
        assert 4 == multiply(2, 2)
        
    def test_division(self):
        assert 2 == divide(10, 5)
        assert 0.5 == divide(1, 2)
        assert 0 == divide(0, 1)
        assert 0 == divide(0, 100)
        
    def test_exponent(self):
        assert 4 == exponent(2, 2)
        assert 8 == exponent(2, 3)
        assert 1 == exponent(1, 100)
        assert 0 == exponent(0, 100)
        
    def test_division_by_zero(self):
        try:
            divide(4, 0)
        except ValueError:
            pass
        else:
            assert False, "Expected ValueError"