## Module 5: Repetition Control Structures

Welcome to this Python tutorial focused on repetition control structures, including count-controlled loops, counters and accumulators, nested loops, and pre-test loops. This tutorial will cover the concepts and practical implementations of these loops in Python.

### 1. Count-Controlled Loops

**Definition:** A count-controlled loop repeats a specified number of times.

**Structure of a Count-Controlled Loop:**
- **Loop counter:** Tracks the number of iterations.
- **Iterative sequence:** Defines the values the loop counter will take, often using the `range()` function.

**Syntax:**
```python
for i in range(start, end, step):
    # Code block to be repeated
```

**Examples:**

- Simple loop from 0 to 9:
    ```python
    for i in range(10):
        print(i)
    ```

- Loop with custom start and end:
    ```python
    for i in range(1, 10):
        print(i)
    ```

- Loop with step value:
    ```python
    for i in range(1, 10, 2):
        print(i)
    ```

### 2. Counters and Accumulators

**Definition:** Counters increment by a specified value in each iteration, while accumulators sum values during each iteration.

**Example of a Counter:**
```python
count_out = 0
for i in range(2, 11, 2):
    count_out += 2
    print(count_out)
```

**Example of an Accumulator:**
```python
total_weight = 0
reps = int(input("How many reps? "))
weight = int(input("What size weights are you using? "))
for i in range(reps):
    total_weight += weight * 2
    print(f"Rep {i + 1}: {total_weight} lbs so far.")
print(f"Your total lift is: {total_weight} lbs.")
```

### 3. Nested Loops

**Definition:** A loop inside another loop.

**Structure:**
- **Outer loop:** Runs a specified number of times.
- **Inner loop:** Runs for each iteration of the outer loop.

**Example:**
```python
for i in range(3):  # Outer loop
    print(f"Outer loop iteration: {i}")
    for j in range(2):  # Inner loop
        print(f"  Inner loop iteration: {j}")
```

### 4. Pre-Test Loops (While Loops)

**Definition:** A loop that executes as long as a specified condition is true.

**Syntax:**
```python
while condition:
    # Code block to be repeated
```

**Example:**
```python
reps = int(input("Enter the number of reps: "))
while reps < 1 or reps > 25:
    reps = int(input("Try again. Enter a number between 1 and 25: "))
print(f"Okay, you want to do {reps} reps.")
```

### Activities

#### Activity 1: Amusement Park Tally
Write a program to tally ride tickets for different amusement park attractions.

**Sample Code:**
```python
total_tickets = 0
attractions = ["Carousel", "Ferris Wheel", "Roller Coaster"]
for attraction in attractions:
    ride = input(f"Do you want to ride the {attraction}? (yes/no): ")
    if ride.lower() == "yes":
        tickets = int(input(f"How many tickets does {attraction} require? "))
        total_tickets += tickets
print(f"Total tickets required: {total_tickets}")
```

#### Activity 2: Pizza Toppings
Write a program to add toppings to a pizza.

**Sample Code:**
```python
toppings = []
while True:
    topping = input("Enter a pizza topping (or 'done' to finish): ")
    if topping.lower() == "done":
        break
    toppings.append(topping)
    print(f"Added {topping} to the pizza.")
print(f"You added {len(toppings)} toppings to your pizza.")
```
