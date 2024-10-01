### In-class-Assignment-7

#### Problem 1: Built-in and Imported Functions
Write a Python script that:
1. Uses the built-in `abs()` function to find the absolute value of -15.
2. Imports the `math` module and uses the `sqrt()` function to find the square root of 25.

#### Problem 2: Programmer-defined Function
Define a function `greet_user` that takes a user's name as an argument and prints a personalized greeting. Call the function with the name "John".

#### Problem 3: Void Function
Create a void function `display_message` that prints "This is a simple message." when called. Call this function.

#### Problem 4: Employee Salary Calculator

**Objective:**  
Write a Python program that calculates the average monthly salary for an employee based on their earnings for each month stored in a dictionary. If a month is missing, the program should handle this using an exception and print an error message for the missing month.

---

### Step-by-Step Working Process:

1. **Create a function:**  
   Define a function `calculate_average_salary()` that takes a dictionary of monthly salaries as input.

2. **Handle Exceptions:**  
   Use a `try-except` block to handle cases where a month's salary is missing or is not a number.

3. **Dictionary Input:**  
   Use a dictionary where the keys are the names of the months (e.g., "January", "February") and the values are the monthly salary amounts.

4. **Calculate Average Salary:**  
   Calculate the average by summing all the salaries and dividing by the number of months available in the dictionary.

5. **Display Result:**  
   Print the employee's name and their average monthly salary. If a month is missing or there’s an error, print an error message.

---

### Example:

**Input:**
```
Enter the employee's name: John
```

**Output:**
```
John's average monthly salary is: $3050.00
```

---
