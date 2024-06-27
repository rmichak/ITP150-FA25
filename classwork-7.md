### Module 7: Functions

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
