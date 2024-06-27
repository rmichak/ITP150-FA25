### HW-Assignment-7

### Functions

#### Problem 1: Function with Parameters
Write a function `calculate_area` that takes two parameters, `length` and `width`, and returns the area of a rectangle. Use this function to calculate the area of a rectangle with length 10 and width 5.

#### Problem 2: Return Values and Scope
Create a function `get_full_name` that takes two parameters, `first_name` and `last_name`, and returns the full name. Also, demonstrate the difference between local and global variables by defining a global variable `greeting` and using it inside the function.

### Exceptions:

### Problem 1: Safe Division
Write a function `safe_divide` that takes two numbers as input and returns their division result. The function should handle the following exceptions:
1. `ZeroDivisionError` if the second number is zero.
2. `TypeError` if either of the inputs is not a number.

**Test Cases:**
1. `safe_divide(10, 2)` should return `5.0`
2. `safe_divide(10, 0)` should return `"Error: Division by zero is not allowed."`
3. `safe_divide(10, 'a')` should return `"Error: Both inputs must be numbers."`

### Problem 2: Square Root Calculation
Write a function `safe_sqrt` that takes a number as input and returns its square root. The function should handle the following exceptions:
1. `ValueError` if the input is negative.
2. `TypeError` if the input is not a number.

**Test Cases:**
1. `safe_sqrt(9)` should return `3.0`
2. `safe_sqrt(-4)` should return `"Error: Cannot calculate the square root of a negative number."`
3. `safe_sqrt('nine')` should return `"Error: Input must be a number."`
