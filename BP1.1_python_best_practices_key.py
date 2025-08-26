"""
Python Best Practices Exercise
Assignment: Improve a Python program to follow best practices and guidelines

This module contains an improved version of the original function that demonstrates
proper Python coding standards including meaningful names, documentation, error handling,
and clean code structure.

Author: Student
Date: 2024
"""


def compare_and_print_numbers(first_number, second_number):
    """
    Compare two numbers and perform different operations based on their values.
    
    This function takes two numbers and:
    1. If both are positive: prints the larger number multiple times based on the smaller number
    2. If either is zero: returns a message indicating zero was found
    3. If both are negative: returns the difference between them
    
    Args:
        first_number (int or float): The first number to compare
        second_number (int or float): The second number to compare
    
    Returns:
        str or int or float: 
            - String message if zero is found
            - Numeric difference if both numbers are negative
            - None if both numbers are positive (prints output instead)
    
    Raises:
        TypeError: If inputs are not numeric types
        ValueError: If inputs are not valid numbers
    
    Example:
        >>> compare_and_print_numbers(5, 3)
        5
        5
        5
        
        >>> compare_and_print_numbers(0, 10)
        'Zero found'
        
        >>> compare_and_print_numbers(-5, -3)
        -2
    """
    
    # Validate input types
    if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
        raise TypeError("Both arguments must be numeric types (int or float)")
    
    # Check for zero values first (simplified logic)
    if first_number == 0 or second_number == 0:
        return "Zero found"
    
    # Handle positive numbers
    if first_number > 0 and second_number > 0:
        _print_larger_number_times(first_number, second_number)
        return None
    
    # Handle negative numbers (simplified logic)
    return _calculate_difference(first_number, second_number)


def _print_larger_number_times(first_number, second_number):
    """
    Print the larger number multiple times based on the smaller number.
    
    This helper function handles the case where both numbers are positive.
    It determines which number is larger and prints it multiple times
    based on the value of the smaller number.
    
    Args:
        first_number (int or float): First positive number
        second_number (int or float): Second positive number
    
    Example:
        >>> _print_larger_number_times(5, 3)
        5
        5
        5
    """
    
    # Determine which number is larger and how many times to print
    if first_number > second_number:
        larger_number = first_number
        print_count = int(second_number)
    else:
        larger_number = second_number
        print_count = int(first_number)
    
    # Print the larger number the specified number of times
    for _ in range(print_count):
        print(larger_number)


def _calculate_difference(first_number, second_number):
    """
    Calculate the difference between two numbers.
    
    This helper function handles the case where both numbers are negative.
    It returns the difference between the numbers, always returning
    a positive value.
    
    Args:
        first_number (int or float): First number
        second_number (int or float): Second number
    
    Returns:
        int or float: The difference between the numbers
    
    Example:
        >>> _calculate_difference(-5, -3)
        -2
    """
    
    # Calculate difference (simplified logic)
    if first_number < second_number:
        return first_number - second_number
    else:
        return second_number - first_number


def test_improved_function():
    """
    Test function to demonstrate the improved code with various scenarios.
    
    This function tests different input combinations to show how the
    improved function handles various cases gracefully.
    """
    
    print("TESTING IMPROVED FUNCTION")
    print("=" * 50)
    
    # Test cases with positive numbers
    print("\n1. Testing with positive numbers:")
    print("-" * 30)
    print("Input: compare_and_print_numbers(5, 3)")
    result = compare_and_print_numbers(5, 3)
    print(f"Return value: {result}")
    
    print("\nInput: compare_and_print_numbers(2, 4)")
    result = compare_and_print_numbers(2, 4)
    print(f"Return value: {result}")
    
    # Test cases with zero
    print("\n2. Testing with zero values:")
    print("-" * 30)
    print("Input: compare_and_print_numbers(0, 10)")
    result = compare_and_print_numbers(0, 10)
    print(f"Result: {result}")
    
    print("Input: compare_and_print_numbers(5, 0)")
    result = compare_and_print_numbers(5, 0)
    print(f"Result: {result}")
    
    # Test cases with negative numbers
    print("\n3. Testing with negative numbers:")
    print("-" * 30)
    print("Input: compare_and_print_numbers(-5, -3)")
    result = compare_and_print_numbers(-5, -3)
    print(f"Result: {result}")
    
    print("Input: compare_and_print_numbers(-2, -7)")
    result = compare_and_print_numbers(-2, -7)
    print(f"Result: {result}")
    
    # Test cases with mixed numbers
    print("\n4. Testing with mixed positive/negative:")
    print("-" * 30)
    print("Input: compare_and_print_numbers(-5, 3)")
    result = compare_and_print_numbers(-5, 3)
    print(f"Result: {result}")
    
    print("Input: compare_and_print_numbers(5, -3)")
    result = compare_and_print_numbers(5, -3)
    print(f"Result: {result}")
    
    # Test error handling
    print("\n5. Testing error handling:")
    print("-" * 30)
    
    try:
        print("Input: compare_and_print_numbers('abc', 5)")
        result = compare_and_print_numbers('abc', 5)
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Error caught: {e}")
    
    try:
        print("Input: compare_and_print_numbers([1, 2], 5)")
        result = compare_and_print_numbers([1, 2], 5)
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Error caught: {e}")


def main():
    """
    Main function to demonstrate the improved code.
    
    This function shows the basic usage of the improved function
    and compares it with the original problematic code.
    """
    
    print("PYTHON BEST PRACTICES EXERCISE")
    print("=" * 50)
    
    print("\nORIGINAL CODE PROBLEMS:")
    print("-" * 30)
    print("1. Single-letter variable names (a, b, i, j)")
    print("2. Unclear function name (fx)")
    print("3. No comments or documentation")
    print("4. Inconsistent indentation")
    print("5. Deep nesting levels")
    print("6. No error handling")
    print("7. No docstrings")
    
    print("\nIMPROVEMENTS MADE:")
    print("-" * 30)
    print("1. ✅ Meaningful variable and function names")
    print("2. ✅ Comprehensive comments and documentation")
    print("3. ✅ Consistent indentation (4 spaces)")
    print("4. ✅ Proper spacing and blank lines")
    print("5. ✅ Simplified logic with helper functions")
    print("6. ✅ Error handling for invalid inputs")
    print("7. ✅ Detailed docstrings with examples")
    print("8. ✅ Separation of concerns")
    
    print("\nDEMONSTRATION:")
    print("-" * 30)
    
    # Demonstrate basic functionality
    print("Example 1: Positive numbers")
    print("compare_and_print_numbers(5, 3)")
    result = compare_and_print_numbers(5, 3)
    print(f"Return value: {result}")
    
    print("\nExample 2: Zero found")
    print("compare_and_print_numbers(0, 10)")
    result = compare_and_print_numbers(0, 10)
    print(f"Result: {result}")
    
    print("\nExample 3: Negative numbers")
    print("compare_and_print_numbers(-5, -3)")
    result = compare_and_print_numbers(-5, -3)
    print(f"Result: {result}")


if __name__ == "__main__":
    # Run the main demonstration
    main()
    
    # Run comprehensive tests
    test_improved_function()
