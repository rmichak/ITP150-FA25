# Using and Creating Modules

## 🧠 Learning Objectives

1. Explain what modules are and why they’re useful.  
2. Import and use built-in Python modules.  
3. Create and use custom modules.  
4. Explain the purpose of `__name__ == "__main__"`.  
5. Understand nested modules and how to use `__init__.py`.  
6. Use `pip` to install and remove external modules.  

---

## 🕒 Lesson Outline

### **1. Introduction to Modules **

**Lecture/Discussion**
- Why organize code? (Maintainability, reusability, collaboration)
- Define **module**: a `.py` file containing reusable code.
- Compare modules to toolboxes: import only what you need.

**Demo:**
```python
import math
print(math.sqrt(25))
```

---

### **2. Importing Modules **

**Explain different import styles:**

| Type | Example | Description |
|------|----------|-------------|
| Basic import | `import math` | Access everything using `math.` |
| Selective import | `from math import factorial` | Import only what you need |
| Import all | `from math import *` | Bring everything in (not recommended) |
| Nested import | `import os.path` | Import from within a module |

**Demo:**
```python
from math import factorial
print(factorial(5))
```
---

### **3. Creating Your Own Modules **

- Modules are just Python files (`.py`).
- Code at top level runs **automatically** on import—so use functions.

**Demo:**
1️⃣ Create a file **`greetings.py`**
```python
\"\"\"Module for greeting users.\"\"\"

def say_hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("This runs only when greetings.py is executed directly.")
```

2️⃣ Create another file **`main.py`**
```python
import greetings
print(greetings.say_hello("Alice"))
```
---

### **4. Understanding `__name__ == "__main__"` **

- Every Python file has a built-in variable `__name__`.
- When run directly: `__name__ == "__main__"`.
- When imported: `__name__` is set to the module’s name.

**This check is called the *main guard* or *if-main idiom*.**

**Example:**
```python
def main():
    print("Running main program.")

if __name__ == "__main__":  # main guard
    main()
```

**Benefits:**
- Prevents unwanted code from running on import.
- Makes files both executable and importable.

---

### **5. Understanding `__init__.py` **

- Marks a folder as a **package**.
- Lets you import modules from that folder.
- Can be empty or contain initialization code.

**Example Folder Structure:**
```
my_package/
├── __init__.py
├── module1.py
└── module2.py
```

**Example `__init__.py`:**
```python
from .module1 import greet

# Optional initialization
print("Initializing my_package...")
```

**Now you can do:**
```python
import my_package
my_package.greet("Alice")
```

**Relative Imports:**
| Syntax | Meaning |
|--------|----------|
| `.` | Same folder |
| `..` | One folder up |
| `...` | Two folders up |

**Example:**
```python
# Inside module2.py
from .module1 import helper_function
```

---

### **6. Dunder Names Explained **

| Term | Name | Meaning |
|------|------|----------|
| `__init__.py` | “dunder init” / *package initializer* | Defines package behavior |
| `if __name__ == "__main__":` | “dunder main” / *main guard* | Runs code only if file executed directly |

> “Dunder” = *double underscore* (e.g., `__init__`, `__name__`).

---

### **7. Using External Modules and `pip` **

**Explain:**
- Some modules must be installed using `pip`.
- `pip` manages dependencies automatically.

**Commands:**
```bash
python -m pip install requests
python -m pip uninstall requests
```

**Demo:**
```bash
python -m pip install pyfiglet
```
Then in Python:
```python
import pyfiglet
print(pyfiglet.figlet_format("Modules!"))
```

---

