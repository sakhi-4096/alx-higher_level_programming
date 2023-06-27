# Python - Exceptions 
A way to handle errors or exceptional conditions

## Description
In Python, exceptions are a way to handle errors or exceptional conditions that may occur during the execution of a program. When an error occurs, an exception object is raised, which can be caught and handled by appropriate exception handling code.
Python provides a built-in hierarchy of exception classes, and you can also define your own custom exception classes.

## Features
 * Exception: The base class for all exceptions in Python.
 * SyntaxError: Raised when a syntax error is encountered.
 * TypeError: Raised when an operation or function is applied to an object of inappropriate type.
 * NameError: Raised when a local or global name is not found.
 * ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.
 * IndexError: Raised when a sequence subscript is out of range.
 * KeyError: Raised when a dictionary key is not found.
 * FileNotFoundError: Raised when a file or directory is requested but cannot be found.
 * IOError: Raised when an input/output operation fails.
 * ZeroDivisionError: Raised when division or modulo by zero is performed.

## Usage
```python
try:
    # Code that might raise an exception
    # ...
except ExceptionType1:
    # Exception handling code for ExceptionType1
except ExceptionType2:
    # Exception handling code for ExceptionType2
else:
    # Optional block executed if no exception occurred
finally:
    # Optional block always executed, regardless of whether an exception occurred or not
```

## Examples
```python
try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    result = dividend / divisor
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An error occurred:", str(e))
else:
    print("Division performed successfully.")
finally:
    print("Program execution complete.")
```

## Credits
 * [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
 * [Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
