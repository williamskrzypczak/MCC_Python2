# Python Best Practices Exercise

## Assignment Overview
This assignment demonstrates how to improve Python code by applying best practices and guidelines. The original code had several issues that needed to be addressed to make it more readable, maintainable, and robust.

## Original Code Problems

### ❌ **Issues in the Original Code:**
```python
def fx(a, b):
  if a > 0 and b > 0:
    if a > b:
      for i in range(b):
        print(a)
    else:
      for j in range(a):
        print(b)
  elif a == 0 or b == 0:
      return "Zero found"
  else:
      if a < b:
          return a - b
      else:
          return b - a
```

**Problems Identified:**
1. **Single-letter variable names** (`a`, `b`, `i`, `j`) - unclear and unreadable
2. **Unclear function name** (`fx`) - doesn't describe purpose
3. **No comments or documentation** - code purpose is unclear
4. **Inconsistent indentation** - mixing tabs and spaces
5. **Deep nesting levels** - hard to read and maintain
6. **No error handling** - crashes with invalid inputs
7. **No docstrings** - missing function documentation

## Improved Code Solution

### ✅ **Improvements Made:**

#### **1. Meaningful Names**
- **Function**: `fx` → `compare_and_print_numbers`
- **Variables**: `a, b` → `first_number, second_number`
- **Loop variables**: `i, j` → `_` (unused variable convention)

#### **2. Comprehensive Documentation**
- **Module docstring**: Explains the purpose of the entire module
- **Function docstrings**: Detailed documentation with parameters, returns, and examples
- **Inline comments**: Explain the purpose of each code block

#### **3. Consistent Formatting**
- **Indentation**: Consistent 4-space indentation throughout
- **Spacing**: Proper blank lines to separate logical sections
- **Line length**: Reasonable line lengths for readability

#### **4. Simplified Logic**
- **Helper functions**: Broke complex logic into smaller, focused functions
- **Reduced nesting**: Flattened conditional structures
- **Early returns**: Handle edge cases first to reduce complexity

#### **5. Error Handling**
- **Type validation**: Check input types before processing
- **Meaningful errors**: Clear error messages for debugging
- **Graceful degradation**: Handle unexpected inputs properly

#### **6. Separation of Concerns**
- **Main function**: High-level logic and coordination
- **Helper functions**: Specific tasks (`_print_larger_number_times`, `_calculate_difference`)
- **Test function**: Comprehensive testing scenarios

## Files Included
- `python_best_practices.py` - Improved Python implementation
- `README_best_practices.md` - This documentation file

## Key Improvements Demonstrated

### **1. Function Structure**
```python
def compare_and_print_numbers(first_number, second_number):
    """
    Compare two numbers and perform different operations based on their values.
    
    Args:
        first_number (int or float): The first number to compare
        second_number (int or float): The second number to compare
    
    Returns:
        str or int or float: Result based on input values
    
    Raises:
        TypeError: If inputs are not numeric types
    """
```

### **2. Error Handling**
```python
# Validate input types
if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
    raise TypeError("Both arguments must be numeric types (int or float)")
```

### **3. Helper Functions**
```python
def _print_larger_number_times(first_number, second_number):
    """Print the larger number multiple times based on the smaller number."""
    
def _calculate_difference(first_number, second_number):
    """Calculate the difference between two numbers."""
```

### **4. Simplified Logic**
```python
# Check for zero values first (simplified logic)
if first_number == 0 or second_number == 0:
    return "Zero found"

# Handle positive numbers
if first_number > 0 and second_number > 0:
    _print_larger_number_times(first_number, second_number)
    return None

# Handle negative numbers (simplified logic)
return _calculate_difference(first_number, second_number)
```

## Running the Code

### Prerequisites
- Python 3.x installed on your system

### Execution
```bash
python3 python_best_practices.py
```

### Output
The program demonstrates:
1. **Original code problems** - Lists all issues found
2. **Improvements made** - Shows what was fixed
3. **Basic functionality** - Demonstrates the improved function
4. **Comprehensive testing** - Tests various scenarios and error handling

## Test Cases Included

The improved code includes comprehensive testing for:

1. **Positive numbers** - Both numbers > 0
2. **Zero values** - Either number = 0
3. **Negative numbers** - Both numbers < 0
4. **Mixed numbers** - One positive, one negative
5. **Error handling** - Invalid input types

## Learning Objectives Met

### ✅ **Code Quality**
- **Readability**: Clear, descriptive names and structure
- **Maintainability**: Modular design with helper functions
- **Robustness**: Proper error handling and validation

### ✅ **Python Best Practices**
- **PEP 8 Compliance**: Proper formatting and style
- **Documentation**: Comprehensive docstrings and comments
- **Error Handling**: Graceful handling of edge cases

### ✅ **Software Engineering Principles**
- **Single Responsibility**: Each function has one clear purpose
- **DRY (Don't Repeat Yourself)**: Eliminated code duplication
- **Separation of Concerns**: Logical organization of functionality

## Assignment Submission

### Files to Submit:
1. `python_best_practices.py` - Improved Python script
2. `README_best_practices.md` - Documentation (optional but recommended)

### GitHub Repository:
Upload the Python script to your course directory on GitHub and submit the link to your repository.

## Code Comparison

### **Before (Original):**
```python
def fx(a, b):
  if a > 0 and b > 0:
    if a > b:
      for i in range(b):
        print(a)
    else:
      for j in range(a):
        print(b)
  elif a == 0 or b == 0:
      return "Zero found"
  else:
      if a < b:
          return a - b
      else:
          return b - a
```

### **After (Improved):**
```python
def compare_and_print_numbers(first_number, second_number):
    """
    Compare two numbers and perform different operations based on their values.
    """
    # Validate input types
    if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
        raise TypeError("Both arguments must be numeric types (int or float)")
    
    # Check for zero values first
    if first_number == 0 or second_number == 0:
        return "Zero found"
    
    # Handle positive numbers
    if first_number > 0 and second_number > 0:
        _print_larger_number_times(first_number, second_number)
        return None
    
    # Handle negative numbers
    return _calculate_difference(first_number, second_number)
```

## Extension Ideas

The improved code can be further enhanced with:
- **Logging**: Add proper logging for debugging
- **Unit tests**: Comprehensive test suite with pytest
- **Type hints**: Add type annotations for better IDE support
- **Configuration**: Make behavior configurable
- **Performance optimization**: Optimize for large inputs

## Technical Notes

- **Python Version**: Compatible with Python 3.x
- **Dependencies**: No external libraries required
- **Performance**: O(n) time complexity where n is the smaller number
- **Memory**: Minimal memory usage
- **Error Handling**: Comprehensive input validation
