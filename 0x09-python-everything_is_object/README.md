# Python - Everything is an Object
Python treats everything as an object and provides a consistent interface for working with different types of objects.
![Python cat](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)

## Description
In Python, everything is an object. This means that all data values, including numbers, strings, functions, classes, and even modules, are objects with their own properties and methods. Being an object-oriented programming language, Python treats everything as an object and provides a consistent interface for working with different types of objects. Objects in Python have attributes (variables that store data) and methods (functions that operate on the object's data).

## Features
 * **Class-based Object-Oriented Programming:** Python supports class-based object-oriented programming (OOP) paradigm. You can define classes, create objects (instances), and utilize inheritance, encapsulation, and polymorphism to organize and structure your code.
 * **Dynamic Typing:** Python allows dynamic typing, meaning you can assign objects of any type to variables without declaring their types explicitly. The type of an object is determined at runtime. This flexibility allows for rapid prototyping and makes Python highly expressive.
 * **Attributes and Methods:** Objects in Python can have attributes (variables) and methods (functions) associated with them. Attributes store data, and methods define behaviors that the objects can perform. You can access and modify object attributes, and call object methods using dot notation.
 * **Inheritance and Polymorphism:** Python supports class inheritance, allowing you to define new classes (derived classes) based on existing classes (base classes). Inheritance enables code reuse, promotes modularity, and facilitates polymorphism—the ability of objects of different classes to respond to the same method calls.
 * **Object Introspection and Reflection:** Python provides powerful object introspection capabilities, allowing you to examine objects at runtime and retrieve information about their attributes, methods, and other properties. Reflection enables dynamic programming techniques by enabling code to manipulate objects based on their attributes and behaviors.
 * **First-Class Functions:** In Python, functions are treated as first-class objects, which means they can be assigned to variables, passed as arguments to other functions, returned as values from functions, and stored in data structures. This feature enables functional programming paradigms in Python.
 * **Higher-Order Functions:** Python supports higher-order functions, which are functions that can take other functions as arguments or return functions as results. This functional programming concept allows for writing more concise and expressive code, enabling techniques like function composition and closures.
 * **Object Serialization and Persistence:** Python provides built-in support for object serialization (pickling) and deserialization, allowing you to convert objects into a byte stream that can be stored or transmitted. This feature enables object persistence, interprocess communication, and data exchange between different systems.

![Python bat](https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif)

## Usage
 * This repository hosts files with answers to practice questions about python objects.

## Examples
 * Class-based Object-Oriented Programming: 
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine started!")

my_car = Car("Toyota", "Corolla")
print(my_car.make)  # Output: Toyota
my_car.start_engine()  # Output: Engine started!
```

## Credits
 * [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)
 * [9.12. Cloning lists](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
 * [Sequence Objects](https://composingprograms.com/pages/24-mutable-data.html#sequence-objects)
 * [Immutable vs Mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
 * [9.11. Aliasing](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
 * [9.10. Objects and values](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)

![Mind blown](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/70f9ea0e969dfcc407a7427aba4786d87a920494.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230705T203508Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e5e1cf1b4dd80be411f4d6497cb651c17c9bed0cd8bd8a30dee356f745a8bbed)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
