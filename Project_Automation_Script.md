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

Here’s a solution with a step-by-step explanation for each part of the problem.

### Solution Code:

```python
import os
import subprocess
import datetime
import psutil  # Make sure to install psutil via `pip install psutil`

def create_audit_directory():
    # Create the `system_audit` directory if it doesn't exist
    if not os.path.exists('/tmp/system_audit'):
        os.makedirs('/tmp/system_audit')
    # Create `audit_log.txt` file within this directory
    with open('/tmp/system_audit/audit_log.txt', 'w') as f:
        f.write("")

def log_audit_summary():
    # Log audit date and total files in `/home` directory
    audit_log = '/tmp/system_audit/audit_log.txt'
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_files = sum(len(files) for _, _, files in os.walk('/home'))
    with open(audit_log, 'a') as f:
        f.write(f"Audit Date: {current_time}\n")
        f.write(f"Total files in /home: {total_files}\n")

def check_and_install_curl():
    # Check if `curl` is installed and install if not
    audit_log = '/tmp/system_audit/audit_log.txt'
    try:
        subprocess.run(['curl', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with open(audit_log, 'a') as f:
            f.write("curl is already installed.\n")
    except subprocess.CalledProcessError:
        # If `curl` isn't installed, install it
        try:
            subprocess.run(['sudo', 'apt', 'install', '-y', 'curl'], check=True)
            with open(audit_log, 'a') as f:
                f.write("curl installed successfully.\n")
        except Exception as e:
            with open(audit_log, 'a') as f:
                f.write(f"Error installing curl: {str(e)}\n")

def list_high_memory_processes():
    # List processes with memory usage above 50MB
    audit_log = '/tmp/system_audit/audit_log.txt'
    with open(audit_log, 'a') as f:
        for process in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                if process.info['memory_info'].rss > 50 * 1024 * 1024:  # Convert MB to Bytes
                    f.write(f"Process {process.info['pid']} - {process.info['name']} - Memory: {process.info['memory_info'].rss // (1024 * 1024)}MB\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

def check_or_create_user():
    # Check if user `analyst` exists, if not create it
    audit_log = '/tmp/system_audit/audit_log.txt'
    try:
        result = subprocess.run(['id', 'analyst'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            with open(audit_log, 'a') as f:
                f.write("User analyst exists.\n")
        else:
            # Create the user `analyst`
            subprocess.run(['sudo', 'useradd', '-m', 'analyst'], check=True)
            with open(audit_log, 'a') as f:
                f.write("User analyst created successfully.\n")
    except Exception as e:
        with open(audit_log, 'a') as f:
            f.write(f"Error managing user analyst: {str(e)}\n")

def set_permissions():
    # Set file permissions for `audit_log.txt`
    audit_log = '/tmp/system_audit/audit_log.txt'
    os.chmod(audit_log, 0o600)  # rw------- for the owner only
    with open(audit_log, 'a') as f:
        f.write("Permissions set: rw-------\n")

def main():
    create_audit_directory()
    log_audit_summary()
    check_and_install_curl()
    list_high_memory_processes()
    check_or_create_user()
    set_permissions()
    print("System audit complete. See audit_log.txt for details.")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Creating the Audit Directory and Log File:**
   - The `create_audit_directory()` function checks if the directory `/tmp/system_audit` exists. If not, it creates it.
   - An empty file `audit_log.txt` is created (or overwritten if it exists).

2. **Logging the Audit Summary:**
   - `log_audit_summary()` writes the current date and time to `audit_log.txt`.
   - It then counts all files in the `/home` directory using `os.walk` and logs the total count.

3. **Checking and Installing `curl`:**
   - `check_and_install_curl()` uses `subprocess.run()` to check if `curl` is installed by running `curl --version`.
   - If `curl` is not installed, it attempts to install it via `apt install`.
   - Both success and error messages are logged.

4. **Listing High-Memory Processes:**
   - `list_high_memory_processes()` uses the `psutil` library to iterate over all processes.
   - It checks if any process is using more than 50MB of memory. If so, it logs the process’s PID, name, and memory usage.

5. **Checking or Creating a User:**
   - `check_or_create_user()` runs `id analyst` to check if the user `analyst` exists.
   - If the user does not exist, it attempts to create it with `useradd`.

6. **Setting File Permissions:**
   - `set_permissions()` changes `audit_log.txt` to have `rw-------` permissions (read and write for the owner only).
   - It then logs the permission status.

7. **Main Function:**
   - The `main()` function calls all the helper functions in sequence and outputs a success message when the audit is complete. 
