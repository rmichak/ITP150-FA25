### Module 3: Character and String Data Types

#### Module Objectives
1. **Characters**:
   - Define character data.
   - Initialize character data.
   - Understand ASCII encoding.
   - Distinguish between digits and numbers.
   - Format character output.
   - Utilize common character manipulation methods.

2. **String Data Type**:
   - Understand string data and initialization.
   - Use escape sequences.
   - Work with string indexes.
   - Manipulate strings using built-in functions and methods.

3. **String Functions**:
   - Get string length.
   - Change string case.
   - Find characters in strings.
   - Retrieve substrings.

4. **Concatenation and Typecasting**:
   - Concatenate strings.
   - Understand typecasting between strings and other data types.

---

### 1. Working with Characters
#### What is a Character?
- A character is a single letter, digit, or symbol.
- Example: `first_letter = "a"`

#### ASCII Encoding
- ASCII assigns an 8-bit code to each character.
- Example: 
  ```python
  uppercase_A = ord("A")  # 65
  lowercase_a = ord("a")  # 97
  ```

#### Character Output Format
- Digits in a string are stored as ASCII values.
- Example:
  ```python
  a_digit = "5"  # ASCII value
  an_integer = 5  # Binary number
  ```

#### Formatting Output
- Use spaces or new lines in print statements.
  ```python
  print("A", "B", "C")  # Output: A B C
  print("A\nB\nC")  # Output on separate lines
  ```

#### Common Methods
- `isalpha()`, `isdigit()`, `upper()`, `lower()`
  ```python
  char = "a"
  print(char.isalpha())  # True
  print(char.upper())  # A
  ```

### 2. Working with Strings
#### Initializing Strings
- Strings are sequences of characters.
- Example:
  ```python
  your_name = ""
  message = "likes alphabet soup."
  ```

#### Escape Characters
- Use backslashes to include special characters.
  ```python
  print("She said, \"Hello!\"")  # She said, "Hello!"
  ```

#### String Indexes
- Access characters using indexes.
  ```python
  company_name = "Campbell's"
  letter = company_name[0]  # C
  ```

### 3. String Functions
#### Length of a String
- Use `len()` to find string length.
  ```python
  length = len("hello")  # 5
  ```

#### Changing Case
- Use `upper()` and `lower()`.
  ```python
  print("hello".upper())  # HELLO
  ```

#### Finding Characters
- Use `find()` and `count()`.
  ```python
  print("apple".find("p"))  # 1
  print("banana".count("a"))  # 3
  ```

#### Retrieving Substrings
- Use slicing to get substrings.
  ```python
  substring = "hello world"[0:5]  # hello
  ```

### 4. Concatenation and Typecasting
#### Concatenating Strings
- Use `+` to concatenate.
  ```python
  first_name = "John"
  last_name = "Doe"
  full_name = first_name + " " + last_name
  print(full_name)  # John Doe
  ```

#### Typecasting
- Convert between types using `str()` and `int()`.
  ```python
  number = 5
  str_number = str(number)
  print("The number is " + str_number)  # The number is 5
  ```

---

### Practice Exercises
1. **Character Initialization**
   ```python
   initial = "a"
   print(initial.isalpha())  # True
   print(initial.isdigit())  # False
   ```

2. **String Initialization and Manipulation**
   ```python
   your_name = input("What is your name? ")
   message = " likes Python programming."
   print(your_name + message)
   ```

3. **Concatenation and Typecasting**
   ```python
   age = input("Enter your age: ")
   age_next_year = int(age) + 1
   print("Next year, you will be " + str(age_next_year))
   ```
