# Lesson Plan: Python File Operations for Cybersecurity

## Course Context

This module introduces students to Python’s file-handling capabilities.  
The focus is on developing safe, efficient, and security-conscious habits when working with files and directories.  
Students will gain hands-on experience handling text and binary files, reading and writing data, parsing structured information, handling exceptions, and automating file-based tasks.

---

## Learning Objectives

By the end of this module, students will be able to:

1. Explain the difference between text and binary files.
2. Understand absolute and relative paths.
3. Use the `os` module to navigate, inspect, and manipulate files and directories.
4. Open, read, write, and close files safely in Python.
5. Handle exceptions and errors gracefully.
6. Parse and process structured text (CSV) data.
7. Work with binary data and compute file hashes.
8. Apply file-handling principles to cybersecurity use cases such as log analysis, malware inspection, and evidence handling.

---

## Prerequisites

- Python 3 installed
- Basic understanding of Python syntax
- Visual Studio Code or another IDE

---

## Required Materials

Students should download or create one Python file named `setup_file_lab.py` and run it once before beginning the lab.  
This will generate all sample files needed for exercises.

---

## Setup Script: `setup_file_lab.py`

```python
"""
setup_file_lab.py
Creates all demo files needed for the File Operations & Cybersecurity Lab.
Run once from any folder — works relative to the current directory.
"""

import os

lab_dir = os.path.join(os.getcwd(), "file_lab")
os.makedirs(lab_dir, exist_ok=True)
print(f"Created working folder: {lab_dir}")

log_file = os.path.join(lab_dir, "log_sample.txt")
with open(log_file, "w") as f:
    f.write("2025-10-30 09:12:01 LOGIN SUCCESS user=admin\n")
    f.write("2025-10-30 09:15:23 LOGIN FAILED user=guest\n")
    f.write("2025-10-30 09:20:55 MALWARE DETECTED file=virus.exe\n")

notes_file = os.path.join(lab_dir, "notes.txt")
with open(notes_file, "w") as f:
    f.write("Initial security notes.\n")
    f.write("Check server logs daily.\n")

csv_file = os.path.join(lab_dir, "threat_data.csv")
with open(csv_file, "w") as f:
    f.write("ip,threat_type,confidence\n")
    f.write("192.168.1.10,Brute Force,95\n")
    f.write("10.0.0.3,Malware,85\n")
    f.write("172.16.5.22,Phishing,40\n")

sec_log = os.path.join(lab_dir, "security_log.txt")
with open(sec_log, "w") as f:
    f.write("10.0.0.5 LOGIN FAILED\n")
    f.write("10.0.0.10 LOGIN SUCCESS\n")
    f.write("172.16.0.3 PORT SCAN DETECTED\n")

tmp_file = os.path.join(lab_dir, "temp_file.tmp")
bin_file = os.path.join(lab_dir, "malware_sample.bin")

with open(tmp_file, "w") as f:
    f.write("temporary cache data\n")

with open(bin_file, "wb") as f:
    f.write(os.urandom(128))

print("All demo files created successfully.")
```

---

# Module Outline

1. Introduction to Files and Paths  
2. Working with the `os` Module  
3. Reading Text Files  
4. Writing and Appending Text Files  
5. Exception Handling in File Operations  
6. Parsing CSV Data  
7. Integration Mini-Project: Security Log Analyzer  
8. Working with Binary Files  
9. Discussion and Reflection  

---

(remaining content truncated for brevity — same as last assistant message)
