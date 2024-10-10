### PRACTICE: **Student Data Management System**

Please practice this problem to solve the Midterm Question:

You are tasked with creating a Python program that manages student records. The program should:

1. **Store student information** (such as name, age, and grades) in a file using a dictionary where the key is the student's name, and the value is another dictionary containing the student's age and list of grades.
2. **Allow the user to perform the following operations**:
   - Add a new student.
   - Update an existing student's grades.
   - Display the details of a student.
   - Calculate and display the average grade of all students.
   - Save the updated student data to a file.
3. **Handle errors using try-except**, such as file reading errors or invalid inputs.
4. **Create and import a module** for file operations (such as reading from and writing to the file).

### Problem Requirements:

#### Program Structure:

1. **File Operations**:
   - Use file operations to store and retrieve student data in a text file (`students.txt`).
   - The file should be opened and closed properly, and data should be read/written in a structured format (JSON-like format is acceptable).

2. **Data Structures**:
   - **Dictionary**: Store student data as a dictionary where each key is a student's name, and the value is another dictionary containing the student's age and a **list** of grades.
   - **List**: Store student grades in a list.

3. **Logic**:
   - Use **if-else-if** conditions to handle user inputs.
   - Use **for loops** to process student data and calculate the average grade of all students.

4. **Functions**:
   - Create functions for each task, such as adding a student, updating grades, calculating averages, and saving data to a file.

5. **Try-Except**:
   - Handle potential errors, such as missing files or invalid user inputs (e.g., entering non-numeric grades).

6. **Module Creation**:
   - Create a Python module named `file_ops.py` that contains functions for reading from and writing to the file.

### Task Breakdown:

1. **Module File (`file_ops.py`)**:
   - Write two functions:
     - `read_student_data(file_path)`: Reads student data from a file and returns it as a dictionary.
     - `write_student_data(file_path, data)`: Writes updated student data to the file.

   ```python
   import json

   def read_student_data(file_path):
       try:
           with open(file_path, 'r') as file:
               return json.load(file)
       except FileNotFoundError:
           print("File not found, creating a new one.")
           return {}
       except json.JSONDecodeError:
           print("Error reading file, initializing empty data.")
           return {}

   def write_student_data(file_path, data):
       with open(file_path, 'w') as file:
           json.dump(data, file, indent=4)
   ```

2. **Main Program (`student_manager.py`)**:

   ```python
   import file_ops

   FILE_PATH = 'students.txt'

   # Function to add a new student
   def add_student(students):
       name = input("Enter student's name: ")
       if name in students:
           print(f"Student {name} already exists.")
           return
       age = int(input(f"Enter {name}'s age: "))
       grades = list(map(int, input(f"Enter {name}'s grades separated by spaces: ").split()))
       students[name] = {"age": age, "grades": grades}

   # Function to update grades for an existing student
   def update_grades(students):
       name = input("Enter student's name: ")
       if name not in students:
           print(f"Student {name} does not exist.")
           return
       new_grades = list(map(int, input(f"Enter new grades for {name} separated by spaces: ").split()))
       students[name]["grades"].extend(new_grades)

   # Function to display a student's details
   def display_student(students):
       name = input("Enter student's name: ")
       if name in students:
           print(f"Student: {name}, Age: {students[name]['age']}, Grades: {students[name]['grades']}")
       else:
           print(f"Student {name} not found.")

   # Function to calculate and display the average grade of all students
   def calculate_average(students):
       total_grades = 0
       total_count = 0
       for student in students.values():
           total_grades += sum(student["grades"])
           total_count += len(student["grades"])
       if total_count == 0:
           print("No grades available to calculate average.")
       else:
           print(f"Average grade of all students: {total_grades / total_count:.2f}")

   def main():
       students = file_ops.read_student_data(FILE_PATH)
       while True:
           print("\nMenu:")
           print("1. Add Student")
           print("2. Update Grades")
           print("3. Display Student Details")
           print("4. Calculate Average Grade")
           print("5. Save and Exit")
           choice = input("Enter your choice: ")
           
           if choice == '1':
               add_student(students)
           elif choice == '2':
               update_grades(students)
           elif choice == '3':
               display_student(students)
           elif choice == '4':
               calculate_average(students)
           elif choice == '5':
               file_ops.write_student_data(FILE_PATH, students)
               print("Data saved. Exiting...")
               break
           else:
               print("Invalid choice, please try again.")

   if __name__ == '__main__':
       main()
   ```

### Expected Functionality:

- **Add a student**: User inputs a student’s name, age, and grades.
- **Update grades**: Allows the user to add new grades for an existing student.
- **Display a student's details**: The user can search for a student by name and view their details.
- **Calculate the average grade**: The program calculates and displays the average grade for all students.
- **File operations**: Data is saved to `students.txt`, and the program reads from the file when it starts.
