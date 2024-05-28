### Python Tutorial: Variables & Data Types

#### 1. Variables & Data Types

In Python, variables are used to store information that can be referenced and manipulated in a program. Data types specify the kind of data that can be stored and manipulated within a program.

### Variables

**Definition:** A variable is a named location in memory that stores a value. The value of a variable can change during program execution.

**Example:**

```python
# Creating variables
name = "Alice"
age = 30
height = 5.7

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
```

### Literals

**Definition:** Literals are fixed values assigned to variables. They can be of various types like integers, floating-point numbers, strings, etc.

**Example:**

```python
# Numeric literals
int_literal = 100
float_literal = 3.14

# String literals
string_literal = "Hello, World!"

# Boolean literals
bool_literal = True

print("Integer Literal:", int_literal)
print("Float Literal:", float_literal)
print("String Literal:", string_literal)
print("Boolean Literal:", bool_literal)
```

### Variables & Constants

**Variables:** As explained, variables can change their values.

**Constants:** Constants are variables whose values do not change. By convention, constants are named using uppercase letters.

**Example:**

```python
# Variable
variable_example = 42
print("Variable Example:", variable_example)

# Changing the value of the variable
variable_example = 100
print("Updated Variable Example:", variable_example)

# Constant
PI = 3.14159
print("Constant PI:", PI)
```

### Assignment Statements

**Definition:** Assignment statements are used to assign values to variables.

**Example:**

```python
# Assigning a value to a variable
x = 10
y = 20

# Assigning the result of an expression to a variable
sum = x + y
print("Sum:", sum)
```

### Input and Output

**Definition:** Input is used to get data from the user, and output is used to display data to the user.

**Example:**

```python
# Getting user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Displaying output
print("Hello,", name)
print("You are", age, "years old.")
```

### Data Types

**Definition:** Data types specify the type of data that a variable can hold. Python supports various data types including primitive and composite data types.

### Primitive Data Types

**Primitive Data Types:** Basic data types built into the language.

**Example:**

```python
# Integer
int_var = 42

# Float
float_var = 3.14

# Boolean
bool_var = True

# None
none_var = None

print("Integer:", int_var)
print("Float:", float_var)
print("Boolean:", bool_var)
print("None:", none_var)
```

### Numeric Data Types

**Numeric Data Types:** These include integers and floating-point numbers.

**Example:**

```python
# Integer
int_num = 5

# Floating-point
float_num = 5.99

print("Integer Number:", int_num)
print("Floating-point Number:", float_num)
```

### Mathematical Expressions

**Definition:** Expressions that perform mathematical operations.

**Example:**

```python
# Arithmetic operations
a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
integer_division = a // b
modulo = a % b
exponentiation = a ** b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Integer Division:", integer_division)
print("Modulo:", modulo)
print("Exponentiation:", exponentiation)
```

### Numeric Data Type Conversion

**Definition:** Converting one numeric data type to another.

**Example:**

```python
# Integer to float
int_var = 10
float_var = float(int_var)
print("Converted to Float:", float_var)

# Float to integer
float_var = 3.99
int_var = int(float_var)
print("Converted to Integer:", int_var)
```

### Formatting Output

**Definition:** Formatting output allows you to control the appearance of output data.

**Example:**

```python
# Formatting numbers
num = 123.456789

# Displaying with 2 decimal places
print("Formatted Number (2 decimal places): {:.2f}".format(num))

# Displaying with 5 decimal places
print("Formatted Number (5 decimal places): {:.5f}".format(num))

# Formatting with width and alignment
print("Formatted Number (Width 10, right-aligned): {:>10.2f}".format(num))
print("Formatted Number (Width 10, left-aligned): {:<10.2f}".format(num))
print("Formatted Number (Width 10, centered): {:^10.2f}".format(num))
```
