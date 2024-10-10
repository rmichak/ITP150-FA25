### Midterm: **Employee Data Management System**

Your points will be counted based on this problem so please make sure you are following the steps properly to solve it. 

You are tasked with creating a Python program that manages employee records. The program should:

1. **Store employee information** (such as name, department, and salary) in a file using a dictionary where the key is the employee's name, and the value is another dictionary containing the employee's department and salary.
2. **Allow the user to perform the following operations**:
   - Add a new employee.
   - Update an existing employee's salary.
   - Display the details of an employee.
   - Calculate and display the average salary of all employees.
   - Save the updated employee data to a file.
3. **Handle errors using try-except**, such as file reading errors or invalid inputs.
4. **Create and import a module** for file operations (such as reading from and writing to the file).

### Problem Requirements:

#### Program Structure:

1. **File Operations**:
   - Use file operations to store and retrieve employee data in a text file (`employees.txt`).
   - The file should be opened and closed properly, and data should be read/written in a structured format (JSON-like format is acceptable).

2. **Data Structures**:
   - **Dictionary**: Store employee data as a dictionary where each key is an employee's name, and the value is another dictionary containing the employee's department and salary.
   - **List**: Used in parts where needed (e.g., calculating averages or managing employee data).

3. **Logic**:
   - Use **if-else-if** conditions to handle user inputs.
   - Use **for loops** to process employee data and calculate the average salary of all employees.

4. **Functions**:
   - Create functions for each task, such as adding an employee, updating salary, displaying employee details, and saving data to a file.

5. **Try-Except**:
   - Handle potential errors, such as missing files or invalid user inputs (e.g., entering non-numeric salaries).

6. **Module Creation**:
   - Create a Python module named `file_operations.py` that contains functions for reading from and writing to the file.

### Task Breakdown:

1. **Module File (`file_operations.py`)**:
   - Write two functions:
     - `read_employee_data(file_path)`: Reads employee data from a file and returns it as a dictionary.
     - `write_employee_data(file_path, data)`: Writes updated employee data to the file.

2. **Main Program (`employee_manager.py`)**:

### Expected Functionality:

- **Add an employee**: The user inputs the employee’s name, department, and salary.
- **Update salary**: The user can update the salary for an existing employee.
- **Display an employee's details**: The user can search for an employee by name and view their details.
- **Calculate the average salary**: The program calculates and displays the average salary of all employees.
- **File operations**: Data is saved to `employees.txt`, and the program reads from the file when it starts.
