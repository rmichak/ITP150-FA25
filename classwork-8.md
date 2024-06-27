### Module 8 : Modules and File Operations

### Table of Contents
1. [Introduction to Modules](#introduction-to-modules)
2. [Importing Modules](#importing-modules)
3. [Creating Modules](#creating-modules)
4. [Using Nested Modules](#using-nested-modules)
5. [File Input and Output](#file-input-and-output)
6. [Using the `os` Module](#using-the-os-module)

---

### Introduction to Modules

#### What is a Module?
A module in Python is a file containing Python definitions and statements. Modules can help organize code by grouping related functions, classes, and variables into separate files.

#### Benefits of Using Modules
- **Reusability**: Code can be reused in multiple programs.
- **Simplicity**: Easier to manage and understand smaller files.
- **Maintainability**: Easier to update and maintain code.

---

### Importing Modules

Python provides several ways to import modules:

1. **Basic Import**:
   ```python
   import math
   print(math.factorial(5))  # Output: 120
   ```

2. **From Import**:
   ```python
   from math import factorial
   print(factorial(5))  # Output: 120
   ```

3. **Import All**:
   ```python
   from math import *
   print(factorial(5))  # Output: 120
   ```

4. **Nested Module Import**:
   ```python
   import os.path
   print(os.path.join('folder', 'file.txt'))
   ```

---

### Creating Modules

To create a module, you simply write Python code in a file with a `.py` extension. For example, create a file named `mymodule.py`:

```python
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"
```

Then, you can import and use this module in another Python script:

```python
# main.py

import mymodule

print(mymodule.greet('Alice'))
print(mymodule.farewell('Bob'))
```

#### Using `__name__ == "__main__"`

Include a main function to execute code only when the file is run directly:

```python
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet('World'))
```

---

### Using Nested Modules

Nested modules are organized within directories. Each directory should contain an `__init__.py` file.

```python
# mypackage/__init__.py
# mypackage/module1.py
# mypackage/module2.py
```

Example of using a nested module:

```python
# mypackage/module1.py

def foo():
    return "foo"

# main.py
from mypackage import module1

print(module1.foo())  # Output: foo
```

---

### File Input and Output

#### Reading from a File

```python
# Reading the entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

#### Writing to a File

```python
# Writing to a file (overwriting)
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")

# Appending to a file
with open('output.txt', 'a') as file:
    file.write("Append this line.\n")
```

#### Handling Exceptions

```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

### Using the `os` Module

The `os` module provides a way to use operating system dependent functionality.

#### Common `os` Module Functions

```python
import os

# Joining paths
path = os.path.join('folder', 'file.txt')
print(path)  # Output will depend on the OS, e.g., 'folder/file.txt' on Unix

# Checking if a path exists
print(os.path.exists(path))  # Output: True or False

# Listing directory contents
print(os.listdir('.'))  # Output: List of files and directories in the current directory

# Removing a file
os.remove('file_to_remove.txt')

# Removing an empty directory
os.rmdir('empty_directory')
```
