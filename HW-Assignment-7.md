# 🧠 HW-Assignment-7: Cybersecurity Programming Basics

## 🧩 Functions

### Problem 1: Hashing a Password
Write a function `hash_password(password)` that takes a string `password` and returns its SHA-256 hash using Python’s built-in `hashlib` module.

**Hint:**  
```python
import hashlib
hashlib.sha256(password.encode()).hexdigest()
```

**Test Cases:**
1. `hash_password("password123")` → should return a 64-character hex string.
2. Verify that calling it twice with the same password gives the same hash.

---

### Problem 2: Check for Weak Passwords
Write a function `is_weak_password(password)` that takes a password string and checks if it’s weak.  
A password is considered **weak** if:
- It’s shorter than 8 characters, **OR**
- It doesn’t contain at least one uppercase letter, one lowercase letter, one number, and one special character.

Return `True` if the password is weak, otherwise `False`.

**Test Cases:**
1. `is_weak_password("Password123!")` → `False`  
2. `is_weak_password("12345")` → `True`  
3. `is_weak_password("weakpass")` → `True`

---

## ⚠️ Exceptions and Safe Programming

### Problem 1: Safe File Access
Write a function `safe_open_file(filename)` that tries to open a file in read mode and returns its contents. Handle the following exceptions:
1. `FileNotFoundError` → return `"Error: File not found."`
2. `PermissionError` → return `"Error: Permission denied."`

**Test Cases:**
1. `safe_open_file("secret.txt")` (if file exists) → file contents  
2. `safe_open_file("nonexistent.txt")` → `"Error: File not found."`

---

### Problem 2: Validate and Parse IP Address
Write a function `validate_ip(ip_address)` that takes a string input and checks whether it’s a valid IPv4 address.

Handle these exceptions:
1. `ValueError` if the IP cannot be split into 4 parts or parts aren’t integers.
2. A custom error message if any part is not between 0 and 255.

Return:
- `"Valid IP address."` if valid  
- An appropriate error message otherwise.

**Test Cases:**
1. `validate_ip("192.168.1.1")` → `"Valid IP address."`  
2. `validate_ip("256.100.0.1")` → `"Error: Each part must be between 0 and 255."`  
3. `validate_ip("abc.def.1.1")` → `"Error: IP must contain only numbers."`

---


