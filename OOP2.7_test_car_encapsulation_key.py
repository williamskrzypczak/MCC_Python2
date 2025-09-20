"""
Car Encapsulation Testing Suite
Assignment: Testing Encapsulation in Python Classes

This module contains comprehensive tests to verify that encapsulation
is properly implemented in the Car class.

Author: Student
Date: 2024
"""

import sys
from OOP2_4_car_key import Car


def test_direct_attribute_access():
    """
    Test that direct access to private attributes is not recommended.
    
    This test verifies that while Python doesn't prevent direct access
    to private attributes (those prefixed with _), the proper way to
    access them is through getter and setter methods.
    """
    print("Testing Direct Attribute Access...")
    print("-" * 40)
    
    # Create a car instance
    my_car = Car("Toyota", "Camry", 2022, "Blue")
    
    # Test that private attributes exist but should not be accessed directly
    try:
        # In Python, private attributes can still be accessed, but it's not recommended
        direct_make = my_car._make  # This works but violates encapsulation
        print(f"WARNING: Direct access to _make succeeded: {direct_make}")
        print("This violates encapsulation principles!")
        
        # Attempt to modify directly (also works but violates encapsulation)
        my_car._make = "Honda"  # This works but violates encapsulation
        print(f"WARNING: Direct modification of _make succeeded: {my_car._make}")
        print("This violates encapsulation principles!")
        
        # Reset for proper testing
        my_car._make = "Toyota"
        
        print("✗ Direct access is possible but should be avoided")
        print("✓ Encapsulation relies on convention (underscore prefix)")
        
    except AttributeError as e:
        print(f"✓ Direct access properly blocked: {e}")
    
    print()


def test_getters_and_setters():
    """
    Test that getter and setter methods work correctly.
    
    This test verifies that the public interface (getters and setters)
    provides proper access to the private attributes with validation.
    """
    print("Testing Getters and Setters...")
    print("-" * 40)
    
    # Create a car instance
    my_car = Car("Ford", "Mustang", 2023, "Red")
    
    # Test getters
    try:
        assert my_car.get_make() == "Ford", f"Expected 'Ford', got '{my_car.get_make()}'"
        assert my_car.get_model() == "Mustang", f"Expected 'Mustang', got '{my_car.get_model()}'"
        assert my_car.get_year() == 2023, f"Expected 2023, got {my_car.get_year()}"
        assert my_car.get_color() == "Red", f"Expected 'Red', got '{my_car.get_color()}'"
        assert my_car.get_gas_level() == 0.0, f"Expected 0.0, got {my_car.get_gas_level()}"
        assert my_car.get_max_gas_capacity() == 15.0, f"Expected 15.0, got {my_car.get_max_gas_capacity()}"
        
        print("✓ All getters work correctly")
        
    except AssertionError as e:
        print(f"✗ Getter test failed: {e}")
        return False
    
    # Test setters with valid data
    try:
        my_car.set_make("Chevrolet")
        assert my_car.get_make() == "Chevrolet", f"Expected 'Chevrolet', got '{my_car.get_make()}'"
        
        my_car.set_model("Corvette")
        assert my_car.get_model() == "Corvette", f"Expected 'Corvette', got '{my_car.get_model()}'"
        
        my_car.set_year(2024)
        assert my_car.get_year() == 2024, f"Expected 2024, got {my_car.get_year()}"
        
        my_car.set_color("Black")
        assert my_car.get_color() == "Black", f"Expected 'Black', got '{my_car.get_color()}'"
        
        print("✓ All setters work correctly with valid data")
        
    except (AssertionError, ValueError) as e:
        print(f"✗ Setter test failed: {e}")
        return False
    
    # Test setters with invalid data
    print("\nTesting setter validation...")
    
    # Test invalid make
    try:
        my_car.set_make("")  # Empty string should fail
        print("✗ Empty make should have raised ValueError")
        return False
    except ValueError:
        print("✓ Empty make properly rejected")
    
    # Test invalid year
    try:
        my_car.set_year(1800)  # Too early should fail
        print("✗ Invalid year should have raised ValueError")
        return False
    except ValueError:
        print("✓ Invalid year properly rejected")
    
    # Test invalid year type
    try:
        my_car.set_year("2024")  # String should fail
        print("✗ String year should have raised ValueError")
        return False
    except ValueError:
        print("✓ Non-integer year properly rejected")
    
    print()
    return True


def test_method_functionality():
    """
    Test that the public methods work correctly and use private attributes.
    
    This test verifies that the car's methods properly interact with
    the encapsulated attributes.
    """
    print("Testing Method Functionality...")
    print("-" * 40)
    
    # Create a car instance
    my_car = Car("BMW", "X5", 2023, "White", max_gas_capacity=20.0)
    
    # Test initial state
    try:
        assert my_car.is_tank_empty(), "Tank should start empty"
        assert not my_car.is_tank_full(), "Tank should not start full"
        print("✓ Initial tank state is correct")
        
    except AssertionError as e:
        print(f"✗ Initial state test failed: {e}")
        return False
    
    # Test adding gas
    try:
        gas_added = my_car.add_gas(10.0)
        assert gas_added == 10.0, f"Expected 10.0 gallons added, got {gas_added}"
        assert my_car.get_gas_level() == 10.0, f"Expected gas level 10.0, got {my_car.get_gas_level()}"
        assert not my_car.is_tank_empty(), "Tank should not be empty after adding gas"
        assert not my_car.is_tank_full(), "Tank should not be full after adding 10 gallons"
        print("✓ Adding gas works correctly")
        
    except AssertionError as e:
        print(f"✗ Add gas test failed: {e}")
        return False
    
    # Test overfilling
    try:
        gas_added = my_car.add_gas(15.0)  # Try to add more than capacity allows
        expected_added = 10.0  # Should only add 10 more (20 total capacity - 10 current = 10 available)
        assert gas_added == expected_added, f"Expected {expected_added} gallons added, got {gas_added}"
        assert my_car.get_gas_level() == 20.0, f"Expected gas level 20.0, got {my_car.get_gas_level()}"
        assert my_car.is_tank_full(), "Tank should be full after adding maximum gas"
        print("✓ Overfill protection works correctly")
        
    except AssertionError as e:
        print(f"✗ Overfill test failed: {e}")
        return False
    
    # Test using gas
    try:
        success = my_car.use_gas(5.0)
        assert success, "Should be able to use 5 gallons"
        assert my_car.get_gas_level() == 15.0, f"Expected gas level 15.0, got {my_car.get_gas_level()}"
        print("✓ Using gas works correctly")
        
        # Test using more gas than available
        success = my_car.use_gas(20.0)
        assert not success, "Should not be able to use more gas than available"
        assert my_car.get_gas_level() == 15.0, f"Gas level should remain 15.0, got {my_car.get_gas_level()}"
        print("✓ Insufficient gas protection works correctly")
        
    except AssertionError as e:
        print(f"✗ Use gas test failed: {e}")
        return False
    
    # Test car information methods
    try:
        info = my_car.get_car_info()
        assert "BMW" in info, "Car info should contain make"
        assert "X5" in info, "Car info should contain model"
        assert "2023" in info, "Car info should contain year"
        assert "White" in info, "Car info should contain color"
        assert "15.0" in info, "Car info should contain current gas level"
        print("✓ Car information method works correctly")
        
        # Test print method (should not raise any errors)
        print("Testing print_car_info method:")
        my_car.print_car_info()
        print("✓ Print car info method works correctly")
        
    except AssertionError as e:
        print(f"✗ Car info test failed: {e}")
        return False
    
    print()
    return True


def test_validation_and_error_handling():
    """
    Test that the class properly validates input and handles errors.
    
    This test verifies that the encapsulation includes proper validation
    to maintain data integrity.
    """
    print("Testing Validation and Error Handling...")
    print("-" * 40)
    
    # Create a car instance
    my_car = Car("Tesla", "Model S", 2023, "Silver")
    
    # Test invalid gas amounts
    try:
        my_car.add_gas(-5.0)  # Negative amount should fail
        print("✗ Negative gas amount should have raised ValueError")
        return False
    except ValueError:
        print("✓ Negative gas amount properly rejected")
    
    try:
        my_car.add_gas("10")  # String amount should fail
        print("✗ String gas amount should have raised ValueError")
        return False
    except ValueError:
        print("✓ Non-numeric gas amount properly rejected")
    
    try:
        my_car.use_gas(-3.0)  # Negative amount should fail
        print("✗ Negative gas usage should have raised ValueError")
        return False
    except ValueError:
        print("✓ Negative gas usage properly rejected")
    
    # Test constructor validation
    try:
        # Test with invalid year
        invalid_car = Car("Honda", "Civic", "2023", "Blue")  # String year
        print("✗ String year in constructor should have caused issues")
    except (ValueError, TypeError):
        print("✓ Constructor properly handles invalid data types")
    
    print()
    return True


def test_encapsulation_principles():
    """
    Test that encapsulation principles are properly implemented.
    
    This test demonstrates the benefits of encapsulation by showing
    controlled access and data integrity.
    """
    print("Testing Encapsulation Principles...")
    print("-" * 40)
    
    # Create a car instance
    my_car = Car("Audi", "A4", 2023, "Gray")
    
    # Demonstrate controlled access
    print("Demonstrating controlled access through getters:")
    print(f"Make: {my_car.get_make()}")
    print(f"Model: {my_car.get_model()}")
    print(f"Year: {my_car.get_year()}")
    print(f"Color: {my_car.get_color()}")
    
    # Demonstrate controlled modification through setters
    print("\nDemonstrating controlled modification through setters:")
    original_make = my_car.get_make()
    my_car.set_make("Mercedes")
    print(f"Changed make from '{original_make}' to '{my_car.get_make()}'")
    
    # Demonstrate data integrity through validation
    print("\nDemonstrating data integrity through validation:")
    try:
        my_car.set_year(1800)  # Should fail
    except ValueError as e:
        print(f"Validation prevented invalid year: {e}")
    
    # Demonstrate that private attributes are still accessible (but shouldn't be used)
    print(f"\nNote: Private attributes are still accessible in Python:")
    print(f"Direct access to _make: {my_car._make}")
    print("However, this violates encapsulation principles and should be avoided!")
    
    print()
    return True


def run_all_tests():
    """
    Run all encapsulation tests and provide a summary.
    
    Returns:
        bool: True if all tests passed, False otherwise
    """
    print("CAR ENCAPSULATION TEST SUITE")
    print("=" * 50)
    
    tests = [
        ("Direct Attribute Access", test_direct_attribute_access),
        ("Getters and Setters", test_getters_and_setters),
        ("Method Functionality", test_method_functionality),
        ("Validation and Error Handling", test_validation_and_error_handling),
        ("Encapsulation Principles", test_encapsulation_principles)
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            if result is not False:  # None or True both count as passed
                passed_tests += 1
                print(f"✓ {test_name}: PASSED")
            else:
                print(f"✗ {test_name}: FAILED")
        except Exception as e:
            print(f"✗ {test_name}: ERROR - {e}")
    
    print("\n" + "=" * 50)
    print(f"TEST SUMMARY: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("All tests passed! Encapsulation is properly implemented.")
        return True
    else:
        print("Some tests failed. Please review the encapsulation implementation.")
        return False


def main():
    """
    Main function to run the encapsulation tests.
    """
    success = run_all_tests()
    
    if not success:
        sys.exit(1)  # Exit with error code if tests failed


if __name__ == "__main__":
    main()
