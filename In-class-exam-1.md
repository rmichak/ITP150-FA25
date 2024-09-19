# In-class Exam-1

### **Problem 1: Leap Year Checker**
Write a Python program that takes a year as input and determines if it is a leap year. A year is a leap year if it is divisible by 4 but not divisible by 100 unless it is also divisible by 400.

**Input:**
- A single integer (year).

**Output:**
- Print "Leap year" if the year is a leap year, otherwise print "Not a leap year".

**Example:**
```
Input: 2020
Output: Leap year

Input: 1900
Output: Not a leap year
```

---

### **Problem 2: Simple Calculator**
Create a simple calculator that takes two numbers and a mathematical operation (addition, subtraction, multiplication, or division) as input from the user and outputs the result.

**Input:**
- Two numbers (floating-point or integers).
- A string indicating the operation: "+", "-", "*", or "/".

**Output:**
- The result of the operation. If the operation is division and the second number is zero, print "Cannot divide by zero".

**Example:**
```
Input: 8
Input: 4
Input: /
Output: 2.0

Input: 5
Input: 0
Input: /
Output: Cannot divide by zero
```

---

### **Problem 3: Age Group Identifier**
Write a Python program that asks the user to input their age and then prints the age group they belong to based on the following criteria:
- "Child" if age < 13
- "Teenager" if age >= 13 and age < 20
- "Adult" if age >= 20 and age < 60
- "Senior" if age >= 60

**Input:**
- An integer representing the user's age.

**Output:**
- Print the corresponding age group.

**Example:**
```
Input: 15
Output: Teenager

Input: 25
Output: Adult
```

---

### **Problem 4: Odd or Even and Positive or Negative**
Write a program that takes an integer as input and determines whether the number is odd or even, and whether it is positive, negative, or zero.

**Input:**
- A single integer.

**Output:**
- Print two statements: one indicating whether the number is odd or even, and another indicating whether it is positive, negative, or zero.

**Example:**
```
Input: -7
Output: Odd
Output: Negative

Input: 12
Output: Even
Output: Positive
```

---

### **Problem 5: Temperature Conversion**
Create a Python program that converts temperature from Celsius to Fahrenheit or from Fahrenheit to Celsius based on the user’s choice.

**Input:**
- A float representing the temperature.
- A string that specifies the conversion type: "C to F" (Celsius to Fahrenheit) or "F to C" (Fahrenheit to Celsius).

**Output:**
- The converted temperature, rounded to 2 decimal places.

**Formula:**
- Celsius to Fahrenheit: \( F = \frac{9}{5}C + 32 \)
- Fahrenheit to Celsius: \( C = \frac{5}{9}(F - 32) \)

**Example:**
```
Input: 100
Input: C to F
Output: 212.00

Input: 32
Input: F to C
Output: 0.00
```
