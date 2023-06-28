# Python - Classes and Objects 
Classes and objects are used to implement object-oriented programming (OOP) concepts.
![Object Oriented Programming](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg)

## Description
In Python, classes and objects are used to implement object-oriented programming (OOP) concepts. A class is a blueprint for creating objects, while an object is an instance of a class. Classes define the properties (attributes) and behaviors (methods) that objects of that class can have.

## Features
 * **Encapsulation:** Classes allow you to encapsulate data (attributes) and behavior (methods) into a single unit. This helps organize and structure code by grouping related data and functions together.
 * **Abstraction:** Classes provide abstraction by hiding the internal details of an object and exposing only the necessary information and functionality. This allows for a simplified and intuitive interaction with objects, as users can focus on what an object does rather than how it does it.
 * **Reusability:** Classes enable code reusability. Once a class is defined, you can create multiple instances (objects) of that class. These objects inherit the attributes and methods defined in the class, allowing you to reuse the code and avoid duplication.
 * **Inheritance:** Inheritance allows classes to inherit attributes and methods from other classes. This promotes code reuse and supports the creation of hierarchies of classes, where subclasses inherit and extend the functionality of their parent (super) class.
 * **Polymorphism:** Polymorphism enables objects of different classes to be treated as objects of a common superclass. This allows for code flexibility and extensibility, as objects can be used interchangeably based on their common interface or superclass type.
 * **Modularity:** Classes facilitate modular programming by breaking down complex systems into smaller, manageable units. Each class can be designed to handle a specific responsibility or represent a distinct component, promoting code organization and maintainability.
 * **State and behavior:** Objects store state (data or attributes) and exhibit behavior (methods or functions). The state represents the object's properties, and the behavior represents the actions or operations that the object can perform. Classes allow you to define and control both the state and behavior of objects.
 * **Data abstraction:** Classes allow you to define custom data types by combining data and related operations into a single entity. This enables you to create meaningful abstractions that model real-world concepts or solve specific problems.

## Usage
```python
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()
```

## Examples
```python
class Person:
    """
    A class representing a person.
    """

    def __init__(self, name, age):
        """
        Initialize a new Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age
    
    def say_hello(self):
        """
        Print a greeting with the person's name.
        """
        print("Hello, my name is", self.name)

# Creating objects (instances) of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing object attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# Calling object methods
person1.say_hello()  # Output: Hello, my name is Alice
person2.say_hello()  # Output: Hello, my name is Bob

```

## Credits
 * [Object Oriented Programming](https://python.swaroopch.com/oop.html)
 * [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
 * [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
 * [Python Classes and Objects](https://youtu.be/apACNr7DC_s)
 * [Object Oriented Programming](https://youtu.be/-DP1i2ZU9gk)
 * [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
