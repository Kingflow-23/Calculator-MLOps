from src.calculator import perform_operation


# Test for addition
def test_addition():
    result = perform_operation(1, 2, 3)  # Test the addition operation
    assert result == 5.0


# Test for subtraction
def test_subtraction():
    result = perform_operation(2, 10, 5)  # Test the subtraction operation
    assert result == 5.0


# Test for multiplication
def test_multiplication():
    result = perform_operation(3, 4, 5)  # Test the multiplication operation
    assert result == 20.0


# Test for division
def test_division():
    result = perform_operation(4, 10, 2)  # Test the division operation
    assert result == 5.0

# Test for division by zero
def test_division_by_zero():
    result = perform_operation(4, 10, 0)  # Division by zero
    assert result == "Error! Division by zero is not allowed."

def test_exponent():
    result = perform_operation(5, 2, 3)  # Test the exponent operation
    assert result == 8.0

# Test for invalid operation
def test_invalid_choice():
    result = perform_operation(50, 10, 2)  # Invalid operation choice
    assert result == "Invalid choice! Please choose 1, 2, 3, or 4."
