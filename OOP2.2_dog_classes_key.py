"""
Dog Classes Implementation
Assignment: Creating Class Diagrams and Implementing Dog Classes

This module implements a base Dog class and two additional dog classes that inherit from it,
demonstrating inheritance and polymorphism concepts.

Classes:
    Dog: Base class for all dogs with common attributes
    SportingDog: Inherits from Dog, represents sporting/hunting dogs
    WorkingDog: Inherits from Dog, represents working/guard dogs
"""

class Dog:
    """
    Base class representing a generic dog.
    
    This class contains common attributes that all dogs share,
    regardless of their specific breed group.
    
    Attributes:
        average_weight (int): Average weight of the dog in pounds
        height_range (str): Height range of the dog
        life_span (str): Expected life span of the dog
        color (str): Color(s) of the dog's coat
    """
    
    def __init__(self, average_weight, height_range, life_span, color):
        """
        Initialize a Dog object with basic attributes.
        
        Args:
            average_weight (int): Average weight in pounds
            height_range (str): Height range description
            life_span (str): Life span description
            color (str): Coat color description
        """
        self.average_weight = average_weight
        self.height_range = height_range
        self.life_span = life_span
        self.color = color
    
    def bark(self):
        """
        Basic barking behavior for all dogs.
        
        Returns:
            str: A generic barking sound
        """
        return "Woof! Woof!"
    
    def eat(self):
        """
        Basic eating behavior for all dogs.
        
        Returns:
            str: A message about eating
        """
        return f"This {self.color} dog is eating its food."
    
    def sleep(self):
        """
        Basic sleeping behavior for all dogs.
        
        Returns:
            str: A message about sleeping
        """
        return f"This {self.average_weight} pound dog is taking a nap."
    
    def get_info(self):
        """
        Get comprehensive information about the dog.
        
        Returns:
            str: Formatted string with all dog information
        """
        return (f"Dog Information:\n"
                f"  Average Weight: {self.average_weight} pounds\n"
                f"  Height Range: {self.height_range}\n"
                f"  Life Span: {self.life_span}\n"
                f"  Color: {self.color}")


class SportingDog(Dog):
    """
    Class representing sporting/hunting dogs.
    
    Sporting dogs are bred for hunting and retrieving game.
    They are typically energetic, intelligent, and good with families.
    
    Attributes:
        average_weight (int): Average weight of the dog in pounds
        height_range (str): Height range of the dog
        life_span (str): Expected life span of the dog
        color (str): Color(s) of the dog's coat
        hunting_ability (str): Level of hunting/retrieving ability
        water_resistance (bool): Whether the dog is water-resistant
    """
    
    def __init__(self, average_weight, height_range, life_span, color, hunting_ability, water_resistance=True):
        """
        Initialize a SportingDog object.
        
        Args:
            average_weight (int): Average weight in pounds
            height_range (str): Height range description
            life_span (str): Life span description
            color (str): Coat color description
            hunting_ability (str): Level of hunting ability
            water_resistance (bool): Whether dog is water-resistant (default: True)
        """
        super().__init__(average_weight, height_range, life_span, color)
        self.hunting_ability = hunting_ability
        self.water_resistance = water_resistance
    
    def hunt(self):
        """
        Sporting dogs' specialized hunting behavior.
        
        Returns:
            str: A message about hunting behavior
        """
        return f"This {self.hunting_ability} hunting dog is tracking game!"
    
    def retrieve(self):
        """
        Sporting dogs' retrieving behavior.
        
        Returns:
            str: A message about retrieving behavior
        """
        return f"This {self.color} sporting dog is retrieving the ball."
    
    def swim(self):
        """
        Sporting dogs' swimming behavior (if water-resistant).
        
        Returns:
            str: A message about swimming ability
        """
        if self.water_resistance:
            return f"This {self.color} sporting dog is swimming in the water!"
        else:
            return f"This {self.color} sporting dog prefers to stay on land."
    
    def get_info(self):
        """
        Get comprehensive information about the sporting dog.
        
        Returns:
            str: Formatted string with all sporting dog information
        """
        base_info = super().get_info()
        return (f"{base_info}\n"
                f"  Hunting Ability: {self.hunting_ability}\n"
                f"  Water Resistant: {'Yes' if self.water_resistance else 'No'}")


class WorkingDog(Dog):
    """
    Class representing working/guard dogs.
    
    Working dogs are bred for specific tasks like guarding, pulling sleds,
    or search and rescue. They are typically strong, intelligent, and loyal.
    
    Attributes:
        average_weight (int): Average weight of the dog in pounds
        height_range (str): Height range of the dog
        life_span (str): Expected life span of the dog
        color (str): Color(s) of the dog's coat
        work_type (str): Type of work the dog is trained for
        strength_level (str): Level of physical strength
    """
    
    def __init__(self, average_weight, height_range, life_span, color, work_type, strength_level):
        """
        Initialize a WorkingDog object.
        
        Args:
            average_weight (int): Average weight in pounds
            height_range (str): Height range description
            life_span (str): Life span description
            color (str): Coat color description
            work_type (str): Type of work the dog performs
            strength_level (str): Level of physical strength
        """
        super().__init__(average_weight, height_range, life_span, color)
        self.work_type = work_type
        self.strength_level = strength_level
    
    def guard(self):
        """
        Working dogs' guarding behavior.
        
        Returns:
            str: A message about guarding behavior
        """
        return f"This {self.strength_level} {self.color} working dog is guarding the property!"
    
    def pull_sled(self):
        """
        Working dogs' sled pulling behavior.
        
        Returns:
            str: A message about sled pulling
        """
        return f"This {self.average_weight} pound working dog is pulling a sled."
    
    def search_rescue(self):
        """
        Working dogs' search and rescue behavior.
        
        Returns:
            str: A message about search and rescue work
        """
        return f"This {self.work_type} dog is searching for survivors."
    
    def get_info(self):
        """
        Get comprehensive information about the working dog.
        
        Returns:
            str: Formatted string with all working dog information
        """
        base_info = super().get_info()
        return (f"{base_info}\n"
                f"  Work Type: {self.work_type}\n"
                f"  Strength Level: {self.strength_level}")


def main():
    """
    Main function to demonstrate the Dog classes and their functionality.
    
    Creates instances of each dog class and demonstrates their
    attributes, methods, and inheritance relationships.
    """
    print("Dog Classes Demonstration")
    print("=" * 50)
    
    # Create instances of each dog class
    print("1. Creating a Sporting Dog (Golden Retriever):")
    golden_retriever = SportingDog(
        average_weight=65,
        height_range="21.5-24 inches",
        life_span="10-12 years",
        color="golden",
        hunting_ability="excellent",
        water_resistance=True
    )
    
    print("2. Creating a Working Dog (German Shepherd):")
    german_shepherd = WorkingDog(
        average_weight=75,
        height_range="22-26 inches",
        life_span="7-10 years",
        color="black and tan",
        work_type="police work",
        strength_level="very strong"
    )
    
    # Demonstrate basic Dog methods (inherited by all)
    print("\n3. Demonstrating Basic Dog Behaviors (Inherited):")
    print("-" * 40)
    
    print("Golden Retriever basic behaviors:")
    print(f"  Bark: {golden_retriever.bark()}")
    print(f"  Eat: {golden_retriever.eat()}")
    print(f"  Sleep: {golden_retriever.sleep()}")
    
    print("\nGerman Shepherd basic behaviors:")
    print(f"  Bark: {german_shepherd.bark()}")
    print(f"  Eat: {german_shepherd.eat()}")
    print(f"  Sleep: {german_shepherd.sleep()}")
    
    # Demonstrate specialized methods for SportingDog
    print("\n4. Demonstrating Sporting Dog Specialized Behaviors:")
    print("-" * 40)
    print(f"  Hunt: {golden_retriever.hunt()}")
    print(f"  Retrieve: {golden_retriever.retrieve()}")
    print(f"  Swim: {golden_retriever.swim()}")
    
    # Demonstrate specialized methods for WorkingDog
    print("\n5. Demonstrating Working Dog Specialized Behaviors:")
    print("-" * 40)
    print(f"  Guard: {german_shepherd.guard()}")
    print(f"  Pull Sled: {german_shepherd.pull_sled()}")
    print(f"  Search & Rescue: {german_shepherd.search_rescue()}")
    
    # Demonstrate polymorphism with get_info method
    print("\n6. Demonstrating Polymorphism (get_info method):")
    print("-" * 40)
    
    print("Golden Retriever Information:")
    print(golden_retriever.get_info())
    
    print("\nGerman Shepherd Information:")
    print(german_shepherd.get_info())
    
    # Demonstrate inheritance relationships
    print("\n7. Demonstrating Inheritance Relationships:")
    print("-" * 40)
    print(f"Is Golden Retriever a Dog? {isinstance(golden_retriever, Dog)}")
    print(f"Is German Shepherd a Dog? {isinstance(german_shepherd, Dog)}")
    print(f"Is Golden Retriever a SportingDog? {isinstance(golden_retriever, SportingDog)}")
    print(f"Is German Shepherd a WorkingDog? {isinstance(german_shepherd, WorkingDog)}")
    
    # Create a list of dogs to demonstrate polymorphism
    print("\n8. Demonstrating Polymorphism with a List of Dogs:")
    print("-" * 40)
    dogs = [golden_retriever, german_shepherd]
    
    for i, dog in enumerate(dogs, 1):
        print(f"Dog {i} ({type(dog).__name__}): {dog.bark()}")


if __name__ == "__main__":
    main()
