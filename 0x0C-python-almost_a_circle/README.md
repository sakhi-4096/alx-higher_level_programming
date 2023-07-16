# Python - Python Almost a Circle 
Is a project that employs object-oriented programming and JSON serialization to create, manage, and store data, providing a simple and efficient way to organize and access data.

## Description
The Python Almost a Circle is a Python-based project that aims to efficiently manage information. It utilizes various object-oriented programming concepts and other Python features to handle data, perform data manipulations, and store the information in a file using JSON serialization/deserialization.

## Features
 * **Import:** The project will utilize Python's import statement to include necessary modules and libraries to enhance functionality, such as json for JSON handling and unittest for testing.
 * **Exceptions:** The code will implement exception handling to gracefully handle potential errors or unexpected situations during file I/O and data operations.
 * **Class and Private Attribute:** The project will define a class with private attributes to encapsulate data and prevent direct access from outside the class.
 * **Getter/Setter:** The class will use getter and setter methods to access and modify private attributes in a controlled manner.
 * **Class Method:** A class method may be implemented to create specialized constructors or perform specific operations related to the class.
 * **Static Method:** Static methods might be used for utility functions that don't require access to instance-specific data.
 * **Inheritance:** The project could have additional classes, inheriting from the super class, demonstrating the concept of inheritance.
 * **Unittest:** To ensure code quality and functionality, the project will include unit tests using Python's unittest framework.
 * **Read/Write File:** The project will read and write employee data from/to a JSON file. The file acts as a persistent storage system, allowing data to be retained even after the program terminates.
 * **Args and Kwargs:** Functions and methods may accept variable-length arguments (*args*) and keyword arguments (*kwargs*) to enhance flexibility.
 * **Serialization/Deserialization:** The project will use JSON serialization to convert Python objects (e.g., class instances) into JSON format for storage in the file. Deserialization will be employed to convert JSON data back into Python objects.

## Examples
```python
import json

class Employee:
    def __init__(self, emp_id, name, position):
        self.__emp_id = emp_id
        self.__name = name
        self.__position = position

    # Getter methods
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def to_dict(self):
        return {
            "emp_id": self.__emp_id,
            "name": self.__name,
            "position": self.__position
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["emp_id"], data["name"], data["position"])


def save_employees_to_file(employees, filename):
    with open(filename, "w") as file:
        json.dump([emp.to_dict() for emp in employees], file)


def load_employees_from_file(filename):
    employees = []
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            for emp_data in data:
                employees.append(Employee.from_dict(emp_data))
    except FileNotFoundError:
        pass
    return employees
```

## Usage
```python
if __name__ == "__main__":
    emp1 = Employee(1, "John Doe", "Software Engineer")
    emp2 = Employee(2, "Jane Smith", "Product Manager")
    employees_list = [emp1, emp2]

    # Save employees to file
    save_employees_to_file(employees_list, "employees.json")

    # Load employees from file
    loaded_employees = load_employees_from_file("employees.json")

    # Output loaded employees
    for emp in loaded_employees:
        print(f"Employee ID: {emp.get_emp_id()}, Name: {emp.get_name()}, Position: {emp.get_position()}")

```

## Credits
 * [\*args and \*\*kwargs in python explained](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
 * [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
 * [Unit testing framework](https://docs.python.org/3.4/library/unittest.html#module-unittest)
 * [A simple Python unittest](https://www.pythonsheets.com/notes/python-tests.html)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
