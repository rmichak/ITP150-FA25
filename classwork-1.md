# Python Basics

## Comments

In Python, comments are used to add explanatory notes or documentation within your code. Comments are ignored by the Python interpreter and are purely for human readability. There are two types of comments in Python:

1. Single-line comments: These start with the `#` symbol and continue until the end of the line.

```python
# This is a single-line comment
print("Hello, World!")  # This comment is after a statement
```

2. Multi-line comments (docstrings): These are enclosed within triple quotes (`'''` or `"""`) and are often used for function and module-level documentation.

```python
'''
This is a multi-line comment
It can span multiple lines
'''
print("Hello, World!")
```

## Print

In Python, you can use the `print()` function to display output on the console.

```python
print("Hello, World!")  # Output: Hello, World!
```

## Strings

Strings are sequences of characters in Python, and they can be defined using single (' '), double (" "), or triple (''' ''' or """ """) quotes.

```python
single_quoted = 'Hello, World!'
double_quoted = "Hello, World!"
triple_quoted = '''Hello,
World!'''
```

## Variables

Variables are used to store data in Python. You can create a variable and assign a value to it using the assignment operator `=`.

```python
name = "Alice"
age = 30
```

## Numbers

Python supports different types of numbers, including integers and floating-point numbers.

```python
integer_num = 42
float_num = 3.14
```

## Calculations

You can perform arithmetic calculations in Python using operators like `+`, `-`, `*`, and `/`.

```python
result = 5 + 3  # Addition
result = 10 - 2  # Subtraction
result = 4 * 6  # Multiplication
result = 12 / 3  # Division
```

## Exponents

You can calculate exponents using the `**` operator.

```python
result = 2 ** 3  # 2 raised to the power of 3 is 8
```

## Modulo

The modulo operator `%` is used to find the remainder of a division operation.

```python
remainder = 10 % 3  # 10 divided by 3 leaves a remainder of 1
```

## Concatenation

You can concatenate (combine) strings using the `+` operator.

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
```

## Plus Equals

The `+=` operator is used to update the value of a variable by adding another value to it.

```python
x = 5
x += 2  # Equivalent to x = x + 2
```

## Multi-line strings

Multi-line strings are often used for documentation or when you need to preserve line breaks.

```python
multiline_string = '''
This is a
multi-line
string.
'''
```
