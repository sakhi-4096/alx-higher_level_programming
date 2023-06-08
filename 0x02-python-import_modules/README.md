# Python - import and modules
Modules are Python .py files that consists of Python code. Any Python file can be referenced as a module. A Python file called hello.py has the module name of hello that can be imported into ither Python files or used on the Python command line interpreter. Modules can define functions, classes, and variables that you can reference in other Python .py files or via the Python command line interpreter.

### General
 * Why Python programming is awesome
 * How to import functions from another file
 * How to use imported functions
 * How to create a module
 * How to use the built-in function *dir()*
 * How to prevent code in your script from being executed when imported
 * How to use command line arguments with your Python programs

---
0 - Import a simple function from a simple file
 * Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
 * You have to use print function with string format to display integers
 * You have to assign:
	* the value 1 to a variable called a
	* the value 2 to a variable called b
	* and use those two variables as arguments when calling the functions add and print
 * a and b must be defined in 2 different lines: a = 1 and another b = 2
 * Your program should print: `` <a value> + <b value> = <add(a, b) value>`` followed with a new line
 * You can only use the word add_0 once in your code
 * You are not allowed to use * for importing or __import__
 * Your code should not be executed when imported - by using __import__, like the example below

1 - My first toolbox!
 * Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
 * Do not use the function print (with string format to display integers) more than 4 times
 * You have to define:
	* the value 10 to a variable a
	* the value 5 to a variable b
	* and use those two variables only, as arguments when calling functions (including print)
 * a and b must be defined in 2 different lines: a = 10 and another b = 5
 * Your program should call each of the imported functions. See example below for format
 * the word calculator_1 should be used only once in your file
 * You are not allowed to use * for importing or __import__
 * Your code should not be executed when imported

---
### Sources
 * [How To Import Modules in Python 3](https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3)
 * [How To Write Modules in Python 3](https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3)
 * [Modules](https://docs.python.org/3/tutorial/modules.html)
 * [Command Line Arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
 * [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
 * [How to Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
 * [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
 * [Pycodestyle](https://pypi.org/project/pycodestyle/)
 * [The Python Manual](https://docs.python.org/3/tutorial/index.html)
 * [Python f-strings](https://realpython.com/python-f-strings/)

### Author
 * Sakhile Ndlazi
