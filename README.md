# Dog Classes Assignment

## Assignment Overview
This assignment demonstrates inheritance and polymorphism concepts by creating a class diagram and implementing additional dog classes based on the American Kennel Club (AKC) dog groups.

## Files Included
- `dog_classes.py` - Main Python implementation with all dog classes
- `dog_class_diagram.txt` - Text-based class diagram showing inheritance relationships
- `README.md` - This documentation file

## Class Structure

### Base Class: Dog
The `Dog` class serves as the base class with common attributes and methods:
- **Attributes**: `average_weight`, `height_range`, `life_span`, `color`
- **Methods**: `bark()`, `eat()`, `sleep()`, `get_info()`

### Derived Classes

#### 1. SportingDog (inherits from Dog)
Represents sporting/hunting dogs like Golden Retrievers, Labradors, etc.
- **Additional Attributes**: `hunting_ability`, `water_resistance`
- **Additional Methods**: `hunt()`, `retrieve()`, `swim()`

#### 2. WorkingDog (inherits from Dog)
Represents working/guard dogs like German Shepherds, Huskies, etc.
- **Additional Attributes**: `work_type`, `strength_level`
- **Additional Methods**: `guard()`, `pull_sled()`, `search_rescue()`

## Key Concepts Demonstrated

### 1. Inheritance
- Both `SportingDog` and `WorkingDog` inherit from the base `Dog` class
- They use `super().__init__()` to properly initialize parent class attributes
- They inherit all base methods while adding their own specialized ones

### 2. Polymorphism
- Method overriding: Both derived classes override the `get_info()` method
- Interface consistency: All classes can use the same method names (`bark()`, `eat()`, `sleep()`)
- Type checking: `isinstance()` demonstrates inheritance relationships

### 3. Encapsulation
- All attributes are properly encapsulated within each class
- Methods provide controlled access to object state

## Running the Code

### Prerequisites
- Python 3.x installed on your system

### Execution
```bash
python3 dog_classes.py
```

### Expected Output
The program will demonstrate:
1. Creating instances of each dog class
2. Basic dog behaviors (inherited methods)
3. Specialized behaviors (unique to each class)
4. Polymorphism through method overriding
5. Inheritance relationships
6. Polymorphism with lists of different dog types

## Sample Output
```
Dog Classes Demonstration
==================================================
1. Creating a Sporting Dog (Golden Retriever):
2. Creating a Working Dog (German Shepherd):

3. Demonstrating Basic Dog Behaviors (Inherited):
----------------------------------------
Golden Retriever basic behaviors:
  Bark: Woof! Woof!
  Eat: This golden dog is eating its food.
  Sleep: This 65 pound dog is taking a nap.

4. Demonstrating Sporting Dog Specialized Behaviors:
----------------------------------------
  Hunt: This excellent hunting dog is tracking game!
  Retrieve: This golden sporting dog is retrieving the ball.
  Swim: This golden sporting dog is swimming in the water!

5. Demonstrating Working Dog Specialized Behaviors:
----------------------------------------
  Guard: This very strong black and tan working dog is guarding the property!
  Pull Sled: This 75 pound working dog is pulling a sled.
  Search & Rescue: This police work dog is searching for survivors.
```

## Class Diagram
The `dog_class_diagram.txt` file contains a text-based representation of the class hierarchy. You can use this as a reference to create a visual diagram using tools like:
- draw.io
- Lucidchart
- Visual Studio Code with PlantUML extension
- Any UML diagramming software

## Learning Objectives Met
✅ **Inheritance**: Proper class hierarchy with base and derived classes  
✅ **Polymorphism**: Method overriding and interface consistency  
✅ **Encapsulation**: Proper attribute and method organization  
✅ **Documentation**: Comprehensive docstrings and comments  
✅ **Practical Application**: Real-world dog breed examples  

## Extending the Code
You can easily extend this implementation by:
1. Adding more dog classes (ToyDog, HoundDog, etc.)
2. Implementing additional methods for each class
3. Adding more sophisticated behaviors and interactions
4. Creating a dog management system that uses these classes

## Assignment Submission
For submission, include:
1. The Python script (`dog_classes.py`)
2. A visual class diagram (created from `dog_class_diagram.txt`)
3. This README file
4. Any additional documentation or notes
