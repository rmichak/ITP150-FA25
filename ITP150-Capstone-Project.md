### ITP150 Capstone Project: Student Management System

#### Project Overview
Develop a Student Management System that allows for managing student records, including adding, removing, updating, and viewing student information. The system will use various Python concepts, including basic OOP, functions, conditionals, loops, and data structures like strings, lists, and dictionaries.

#### Below are the attributes and methods you will need for creating the classes

1. **Class: Student**
   - Attributes: student_id, name, age, grades (a dictionary of subjects and their corresponding grades)
   - Methods: 
     - `__init__(self, student_id, name, age)`
     - `add_grade(self, subject, grade)`
     - `remove_grade(self, subject)`
     - `update_grade(self, subject, grade)`
     - `get_average_grade(self)`

2. **Class: StudentManagementSystem**
   - Attributes: students (a dictionary with student_id as key and Student objects as values)
   - Methods:
     - `__init__(self)`
     - `add_student(self, student_id, name, age)`
     - `remove_student(self, student_id)`
     - `update_student(self, student_id, name=None, age=None)`
     - `add_grade_to_student(self, student_id, subject, grade)`
     - `remove_grade_from_student(self, student_id, subject)`
     - `update_grade_for_student(self, student_id, subject, grade)`
     - `get_student_average_grade(self, student_id)`
     - `display_student(self, student_id)`
     - `display_all_students(self)`

### Breakdown of Steps for the Student Management System Project

#### Step 1: Implement the Student Class (30 points)

1. **Define the Student Class and Initialization Method** (10 points):
   - Write the `Student` class and the `__init__` method to initialize student attributes.

2. **Add Methods to Manage Grades** (10 points):
   - Write methods to add, remove, and update grades.

3. **Calculate Average Grade** (10 points):
   - Write a method to calculate the average grade.

#### Step 2: Define the StudentManagementSystem Class (30 points)
1. **Create a StudentManagementSystem Class** (10 points):
   - This class will manage multiple students using a dictionary where each student's ID is the key and the Student object is the value.

2. **Initialize the System** (10 points):
   - Write an `__init__` method to initialize an empty dictionary to store students.

3. **Add Methods to Manage Students** (10 points):
   - Write methods to add, remove, and update student details (ID, name, age).
   - Write methods to add, remove, and update grades for a specific student.
   - Write a method to get the average grade of a specific student.
   - Write methods to display the information of a specific student and all students.

#### Step 3: Implement the Student Class (30 points)
1. **Define the Student Class and Initialization Method** (10 points):
   - Write the `Student` class and the `__init__` method to initialize student attributes.

2. **Add Methods to Manage Grades** (10 points):
   - Write methods to add, remove, and update grades.

3. **Calculate Average Grade** (10 points):
   - Write a method to calculate the average grade.

#### Step 4: Implement the StudentManagementSystem Class (50 points)
1. **Define the StudentManagementSystem Class and Initialization Method** (10 points):
   - Write the `StudentManagementSystem` class and the `__init__` method to initialize the student dictionary.

2. **Add Methods to Manage Students** (10 points):
   - Write methods to add, remove, and update student details.

3. **Add Methods to Manage Grades for Students** (10 points):
   - Write methods to add, remove, and update grades for a specific student.

4. **Calculate and Display Average Grade** (10 points):
   - Write a method to calculate and display the average grade for a specific student.

5. **Display Student Information** (10 points):
   - Write methods to display the information of a specific student and all students.




