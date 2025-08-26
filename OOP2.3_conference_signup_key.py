"""
Conference Sign-up System
Assignment: Create a Python function that simulates a conference sign-up process

This module implements a conference sign-up function that accepts participant names
and their contact details, then prints a summary in an organized format.

Author: Student
Date: 2024
"""

def conference_signup(*args, **kwargs):
    """
    Simulates a conference sign-up process by accepting participant names and contact details.
    
    This function demonstrates the use of *args for variable number of arguments
    and **kwargs for keyword arguments. It handles cases where no participants
    or no contact details are provided gracefully.
    
    Args:
        *args: Variable number of participant names (strings)
        **kwargs: Keyword arguments containing contact details
                 Expected keys: 'email', 'phone'
    
    Returns:
        None: Function prints the summary directly
    
    Example:
        conference_signup("Alice", "Bob", "Charlie", 
                         email="alice@example.com", phone="123-456-7890")
    """
    
    # Print header
    print("Conference Participants and Their Contact Details:")
    print("-" * 50)
    
    # Handle case where no participants are provided
    if not args:
        print("No participants registered for the conference.")
        return
    
    # Get contact details from kwargs
    email = kwargs.get('email', 'N/A')
    phone = kwargs.get('phone', 'N/A')
    
    # Process each participant
    for i, participant in enumerate(args, 1):
        print(f"Name: {participant}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        
        # Add separator line between participants (except for the last one)
        if i < len(args):
            print("-" * 50)
    
    # Print summary statistics
    print("-" * 50)
    print(f"Total Participants: {len(args)}")
    print(f"Contact Email: {email}")
    print(f"Contact Phone: {phone}")


def test_conference_signup():
    """
    Test function to demonstrate the conference_signup function with various scenarios.
    
    This function tests different cases including:
    - Multiple participants with contact details
    - Single participant
    - No participants
    - Missing contact details
    """
    
    print("TESTING CONFERENCE SIGN-UP FUNCTION")
    print("=" * 60)
    
    # Test Case 1: Multiple participants with full contact details
    print("\nTest Case 1: Multiple participants with full contact details")
    print("-" * 60)
    conference_signup("Alice", "Bob", "Charlie", 
                     email="alice@example.com", phone="123-456-7890")
    
    # Test Case 2: Single participant with contact details
    print("\nTest Case 2: Single participant with contact details")
    print("-" * 60)
    conference_signup("David", email="david@example.com", phone="555-123-4567")
    
    # Test Case 3: Multiple participants with only email
    print("\nTest Case 3: Multiple participants with only email")
    print("-" * 60)
    conference_signup("Eve", "Frank", "Grace", email="eve@example.com")
    
    # Test Case 4: Multiple participants with only phone
    print("\nTest Case 4: Multiple participants with only phone")
    print("-" * 60)
    conference_signup("Henry", "Ivy", "Jack", phone="555-987-6543")
    
    # Test Case 5: Multiple participants with no contact details
    print("\nTest Case 5: Multiple participants with no contact details")
    print("-" * 60)
    conference_signup("Kate", "Liam", "Mia", "Noah")
    
    # Test Case 6: No participants (edge case)
    print("\nTest Case 6: No participants (edge case)")
    print("-" * 60)
    conference_signup(email="admin@conference.com", phone="555-000-0000")
    
    # Test Case 7: No participants and no contact details (edge case)
    print("\nTest Case 7: No participants and no contact details (edge case)")
    print("-" * 60)
    conference_signup()


def main():
    """
    Main function to run the conference sign-up demonstration.
    
    This function demonstrates the basic usage of the conference_signup function
    with the expected output format as specified in the assignment.
    """
    
    print("CONFERENCE SIGN-UP SYSTEM DEMONSTRATION")
    print("=" * 60)
    
    # Demonstrate the expected output format from the assignment
    print("\nExpected Output Format:")
    conference_signup("Alice", "Bob", "Charlie", 
                     email="alice@example.com", phone="123-456-7890")
    
    # Additional demonstration with different contact details
    print("\nAdditional Demonstration:")
    conference_signup("David", "Eve", "Frank", 
                     email="david@example.com", phone="987-654-3210")
    
    # Demonstrate handling of missing contact details
    print("\nHandling Missing Contact Details:")
    conference_signup("Grace", "Henry", "Ivy", 
                     email="grace@example.com")  # No phone provided


if __name__ == "__main__":
    # Run the main demonstration
    main()
    
    # Run all test cases
    test_conference_signup()
