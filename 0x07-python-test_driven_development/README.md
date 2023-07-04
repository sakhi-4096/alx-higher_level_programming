# Python - Test Driven Development
Test-driven development (TDD) is a software development approach that emphasizes writing tests before writing the code
![Test-driven development](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-4.gif)

## Description
TDD is a way of writing software where we start by writing tests before we even start writing the actual code. It follows a cycle of writing a test, writing the minimum amount of code to pass the test, and then refactoring the code.

## Features
 * **Test-First Approach:** TDD emphasizes writing tests before writing the actual code. This ensures that the code is driven by the desired behavior and functionality defined by the tests.
 * **Incremental Development:** TDD promotes an iterative development process. Developers start by writing a failing test and then implement the minimum amount of code required to make that test pass. The process is repeated for each new functionality or behavior.
 * **Red-Green-Refactor Cycle:** TDD follows a cycle of "red, green, refactor." The initial test is written, which fails(red). Then, the code is implemented to make the test pass (green). After that, the code is refactored to improve its design, readability, and efficiency while ensuring that all tests continue to pass.
 * **Test Automation:** TDD encourages the use of automated testing frameworks, such as *unittest* or *doctest*, to execute tests consistently and efficiently. Automation enables developers to run tests frequently and ensures that any regressions are caught early.
 * **Continuous Integration:** TDD works well with continuous integration practices. The automated tests written during TDD can be integrated into a continuous integration pipeline, allowing tests to be executed automatically whenever changes are made to the codebase. This helps in identifying and resolving issues early in the development process.
 * **Design Improvement:** TDD promotes better design practices by forcing developers to think about the code's structure and interface before writing it. The iterative nature of TDD allows for continuous refactoring, resulting in cleaner, modular, and maintainable code.
 * **Documentation and Living Documentation:** TDD encourages the use of test cases as living documentation. By writing tests that define the desired behavior, developers ensure that the tests always reflect the expected functionality. This serves as executable documentation and helps in understanding the codebase.

## Usage
```python
import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
```

## Examples
```python
class TestMultiply(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_multiply_negative_numbers(self):
        result = multiply(-2, 3)
        self.assertEqual(result, -6)

    def test_multiply_mixed_sign_numbers(self):
        result = multiply(-2, -3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
```

## Credits
 * [Unit Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI)
 * [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
