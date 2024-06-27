### Module 7

### Part -1 : Functions

This tutorial will cover the essentials of Python functions, based on the provided slides. Functions are a fundamental concept in programming, enabling code modularity, reusability, and better organization.

#### 1. Function Basics
Functions in Python can be classified into three types:
- **Built-in functions**: Provided by Python (e.g., `print()`, `len()`).
- **Imported functions**: Functions from external modules (e.g., `math.sqrt()`).
- **Programmer-defined functions**: Functions created by the programmer.

##### Example:
```python
# Built-in function
print("Hello, World!")

# Imported function
import math
print(math.sqrt(16))

# Programmer-defined function
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
```

##### Advantages of Functions:
- **Modularization**: Grouping related code together.
- **Simplification of modifications**: Changes in a function affect only that function.
- **Reduction of code duplication**: Reusing functions across the program.
- **Encapsulation**: Isolating code to simplify debugging.

#### 2. Void Functions
Void functions perform a task but do not return a value to the caller.

##### Example:
```python
def print_greeting(name):
    print(f"Hello, {name}!")

print_greeting("Bob")
```

##### Key Characteristics:
- Do not use the `return` statement to send back a value.
- Typically used for actions like printing or modifying data in place.

#### 3. Functions with Parameters
Functions can accept parameters to operate on different data.

##### Example:
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

##### Concepts:
- **Parameters**: Variables listed in the function definition.
- **Arguments**: Actual values passed to the function when called.

#### 4. Return Values
Functions can return values to the caller, enabling the main program to use the result.

##### Example:
```python
def multiply(a, b):
    return a * b

product = multiply(4, 3)
print(product)  # Output: 12
```

##### Returning Multiple Values:
```python
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x, y)  # Output: 10 20
```

#### 5. Scope
Scope determines the visibility of variables within different parts of a program.

##### Example:
```python
global_var = "I am global"

def some_function():
    local_var = "I am local"
    print(global_var)
    print(local_var)

some_function()
# print(local_var)  # This will cause an error because local_var is not defined outside the function.
```

##### Concepts:
- **Local variables**: Defined within a function, not accessible outside.
- **Global variables**: Defined outside any function, accessible everywhere.
- **Pass by value**: The function receives a copy of the argument.
- **Pass by reference**: The function can modify the original data (e.g., lists).

### Practical Activities

#### Activity 1: Simple Calculator
Create a simple calculator that can add, subtract, multiply, and divide two numbers. Use functions to perform each operation.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        print("Result:", add(num1, num2))
    elif operation == '-':
        print("Result:", subtract(num1, num2))
    elif operation == '*':
        print("Result:", multiply(num1, num2))
    elif operation == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation!")

main()
```

#### Activity 2: Multipurpose Function
Write a function that can be used in different ways by calling it with different arguments.

```python
def compute_area(shape, dimension1, dimension2=None):
    if shape == 'circle':
        return 3.14 * dimension1**2
    elif shape == 'rectangle' and dimension2:
        return dimension1 * dimension2
    elif shape == 'square':
        return dimension1**2
    else:
        return "Invalid shape or dimensions"

print(compute_area('circle', 5))  # Output: 78.5
print(compute_area('rectangle', 4, 6))  # Output: 24
print(compute_area('square', 3))  # Output: 9
```

### Part - 2: Exceptions

### Module Objectives
By the end of this tutorial, you should be able to:
1. Define exceptions and understand their use.
2. Differentiate between logic errors, semantic errors, and runtime errors.
3. Describe various types of exceptions and their use cases.
4. Implement try-except blocks to handle exceptions.
5. Understand the best practices for exception handling.

### 1. Defining Exceptions

#### Errors in Code
- **Logic Errors**: These are mistakes in the program’s logic that produce incorrect results but do not crash the program.
- **Semantic Errors**: These errors are detected by the compiler and prevent the code from running.
- **Runtime Errors**: These errors occur during the execution of the program, causing it to stop.
- **Exception**: An unexpected event that occurs during the program’s execution, preventing the program from continuing.

#### Exception Objects
Exceptions in Python are objects that contain information about the error. They can be handled using try-except blocks.

### 2. Types of Exceptions
There are many built-in exceptions in Python. Here are some common ones:

| Exception           | Situation                                              | Example                          |
|---------------------|--------------------------------------------------------|----------------------------------|
| IndexError          | An index is outside an appropriate range               | `numbers = [1, 2, 3]; print(numbers[3])` |
| NotImplementedError | A function or method was not implemented               | `raise NotImplementedError("This function is not implemented yet.")` |
| RuntimeError        | An error that does not fit any other exception type    | `raise RuntimeError("Runtime error occurred")` |
| TypeError           | A function receives an argument of incorrect type      | `print(len(42))`                 |
| ValueError          | A function receives an argument of incorrect value     | `int("abc")`                     |
| ZeroDivisionError   | Division by zero                                       | `x = 1 / 0`                      |

### 3. Handling Exceptions

#### Try-Except Block
The basic syntax for handling exceptions in Python is the try-except block:

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if the exception occurs
    print("You cannot divide by zero!")
```

#### Catching Multiple Exceptions
You can handle multiple exceptions by specifying multiple except blocks:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

#### General Exception Handling
You can catch all exceptions using a general except block, but this is not recommended for all cases as it can make debugging difficult:

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except Exception as e:
    # Code that runs if any exception occurs
    print(f"An error occurred: {e}")
```

### 4. Raising Exceptions
You can raise exceptions in your code using the `raise` keyword:

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Your age is {age}")

try:
    check_age(-1)
except ValueError as e:
    print(e)
```

### 5. Best Practices for Exception Handling
- Use specific exceptions instead of a general except block to make the code more readable and easier to debug.
- Ensure the try block contains only the code that might throw an exception.
- Avoid using exceptions for normal control flow in your programs.
- Document the exceptions that your functions can raise.
