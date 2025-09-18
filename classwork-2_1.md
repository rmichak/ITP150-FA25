# Module 4: Python Tools, REPL, and Libraries

---

## 1. The Python REPL

**Definition:**  
The REPL (Read–Eval–Print Loop) is an interactive environment where Python code can be typed and executed immediately. It reads your input, evaluates it, prints the result, and then loops back to wait for the next command.

**How to start it:**  
Open a terminal or command prompt and type:

```bash
python
```

You’ll see something like:

```
Python 3.11.6 (main, Sep  1 2023, 12:00:00)
>>>
```

Now you’re inside the Python REPL.

**Example:**

```python
>>> 2 + 3
5
>>> print("Hello, World!")
Hello, World!
```

**Why it’s useful:**

- Great for testing small code snippets.
- Perfect for beginners to experiment.
- Fast feedback without creating files.

---

## 2. Google Colab (Interactive Notebooks)

**Definition:**  
Google Colab is an interactive environment similar to Jupyter Notebooks, but runs entirely in the cloud. You can write and run Python code in "cells," mixing it with explanations, images, and visualizations.

**How to run it:**  
Visit: [https://colab.research.google.com](https://colab.research.google.com) and start a new notebook.

**Features:**

- Code cells: run Python code.
- Markdown cells: add formatted text, headings, and explanations.
- Visualizations: integrate with libraries like `matplotlib` or `pandas`.
- Cloud execution: no need to install Python locally.

---

### Google Colab Demo

#### Text Cell (Markdown)

```
# Welcome to Google Colab!

This is an interactive environment to write and run Python code.
You can mix **text (Markdown)** with **code** to build rich notebooks.
```

#### Code Cell 1 – Hello World

```python
# First Python program in Google Colab
print("Hello, Google Colab!")
```

#### Code Cell 2 – Using Libraries

```python
# Import and use the math library
import math

print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)
```

#### Text Cell (Markdown)

```
### External Libraries
Colab comes with many libraries pre-installed, but you can also install new ones directly with **pip**.
```

#### Code Cell 3 – Installing a Library

```python
# Install the 'requests' library
!pip install requests
```

#### Code Cell 4 – Using an External Library

```python
import requests

response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
print("First 200 characters of response:")
print(response.text[:200])
```

#### Code Cell 5 – Cybersecurity Sneak Peek (Hashing)

```python
import hashlib

password = "mypassword123"
hashed = hashlib.sha256(password.encode()).hexdigest()

print("Original password:", password)
print("SHA-256 hash:", hashed)
```

---

## 3. The `sys` Library

**Definition:**  
The `sys` module gives access to system-specific parameters and functions used by Python.

**Examples:**

```python
import sys

# Python version
print("Python version:", sys.version)

# Command-line arguments
print("Script name:", sys.argv[0])
```

If you ran the script like this:

```bash
python myscript.py hello world
```

Output:

```
Script name: myscript.py
['myscript.py', 'hello', 'world']
```

**Other Useful Functions:**

```python
# Exit the program
sys.exit()

# Maximum integer size
print("Max integer:", sys.maxsize)

# Default encoding
print("Encoding:", sys.getdefaultencoding())
```

---

## 4. Other Standard Libraries

Python comes with many built-in libraries you can use right away.

**Examples:**

```python
import math

print("Square root of 16:", math.sqrt(16))
print("Pi:", math.pi)

import datetime

now = datetime.datetime.now()
print("Current time:", now)
```

**Activity Idea:**  
Ask students to explore the `math` or `datetime` library and print one interesting function they find.

---

## 5. External Libraries & Package Managers

Python’s power comes from its ecosystem of external libraries.

### Installing Libraries with `pip`

**Definition:**  
`pip` is Python’s package manager. It allows you to install libraries from the Python Package Index (PyPI).

**Example:**

```bash
pip install requests
```

**Usage Example:**

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

---

### What is PyPI?

**Definition:**  
PyPI (Python Package Index) is an online repository of Python packages you can install with `pip`. It contains hundreds of thousands of libraries for tasks like data science, web development, and cybersecurity.

**Example Libraries on PyPI:**

- `numpy` – numerical computations.
- `pandas` – data analysis.
- `flask` – web applications.
- `cryptography` – security and encryption.

---

## 6. Preview: Python and Cybersecurity

**Bridge to next lectures:**  
While today we focused on the environment and libraries, in cybersecurity we will often use Python libraries like:

- `hashlib` (for hashing passwords).
- `socket` (for networking).
- `cryptography` (for encryption).

**Example Sneak Peek:**

```python
import hashlib

# Simple password hashing
password = "mypassword123"
hashed = hashlib.sha256(password.encode()).hexdigest()

print("SHA-256 hash:", hashed)
```

---

## Practice Prompts

1. Start the Python REPL and try a few calculations.
2. Create a Google Colab Notebook with one code cell and one Markdown cell.
3. Use the `sys` library to print your Python version.
4. Install a new package with `pip` (for example `requests`) and use it to fetch a webpage.
5. (Challenge) Use `hashlib` to hash two different passwords and compare their results.

---

## Timing Breakdown (Approx. 1 hour)

- **Intro to REPL:** 10 minutes (demo + short exercise)
- **Google Colab:** 15 minutes (demo + mini exercise)
- **`sys` and built-in libraries:** 15 minutes (examples + student activity)
- **PyPI and `pip`:** 10 minutes (explanation + install demo)
- **Cybersecurity preview:** 10 minutes (hashing demo + discussion)
