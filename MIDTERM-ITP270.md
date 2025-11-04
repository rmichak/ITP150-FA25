# 🧩 Midterm: User Login and Password Management System

You are tasked with creating a Python program that manages user login data for a small company’s internal system.  
Your program will simulate a basic authentication management system.

---

## **Program Requirements**

### 1. Store User Data
Store **user information** (username, password, and access level) in a file using a **dictionary**, where:
- The **key** is the username.
- The **value** is another dictionary containing the user’s **password (hashed)** and **access level**.

Example:
```python
{
    "alice": {"password": "5f4dcc3b5aa765d61d8327deb882cf99", "access": "admin"}
}
```

---

### 2. User Operations
The user should be able to perform the following operations:
1. **Add a new user** (username, password, access level).  
   - Passwords should be stored as **MD5 hashes** (use the `hashlib` module).  
2. **Update a user’s password.**
3. **Display user details (except password).**
4. **Check login credentials** — prompt for username and password and verify if they match the stored hash.
5. **Display the count of users by access level** (e.g., how many admins, users, etc.).
6. **Save all updates** to a file (`users.txt`).

---

### 3. Error Handling
Use `try-except` blocks to handle:
- File not found errors.
- Invalid user input.
- Lookup errors for non-existent users.

---

### 4. File Operations Module
Create a separate module file named `file_operations.py` that contains:
- `read_user_data(file_path)` – reads user data from a file and returns it as a dictionary.  
- `write_user_data(file_path, data)` – writes updated user data to the file.

---

### 5. File Structure

- `file_operations.py` – handles reading/writing from the text file.
- `user_manager.py` – contains the main program logic.

---

### 🔐 **Hint: Using `hashlib` to Hash a Password**

You can use Python’s built-in `hashlib` module to hash a password before storing it.

Example:
```python
import hashlib

# Get a password from the user
password = input("Enter password: ")

# Create an MD5 hash of the password
hashed_password = hashlib.md5(password.encode()).hexdigest()

print("Hashed password:", hashed_password)
```

👉 **Explanation:**
- `hashlib.md5()` creates an MD5 hash object.
- `.encode()` converts the string into bytes (required by hashlib).
- `.hexdigest()` returns the hash as a readable string of hexadecimal characters.

You can use this same pattern whenever you need to hash passwords before saving them to your dictionary or file.

---

## **Grading Rubric**

| Component | Points |
|------------|---------|
| File operations (read/write) | 20 |
| Dictionary data structure | 15 |
| User operations (add, update, display, verify, count) | 25 |
| Error handling | 15 |
| Use of functions and modular design | 15 |
| Screenshots showing output/execution | 10 |
| **Total** | **100** |

---

### **Learning Objectives**
- File I/O and data persistence  
- Working with nested dictionaries  
- Exception handling  
- Hashing (basic cybersecurity principle)  
- Modular programming and function design  
