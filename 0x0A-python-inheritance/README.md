# Python - Inheritance 
Inheritance is a fundamental concept in object-oriented programming and plays a crucial role in creating modular, extensible, and maintainable code.

## Description
Inheritance is a fundamental concept in object-oriented programming and plays a crucial role in creating modular, extensible, and maintainable code. It helps to organize code hierarchically, promote code reuse, and enable customization and specialization of behavior. In Python, inheritance allows you to create new classes that inherit attributes and methods from existing classes. This enables code reuse and promotes a hierarchical organization of classes.

## Features
 * **Code Reusability:** Inheritance allows you to reuse code from existing classes. Subclasses inherit attributes and methods from their base classes, reducing code duplication and promoting modular design.
 * **Class Hierarchy:** Inheritance enables the creation of a hierarchical structure of classes, where subclasses inherit from parent or base classes. This hierarchy represents relationships and classifications among different entities in your code.
 * **Overriding Methods:** Subclasses can override methods inherited from base classes to provide their own implementations. This allows customization and specialization of behavior specific to the subclass while still utilizing the common functionality inherited from the base class.
 * **Access to Inherited Members:** Subclasses have access to the attributes and methods inherited from their base classes. This allows them to use and manipulate inherited members as if they were their own.
 * **Polymorphism:** Inheritance is closely related to the concept of polymorphism, which allows objects of different classes to be used interchangeably when they share a common base class. Polymorphism enables flexibility and modularity in the design of your code.
 * **Multiple Inheritance:** Python supports multiple inheritance, which means a subclass can inherit from multiple base classes. This feature allows you to combine attributes and methods from different classes, providing more flexibility in designing complex relationships between classes.

## Usage
```python
class SubClassName(BaseClassName):
    # Additional attributes and methods specific to the subclass
```

## Examples
```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")


class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def drive(self):
        print(f"Driving the {self.color} car")


# Create an instance of the Car class
my_car = Car("Toyota", 2021, "red")

# Access attributes and methods from the base class
print(my_car.brand)    # Output: Toyota
print(my_car.year)     # Output: 2021

# Call methods from the base class
my_car.start_engine()  # Output: Engine started

# Call methods specific to the subclass
my_car.drive()         # Output: Driving the red car
```

## Credits
 * [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
 * [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
 * [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
 * [Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
