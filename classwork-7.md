### Module 7: Lists

### Objectives
1. Understand list basics.
2. Initialize and use one-dimensional lists.
3. Perform input and output operations with lists.
4. Apply list operations, functions, and methods.
5. Use list comprehensions.
6. Work with two-dimensional lists.
7. Utilize dictionaries in Python.

### 1. List Basics
A list is a data structure that stores a collection of elements in a specific order. Lists in Python can contain any combination of data types and are ordered, meaning each element is identified by its index.

#### Example
```python
# Creating a list
my_list = [1, 2, 3, "a", "b", "c"]
print(my_list)  # Output: [1, 2, 3, 'a', 'b', 'c']
```

### 2. One-Dimensional List Initialization
You can declare and initialize lists using square brackets or the `list()` function.

#### Example
```python
# Declaring an empty list
empty_list = []
empty_list = list()

# Declaring and initializing a list with values
numbers_list = [2, 6, 2, 3, 9, 12]
letters_list = ["A", "H", "C", "B"]
mixed_list = [2, 4, "B", 2, "Z"]
print(numbers_list)  # Output: [2, 6, 2, 3, 9, 12]
```

### 3. One-Dimensional List Input and Output
You can output a list element using its index and traverse the list using loops.

#### Example
```python
# Outputting a list element
numbers = [6, 7, 8, 9, 10]
print(numbers[3])  # Output: 9

# Traversing a list
for number in numbers:
    print(number)

# Inputting list elements
user_list = []
for i in range(3):
    user_input = input("Enter a number: ")
    user_list.append(user_input)
print(user_list)
```

### 4. One-Dimensional List Operations, Functions, and Methods
Lists support various operations such as changing elements, finding elements, and summing elements.

#### Example
```python
# Changing a list element
numbers = [6, 7, 8, 9, 10]
numbers[3] = 22
print(numbers)  # Output: [6, 7, 8, 22, 10]

# Finding an element
count = numbers.count(22)
print(count)  # Output: 1

# Summing elements
total = sum(numbers)
print(total)  # Output: 53
```

### 5. List Comprehension
List comprehensions provide a concise way to create lists.

#### Example
```python
# Creating a list using list comprehension
numbers = [i for i in range(100)]
print(numbers)

# Filtering with list comprehension
evens = [i for i in range(100) if i % 2 == 0]
print(evens)

# Mapping with list comprehension
doubled = [i * 2 for i in range(50)]
print(doubled)

# Combined filtering and mapping
filtered_mapped = [i * 3 for i in range(50) if i % 3 == 0]
print(filtered_mapped)
```

### 6. Two-Dimensional Lists
Two-dimensional lists can be visualized as tables with rows and columns.

#### Example
```python
# Initializing a two-dimensional list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

# Traversing a two-dimensional list
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

### 7. Dictionaries
Dictionaries store data as key-value pairs.

#### Example
```python
# Creating and using a dictionary
scores = {"mandy": 2, "fernando": 4, "jessica": 1, "prateek": 1}
print(scores["fernando"])  # Output: 4

# Adding and updating dictionary entries
scores["George"] = 0
scores["mandy"] = 3

# Removing a dictionary entry
scores.pop("George")
print(scores)
```
