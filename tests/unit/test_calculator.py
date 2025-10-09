"""
Unit Tests for Calculator Module
"""
import pytest
from src.calculator import add, subtract, multiply, divide, power, square_root


class TestBasicOperations:
    """Test basic addition and subtraction"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2, -3) == -5
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2


class TestMultiplyDivideWithValidation:
    """Test input validation for multiply and divide"""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError):
            multiply("5", 3)
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError):
            divide("10", 2)


class TestMultiplyDivide:
    """Test multiplication and division operations"""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(3, 4) == 12
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(5, 0) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-2, 3) == -6
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        assert divide(-10, 2) == -5


class TestAdvancedOperations:
    """Test power and square root operations"""
    
    def test_power_positive_numbers(self):
        """Test power with positive numbers"""
        assert power(2, 3) == 8
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent"""
        assert power(5, 0) == 1
    
    def test_square_root_positive_numbers(self):
        """Test square root of positive numbers"""
        assert square_root(4) == 2
    
    def test_square_root_negative_raises_error(self):
        """Test that square root of negative raises ValueError"""
        with pytest.raises(
            ValueError, match="Cannot calculate square root of negative"
        ):
            square_root(-4)
