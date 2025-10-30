# Lesson Plan: Python File Operations for Cybersecurity

## Course Context

This module introduces students to Python’s file-handling capabilities.  
The focus is on developing safe, efficient, and security-conscious habits when working with files and directories.  
Students will gain hands-on experience handling text and binary files, reading and writing data, parsing structured information, and automating file-based tasks.

---

## Learning Objectives

By the end of this module, students will be able to:

1. Explain the difference between text and binary files.
2. Understand absolute and relative paths.
3. Use the `os` module to navigate, inspect, and manipulate files and directories.
4. Open, read, write, and close files safely in Python.
5. Handle exceptions related to file operations.
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
3. Working with Binary Files  
4. Reading Text Files  
5. Writing and Appending Text Files  
6. Parsing CSV Data  
7. Integration Mini-Project: Security Log Analyzer  
8. Discussion and Reflection  

---

## 1. Introduction to Files and Paths

### Key Concepts
- Files and directories
- Absolute vs. relative paths
- Escape sequences in paths
- File naming conventions

### Example
```python
import os

print("Current working directory:", os.getcwd())
path = os.path.join("file_lab", "log_sample.txt")
print("Relative path:", path)
print("Absolute path:", os.path.abspath(path))
```

### Discussion
In cybersecurity, analysts often work with nested directories containing logs, evidence, and artifacts.  
Understanding file paths ensures accurate and safe access to data.

---

## 2. Working with the `os` Module

### Objectives
- Navigate directories
- Check file existence and type
- List, filter, and delete files
- Retrieve file properties

### 2.1 Listing Files
```python
import os

for name in os.listdir("file_lab"):
    print(name)
```

### 2.2 Checking File Properties
```python
import os

path = os.path.join("file_lab", "malware_sample.bin")
print("Exists:", os.path.exists(path))
print("Is file:", os.path.isfile(path))
print("Is directory:", os.path.isdir(path))
```

### 2.3 Filtering Files by Type
```python
import os

txt_files = [f for f in os.listdir("file_lab") if f.endswith(".txt")]
print(txt_files)
```

### 2.4 Removing Temporary Files
```python
import os

for file in os.listdir("file_lab"):
    if file.endswith(".tmp"):
        os.remove(os.path.join("file_lab", file))
        print("Removed temp file:", file)
```

### 2.5 File Sizes
```python
import os

for file in os.listdir("file_lab"):
    full_path = os.path.join("file_lab", file)
    if os.path.isfile(full_path):
        size = os.path.getsize(full_path)
        print(f"{file}: {size} bytes")
```

### Discussion
Cybersecurity analysts use `os` functions to audit directories, identify suspicious files, or clean up unwanted artifacts safely.  
Being able to traverse and validate the file system programmatically is essential for automation and evidence management.

---

## 3. Working with Binary Files

### Key Concepts
- Text vs. binary representation
- Binary file modes (`'rb'`, `'wb'`, `'ab'`)
- Reading, writing, and copying binary data
- Hex representation and file signatures
- Hashing for file integrity

### 3.1 Reading Binary Files
```python
with open("file_lab/malware_sample.bin", "rb") as f:
    data = f.read(32)
    print("Byte data:", data)
    print("Hex:", data.hex())
```

### 3.2 Writing Binary Files
```python
with open("file_lab/malware_sample.bin", "rb") as src, open("file_lab/sample_copy.bin", "wb") as dst:
    dst.write(src.read(64))
```

### 3.3 Reading in Chunks
```python
with open("file_lab/malware_sample.bin", "rb") as f:
    while True:
        chunk = f.read(16)
        if not chunk:
            break
        print(chunk.hex())
```

### 3.4 File Signature Example
```python
with open("file_lab/malware_sample.bin", "rb") as f:
    header = f.read(4)
    print("Header bytes:", header.hex())

if header.startswith(b"MZ"):
    print("Windows Executable")
elif header.startswith(b"PK"):
    print("ZIP or JAR Archive")
else:
    print("Unknown or custom format")
```

### 3.5 Hashing a Binary File
```python
import hashlib

with open("file_lab/malware_sample.bin", "rb") as f:
    data = f.read()
    md5_hash = hashlib.md5(data).hexdigest()
    print("MD5:", md5_hash)
```

### Discussion
Binary files are central to cybersecurity analysis.  
Students learn to handle potentially malicious binaries safely using read-only operations and hashing to confirm data integrity.

---

## 4. Reading Text Files

### 4.1 Read Entire File
```python
with open("file_lab/log_sample.txt", "r") as f:
    contents = f.read()
    print(contents)
```

### 4.2 Read Line by Line
```python
with open("file_lab/log_sample.txt", "r") as f:
    for line in f:
        if "FAILED" in line:
            print("Suspicious login:", line.strip())
```

### 4.3 Read Specific Characters
```python
with open("file_lab/log_sample.txt", "r") as f:
    chars = f.read(10)
    print(chars)
```

### Discussion
Reading text logs allows analysts to parse and identify attack indicators or anomalies.  
Sequential reading ensures data integrity and efficient processing.

---

## 5. Writing and Appending Text Files

### 5.1 Writing to a New File
```python
with open("file_lab/alerts.txt", "w") as f:
    f.write("Brute-force attempt detected\n")
    f.write("Suspicious IP connection\n")
```

### 5.2 Appending Data
```python
with open("file_lab/alerts.txt", "a") as f:
    f.write("Added on 2025-10-30\n")
```

### 5.3 Using Context Manager
```python
with open("file_lab/notes.txt", "r") as f:
    print(f.read())
```

### Discussion
Writing and appending data is key for logging and incident documentation.  
Using `'a'` ensures analysts do not accidentally overwrite important records.

---

## 6. Parsing CSV Data

### 6.1 Reading and Filtering
```python
with open("file_lab/threat_data.csv", "r") as f:
    next(f)
    for line in f:
        ip, threat, confidence = line.strip().split(",")
        if int(confidence) > 80:
            print(f"High confidence threat: {ip} ({threat})")
```

### 6.2 Writing Filtered Results
```python
with open("file_lab/threat_data.csv", "r") as infile, open("file_lab/high_confidence.csv", "w") as outfile:
    next(infile)
    for line in infile:
        ip, threat, confidence = line.strip().split(",")
        if int(confidence) > 80:
            outfile.write(f"{ip},{threat},{confidence}\n")
```

### Discussion
Many cybersecurity tools output CSV data.  
This section introduces simple parsing and filtering logic to analyze threat feeds or system reports.

---

## 7. Integration Mini-Project: Security Log Analyzer

### Project Description
Students build a Python script that reads from `security_log.txt`, detects intrusion events, and writes a summary report.

### Example Implementation
```python
with open("file_lab/security_log.txt", "r") as infile, open("file_lab/security_summary.txt", "w") as outfile:
    failed_count = 0
    for line in infile:
        if "FAILED" in line:
            failed_count += 1
        if "SCAN" in line:
            outfile.write("Intrusion Detected: " + line)
    outfile.write(f"\nTotal failed logins: {failed_count}\n")
```

### Expected Output
```
Intrusion Detected: 172.16.0.3 PORT SCAN DETECTED
Total failed logins: 1
```

### Discussion
This project ties together all previous topics: file reading, writing, conditions, iteration, and safe handling practices.

---

## 8. Discussion and Reflection

### Key Questions
1. What is the difference between text and binary file handling?
2. Why is `with open()` preferred over manually closing files?
3. How can mishandling files create cybersecurity risks?
4. Why should analysts avoid overwriting logs or evidence?
5. How could file metadata (timestamps, sizes, hashes) be used in investigations?

### Summary of Learning
- Students understand file systems and paths.
- Students can read, write, and process both text and binary data.
- Students can use the `os` module to navigate and manage files.
- Students can apply file-handling principles to real cybersecurity tasks.

---

## Assessment Ideas

1. Hands-On Quiz:  
   Write a script that reads all `.txt` files in `file_lab` and counts total lines containing the word “FAILED”.

2. Practical Task:  
   Modify the log analyzer to generate separate reports for different alert types (login, scan, malware).

3. Reflection Essay:  
   Explain how Python’s file handling can assist in automating forensic evidence collection or malware analysis.

---

## Files Summary

| File | Purpose |
|------|----------|
| log_sample.txt | Log reading and pattern detection |
| notes.txt | Writing and appending text |
| alerts.txt | Output file for incident alerts |
| threat_data.csv | CSV parsing and filtering |
| high_confidence.csv | Filtered CSV output |
| malware_sample.bin | Binary read/write practice |
| sample_copy.bin | Output from binary exercises |
| security_log.txt | Input for log analyzer project |
| security_summary.txt | Final project output |
| temp_file.tmp | Used for cleanup with os module |

---

## Instructor Notes

- Run `setup_file_lab.py` before class to confirm file creation.
- Encourage students to explore file contents directly in VS Code to observe changes.
- Remind students to always handle unknown binary files in read-only mode.
- Relate exercises to real-world security workflows such as intrusion detection, malware triage, and evidence documentation.

---
