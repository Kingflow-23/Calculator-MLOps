from src.utils import add, subtract, multiply, divide, exponent

def perform_operation(choice, num1, num2):
    if choice == 1:
        return add(num1, num2)
    elif choice == 2:
        return subtract(num1, num2)
    elif choice == 3:
        return multiply(num1, num2)
    elif choice == 4:
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        return divide(num1, num2)
    elif choice == 5:
        return exponent(num1, num2)
    
    else:
        return "Invalid choice! Please choose 1, 2, 3, or 4."

def calculator(choice, num1, num2, another_calculation='no'):
    result = perform_operation(choice, num1, num2)
    
    if another_calculation == 'yes':
        return True, result  # If the user wants to continue, return a flag and result
    else:
        return False, result  # End the program and return result
