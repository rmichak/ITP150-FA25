### In-class Assignment-3: Characters and Strings

### Problem 1: Character Check
Write a Python function `is_alpha_digit` that takes a single character as input and returns a tuple with two boolean values:
1. Whether the character is an alphabet letter.
2. Whether the character is a digit.

**Example:**
```python
print(is_alpha_digit("a"))  # (True, False)
print(is_alpha_digit("1"))  # (False, True)
print(is_alpha_digit("#"))  # (False, False)
```

### Problem 2: String Length and First Character
Write a Python function `string_info` that takes a string as input and returns a tuple with two values:
1. The length of the string.
2. The first character of the string.

**Example:**
```python
print(string_info("hello"))  # (5, 'h')
print(string_info(""))  # (0, None)  # If the string is empty, return None for the first character.
```

### Problem 3: Count Vowels
Write a Python function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

**Example:**
```python
print(count_vowels("hello"))  # 2
print(count_vowels("sky"))  # 0
```
