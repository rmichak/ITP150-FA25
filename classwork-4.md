## Module 6: Decision Control Structures

### Table of Contents
1. If-Then Control Structures
2. Relational Operators
3. Multiple Conditions
4. Conditional Logical Operators
5. Activities and Exercises

### 1. If-Then Control Structures
Control structures alter the sequential execution of statements in a program. The if-then control structure is used to direct the program flow based on a condition.

#### Example:
```python
if condition:
    # statements to execute if condition is True
```

#### Key Points:
- The condition is followed by a colon.
- The statements inside the if block are indented.

### 2. Relational Operators
Relational operators compare two operands and return a Boolean value (True or False).

#### Common Relational Operators:
- `==` (equal to)
- `!=` (not equal to)
- `<` (less than)
- `>` (greater than)
- `<=` (less than or equal to)
- `>=` (greater than or equal to)

#### Example:
```python
a = 10
b = 20

print(a == b)  # False
print(a < b)   # True
```

### 3. Multiple Conditions
Multiple conditions can be handled using if-then-else and nested-if structures.

#### If-Then-Else Structure:
```python
if condition:
    # statements if condition is True
else:
    # statements if condition is False
```

#### Example:
```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

#### Nested-If Structure:
```python
if condition1:
    if condition2:
        # statements if both conditions are True
    else:
        # statements if condition1 is True and condition2 is False
else:
    # statements if condition1 is False
```

### 4. Conditional Logical Operators
Logical operators combine multiple Boolean expressions.

#### Common Logical Operators:
- `and` (both conditions must be True)
- `or` (at least one condition must be True)
- `not` (negates the Boolean value)

#### Example:
```python
x = 5
y = 10
z = 15

if x < y and y < z:
    print("Both conditions are True")
```

### 5. Activities and Exercises

#### Activity 1: If-Then Structure
Write a program that checks if a number is positive, negative, or zero.

```python
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

#### Activity 2: Relational Operators
Write a program that compares two numbers and prints whether they are equal or which one is greater.

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 == num2:
    print("Both numbers are equal.")
elif num1 > num2:
    print("The first number is greater.")
else:
    print("The second number is greater.")
```

#### Activity 3: Logical Operators
Write a program that checks if a number is between 10 and 20 (inclusive).

```python
number = int(input("Enter a number: "))

if number >= 10 and number <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")
```
