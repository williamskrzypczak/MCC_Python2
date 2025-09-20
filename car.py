"""
Car Class Implementation
Assignment: Testing Encapsulation in Python Classes

This module implements a Car class that demonstrates proper encapsulation
with private attributes and public getter/setter methods.

Author: Student
Date: 2024
"""


class Car:
    """
    A class representing a car with encapsulated attributes.
    
    This class demonstrates proper encapsulation by using private attributes
    (prefixed with underscore) and providing public getter and setter methods
    to access and modify the attributes safely.
    
    Attributes:
        _make (str): The make/brand of the car (private)
        _model (str): The model of the car (private)
        _year (int): The year the car was manufactured (private)
        _color (str): The color of the car (private)
        _gas_level (float): Current gas level in the tank (private)
        _max_gas_capacity (float): Maximum gas tank capacity (private)
    """
    
    def __init__(self, make, model, year, color, max_gas_capacity=15.0):
        """
        Initialize a Car object with encapsulated attributes.
        
        Args:
            make (str): The make/brand of the car
            model (str): The model of the car
            year (int): The year the car was manufactured
            color (str): The color of the car
            max_gas_capacity (float): Maximum gas tank capacity (default: 15.0)
        """
        # Private attributes (encapsulated)
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._gas_level = 0.0  # Start with empty tank
        self._max_gas_capacity = max_gas_capacity
    
    # Getter methods (provide controlled access to private attributes)
    
    def get_make(self):
        """Get the make/brand of the car."""
        return self._make
    
    def get_model(self):
        """Get the model of the car."""
        return self._model
    
    def get_year(self):
        """Get the year the car was manufactured."""
        return self._year
    
    def get_color(self):
        """Get the color of the car."""
        return self._color
    
    def get_gas_level(self):
        """Get the current gas level."""
        return self._gas_level
    
    def get_max_gas_capacity(self):
        """Get the maximum gas tank capacity."""
        return self._max_gas_capacity
    
    # Setter methods (provide controlled modification of private attributes)
    
    def set_make(self, make):
        """
        Set the make/brand of the car.
        
        Args:
            make (str): The new make/brand
            
        Raises:
            ValueError: If make is not a valid string
        """
        if not isinstance(make, str) or not make.strip():
            raise ValueError("Make must be a non-empty string")
        self._make = make.strip()
    
    def set_model(self, model):
        """
        Set the model of the car.
        
        Args:
            model (str): The new model
            
        Raises:
            ValueError: If model is not a valid string
        """
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string")
        self._model = model.strip()
    
    def set_year(self, year):
        """
        Set the year the car was manufactured.
        
        Args:
            year (int): The new year
            
        Raises:
            ValueError: If year is not a valid integer or is unrealistic
        """
        if not isinstance(year, int) or year < 1886 or year > 2030:
            raise ValueError("Year must be an integer between 1886 and 2030")
        self._year = year
    
    def set_color(self, color):
        """
        Set the color of the car.
        
        Args:
            color (str): The new color
            
        Raises:
            ValueError: If color is not a valid string
        """
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Color must be a non-empty string")
        self._color = color.strip()
    
    # Public methods that use private attributes
    
    def add_gas(self, amount):
        """
        Add gas to the car's tank.
        
        Args:
            amount (float): Amount of gas to add in gallons
            
        Returns:
            float: Amount of gas actually added
            
        Raises:
            ValueError: If amount is negative or not a number
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Gas amount must be a non-negative number")
        
        # Calculate how much gas can actually be added
        available_space = self._max_gas_capacity - self._gas_level
        gas_added = min(amount, available_space)
        
        self._gas_level += gas_added
        
        return gas_added
    
    def use_gas(self, amount):
        """
        Use gas from the car's tank.
        
        Args:
            amount (float): Amount of gas to use in gallons
            
        Returns:
            bool: True if there was enough gas, False otherwise
            
        Raises:
            ValueError: If amount is negative or not a number
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Gas amount must be a non-negative number")
        
        if amount <= self._gas_level:
            self._gas_level -= amount
            return True
        else:
            return False
    
    def get_car_info(self):
        """
        Get comprehensive information about the car.
        
        Returns:
            str: Formatted string with all car information
        """
        return (f"Car Information:\n"
                f"  Make: {self._make}\n"
                f"  Model: {self._model}\n"
                f"  Year: {self._year}\n"
                f"  Color: {self._color}\n"
                f"  Gas Level: {self._gas_level:.1f}/{self._max_gas_capacity:.1f} gallons")
    
    def print_car_info(self):
        """Print comprehensive information about the car."""
        print(self.get_car_info())
    
    def is_tank_full(self):
        """
        Check if the gas tank is full.
        
        Returns:
            bool: True if tank is full, False otherwise
        """
        return self._gas_level >= self._max_gas_capacity
    
    def is_tank_empty(self):
        """
        Check if the gas tank is empty.
        
        Returns:
            bool: True if tank is empty, False otherwise
        """
        return self._gas_level <= 0
    
    # Magic methods for better object representation
    
    def __str__(self):
        """Return a string representation of the car."""
        return f"{self._year} {self._make} {self._model} ({self._color})"
    
    def __repr__(self):
        """Return an official string representation of the car."""
        return (f"Car(make='{self._make}', model='{self._model}', "
                f"year={self._year}, color='{self._color}', "
                f"max_gas_capacity={self._max_gas_capacity})")
