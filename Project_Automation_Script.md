### Project: Automation Script for Cybersecurity Analysts

As a cybersecurity analyst, you often need to automate system checks and maintenance tasks. Write a Python script that performs the following tasks on a Linux system. Ensure each function is modular so it can be reused independently.

#### Task Requirements:

1. **File and Folder Management**  
   - Create a directory named `system_audit` in the `/tmp` folder if it does not exist.
   - Within the `system_audit` directory, create a file named `audit_log.txt`.
   - Write a summary log into `audit_log.txt` containing:
     - The date and time of audit (use Python’s `datetime` module).
     - The total number of files and directories in the `/home` directory.

2. **Package Management**  
   - Check if the package `curl` is installed.
     - If it is installed, log `"curl is already installed."` in `audit_log.txt`.
     - If it is not installed, install `curl` using the `subprocess` module, then log `"curl installed successfully."` in `audit_log.txt`.

3. **Process Management**  
   - Use the `psutil` library to:
     - List all active processes that have a memory usage higher than 50MB.
     - Log each of these processes in `audit_log.txt` with its PID, name, and memory usage.
   - Hint: You can use `psutil.Process().memory_info().rss` to get memory usage.

4. **User Management**  
   - Check if a user named `analyst` exists on the system.
     - If the user exists, log `"User analyst exists."` in `audit_log.txt`.
     - If the user does not exist, create the user and log `"User analyst created successfully."` in `audit_log.txt`.

5. **Permissions Check**  
   - Ensure the `audit_log.txt` file has read and write permissions for the owner, but no permissions for others.
   - Log the permission status in `audit_log.txt` as `"Permissions set: rw-------"`.

6. **Summary Execution**  
   - After executing all tasks, print a success message in the console: `"System audit complete. See audit_log.txt for details."`

#### Constraints:

- Use only standard libraries for most of the tasks, but you may need to install `psutil` for process management. Include a comment at the top of your script explaining how to install it (`pip install psutil`).
- Use appropriate exception handling to ensure each task logs any errors in `audit_log.txt`.

#### Example Output in `audit_log.txt`:

```
Audit Date: 2024-10-31 15:22:10
Total files in /home: 120
curl is already installed.
Process 1234 - nginx - Memory: 75MB
Process 5678 - python - Memory: 100MB
User analyst exists.
Permissions set: rw-------
```

#### Hints:

- Use `subprocess` for executing Linux commands for package and user management.
- Use `os` and `shutil` for file and directory management.
- Use `psutil` for process management.
- To check and modify permissions, use `os.chmod`.
