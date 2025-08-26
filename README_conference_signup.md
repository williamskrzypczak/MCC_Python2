# Conference Sign-up System Assignment

## Assignment Overview
This assignment demonstrates the use of Python's `*args` and `**kwargs` syntax to create a flexible conference sign-up function that can handle any number of participants and their contact details.

## Assignment Requirements

### ✅ **Core Requirements Met:**
1. **Function Name**: `conference_signup` ✓
2. ***args Usage**: Accepts any number of participant names ✓
3. ****kwargs Usage**: Accepts contact details (email, phone) ✓
4. **Organized Output**: Prints summary in clear, formatted way ✓
5. **Graceful Handling**: Handles edge cases (no participants, missing details) ✓
6. **Testing**: Comprehensive test cases included ✓

## Files Included
- `conference_signup.py` - Main Python implementation
- `README_conference_signup.md` - This documentation file

## Function Signature
```python
def conference_signup(*args, **kwargs):
```

### Parameters:
- **`*args`**: Variable number of participant names (strings)
- **`**kwargs`**: Keyword arguments for contact details
  - `email`: Contact email address
  - `phone`: Contact phone number

## Key Features

### 1. **Flexible Argument Handling**
- Uses `*args` to accept any number of participant names
- Uses `**kwargs` to accept optional contact details
- Gracefully handles missing or empty arguments

### 2. **Robust Error Handling**
- Handles case where no participants are provided
- Handles missing contact details (shows "N/A")
- Provides clear feedback for edge cases

### 3. **Formatted Output**
- Clear header and separator lines
- Organized participant information
- Summary statistics at the end

### 4. **Comprehensive Testing**
- Multiple test scenarios included
- Edge case testing
- Various input combinations

## Usage Examples

### Basic Usage
```python
# Multiple participants with contact details
conference_signup("Alice", "Bob", "Charlie", 
                 email="alice@example.com", phone="123-456-7890")
```

### Single Participant
```python
# Single participant
conference_signup("David", email="david@example.com", phone="555-123-4567")
```

### Missing Contact Details
```python
# Participants with only email
conference_signup("Eve", "Frank", "Grace", email="eve@example.com")

# Participants with only phone
conference_signup("Henry", "Ivy", "Jack", phone="555-987-6543")

# Participants with no contact details
conference_signup("Kate", "Liam", "Mia", "Noah")
```

### Edge Cases
```python
# No participants
conference_signup(email="admin@conference.com", phone="555-000-0000")

# No participants and no contact details
conference_signup()
```

## Expected Output Format

The function produces output in this format:
```
Conference Participants and Their Contact Details:
--------------------------------------------------
Name: Alice
Email: alice@example.com
Phone: 123-456-7890
--------------------------------------------------
Name: Bob
Email: alice@example.com
Phone: 123-456-7890
--------------------------------------------------
Name: Charlie
Email: alice@example.com
Phone: 123-456-7890
--------------------------------------------------
Total Participants: 3
Contact Email: alice@example.com
Contact Phone: 123-456-7890
```

## Running the Code

### Prerequisites
- Python 3.x installed on your system

### Execution
```bash
python3 conference_signup.py
```

### Output
The program will demonstrate:
1. Expected output format (as specified in assignment)
2. Additional demonstrations with different scenarios
3. Comprehensive test cases showing all functionality

## Learning Objectives Demonstrated

### 1. ***args and **kwargs Mastery**
- Understanding variable argument syntax
- Proper usage of keyword arguments
- Flexible function design

### 2. **Error Handling**
- Graceful handling of edge cases
- Providing meaningful feedback
- Robust function design

### 3. **String Formatting**
- f-string usage for dynamic output
- Organized and readable formatting
- Professional presentation

### 4. **Function Design**
- Clear documentation with docstrings
- Logical function structure
- Comprehensive testing

## Test Cases Included

The implementation includes 7 comprehensive test cases:

1. **Multiple participants with full contact details**
2. **Single participant with contact details**
3. **Multiple participants with only email**
4. **Multiple participants with only phone**
5. **Multiple participants with no contact details**
6. **No participants (edge case)**
7. **No participants and no contact details (edge case)**

## Code Quality Features

### ✅ **Documentation**
- Comprehensive docstrings
- Clear comments explaining logic
- Example usage in docstrings

### ✅ **Error Handling**
- Graceful handling of edge cases
- Meaningful error messages
- Robust input validation

### ✅ **Code Organization**
- Logical function structure
- Clear separation of concerns
- Readable and maintainable code

### ✅ **Testing**
- Comprehensive test suite
- Edge case coverage
- Multiple usage scenarios

## Assignment Submission

### Files to Submit:
1. `conference_signup.py` - Main Python script
2. `README_conference_signup.md` - Documentation (optional but recommended)

### GitHub Repository:
Upload the Python script to your course directory on GitHub and submit the link to your repository.

## Extension Ideas

The function can be easily extended to include:
- Additional contact details (address, company, etc.)
- Registration timestamps
- Payment information
- Dietary preferences
- Session preferences
- Export functionality (CSV, JSON)

## Technical Notes

- **Python Version**: Compatible with Python 3.x
- **Dependencies**: No external libraries required
- **Performance**: O(n) time complexity where n is number of participants
- **Memory**: Minimal memory usage, suitable for large participant lists
