# Python - Input/Output
In Python, file input and output (I/O) operations are commonly performed using the built-in functions and methods available in the open() function and file objects. 

## Description
File I/O is a fundamental aspect of programming that allows reading data from files and writing data to files, enabling data persistence and interaction with external resources.
The Python programming language provides comprehensive support for file I/O operations, making it easy to work with different types of files, such as text files, binary files, CSV files, JSON files, and more. With Python's file I/O capabilities, you can read data from existing files, modify the data, and write the modified data back to the files.

## Features
 * **Opening Files:** Python provides the open() function to open files. It allows you to specify the file name/path and the mode (read, write, append, etc.) for file access.
 * **Reading Files:**
	* read(): Reads the entire contents of a file as a string.
	* readline(): Reads a single line from the file.
	* readlines(): Reads all lines from the file and returns them as a list.
 * **Writing to Files:**
	* write(): Writes data to a file. It overwrites the existing file contents if the file is opened in write mode.
	* writelines(): Writes a sequence of strings (e.g., list of lines) to a file.
 * **Appending to Files:**
	* Opening a file in append mode ("a") allows you to add data to the end of the file without overwriting existing contents.
 * **Closing Files:** After reading from or writing to a file, it's essential to close it using the close() method. This ensures that system resources are properly released.
 * **Context Managers:** Python supports using file objects as context managers using the with statement. This ensures that the file is automatically closed when the block of code is exited, even if an exception occurs.
 * **Error Handling:** When working with files, it's crucial to handle potential errors gracefully. Common file-related errors include FileNotFoundError and PermissionError. You can use try-except blocks to catch and handle these exceptions.
 * **File Position:** File objects keep track of the current read/write position within the file. You can use the seek() method to change the position within the file.
 * **Binary File I/O:** In addition to working with text files, Python supports reading from and writing to binary files using the appropriate modes ("rb", "wb", "ab").
 * **File Metadata:** You can retrieve information about a file, such as its size, creation/modification time, and permissions, using functions from the os module.
 * **File System Navigation:** The os module provides functions to navigate and manipulate the file system, such as checking if a file or directory exists, creating directories, deleting files, etc.
 * **File Compression:** Python offers modules like gzip, zipfile, and tarfile to handle compressed files and archives.

## Usage
```python
# Open a file for reading
file = open("example.txt", "r")

# Open a file for writing (creates a new file if it doesn't exist)
file = open("output.txt", "w")

# Open a file for appending (creates a new file if it doesn't exist)
file = open("log.txt", "a")
```

## Examples
```python
# Reading from a file
with open("input.txt", "r") as file:
    contents = file.read()
    print(contents)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("This is some text.")

# Handling potential errors
try:
    file = open("nonexistent.txt", "r")
    contents = file.read()
    print(contents)
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Insufficient permissions!")
```

## Credits
 * [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
 * [8.8. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
 * [Python Read File and Python Write to File](https://techvidvan.com/tutorials/python-file-read-write/)
 * [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
 * [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
 * [JSON encoder and decoder](https://docs.python.org/3/library/json.html)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
