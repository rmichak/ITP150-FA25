### **Kali Linux: Managing Files and Folders**

This tutorial will guide you through basic file and folder management tasks using **Bash commands** and then show how to accomplish the same tasks using Python’s `subprocess` module.

---

### **1. Creating a New File**

#### **Using Bash Commands:**

To create a new file in the terminal, you can use the `touch` command.

- **Command**:
  ```bash
  touch newfile.txt
  ```
- **Explanation**: This creates an empty file named `newfile.txt` in the current directory.

#### **Using Python with `subprocess`:**

You can achieve the same task by running the `touch` command from a Python script using the `subprocess` module.

```python
import subprocess

# Create a new file using touch command
subprocess.run(["touch", "newfile.txt"])
```

### **2. Writing Text to a File**

#### **Using Bash Commands:**

To write text to a file, you can use the `echo` command with redirection (`>`).

- **Command**:
  ```bash
  echo "Hello, World!" > newfile.txt
  ```
- **Explanation**: This writes "Hello, World!" into `newfile.txt`. The `>` symbol overwrites the file content if the file already exists.

#### **Using Python with `subprocess`:**

You can run the same `echo` command in Python using `subprocess.run()`.

```python
import subprocess

# Write text to a file using echo command
subprocess.run('echo "Hello, World!" > newfile.txt', shell=True)
```

### **3. Creating a New Directory**

#### **Using Bash Commands:**

To create a directory in the terminal, use the `mkdir` command.

- **Command**:
  ```bash
  mkdir newfolder
  ```
- **Explanation**: This creates a new directory named `newfolder` in the current directory.

#### **Using Python with `subprocess`:**

To create a directory in Python, use the `mkdir` command with `subprocess`.

```python
import subprocess

# Create a new directory using mkdir command
subprocess.run(["mkdir", "newfolder"])
```

### **4. Moving a File into a Directory**

#### **Using Bash Commands:**

To move a file to a directory, use the `mv` command.

- **Command**:
  ```bash
  mv newfile.txt newfolder/
  ```
- **Explanation**: This moves `newfile.txt` into the `newfolder` directory.

#### **Using Python with `subprocess`:**

The same operation can be done in Python using `subprocess.run()`.

```python
import subprocess

# Move a file into a directory using mv command
subprocess.run(["mv", "newfile.txt", "newfolder/"])
```

### **5. Listing the Contents of a Directory**

#### **Using Bash Commands:**

To list the contents of a directory, use the `ls` command.

- **Command**:
  ```bash
  ls newfolder
  ```
- **Explanation**: This lists the files and subdirectories inside the `newfolder` directory.

#### **Using Python with `subprocess`:**

In Python, you can list the contents of a directory using the `ls` command with `subprocess`.

```python
import subprocess

# List the contents of a directory using ls command
subprocess.run(["ls", "newfolder"])
```

### **6. Removing a File**

#### **Using Bash Commands:**

To delete a file, use the `rm` command.

- **Command**:
  ```bash
  rm newfolder/newfile.txt
  ```
- **Explanation**: This deletes `newfile.txt` from the `newfolder` directory.

#### **Using Python with `subprocess`:**

You can delete the file in Python by using the same `rm` command via `subprocess`.

```python
import subprocess

# Remove a file using rm command
subprocess.run(["rm", "newfolder/newfile.txt"])
```

### **7. Removing a Directory**

#### **Using Bash Commands:**

To delete an empty directory, use the `rmdir` command.

- **Command**:
  ```bash
  rmdir newfolder
  ```
- **Explanation**: This removes the empty `newfolder` directory.

#### **Using Python with `subprocess`:**

To remove a directory using Python, you can run the `rmdir` command via `subprocess`.

```python
import subprocess

# Remove a directory using rmdir command
subprocess.run(["rmdir", "newfolder"])
```

---

### **Summary of Tasks Covered**

| **Task**                         | **Bash Command**                       | **Python with `subprocess`**                          |
|-----------------------------------|----------------------------------------|-------------------------------------------------------|
| Create a new file                 | `touch newfile.txt`                    | `subprocess.run(["touch", "newfile.txt"])`            |
| Write text to a file              | `echo "Hello, World!" > newfile.txt`   | `subprocess.run('echo "Hello, World!" > newfile.txt', shell=True)` |
| Create a new directory            | `mkdir newfolder`                      | `subprocess.run(["mkdir", "newfolder"])`              |
| Move a file into a directory      | `mv newfile.txt newfolder/`            | `subprocess.run(["mv", "newfile.txt", "newfolder/"])` |
| List contents of a directory      | `ls newfolder`                         | `subprocess.run(["ls", "newfolder"])`                 |
| Remove a file                     | `rm newfolder/newfile.txt`             | `subprocess.run(["rm", "newfolder/newfile.txt"])`     |
| Remove a directory                | `rmdir newfolder`                      | `subprocess.run(["rmdir", "newfolder"])`              |

---

### **Kali Linux: Package Management**

This tutorial covers basic package management tasks in **Kali Linux** using the **APT (Advanced Package Tool)**. We will first demonstrate these tasks using **Bash commands**, followed by the same tasks using Python's `apt` module. 

### **What is APT?**
APT is the package management system used in Debian-based Linux distributions (like Ubuntu and Kali Linux) to install, update, remove, and manage software packages.

---

### **1. Updating Package List**

Before installing or upgrading any package, it's essential to update the local package list so that the latest version of available software can be fetched.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo apt update
  ```

- **Explanation**: This command updates the package list from the repositories, ensuring that you have the latest information on available packages.

#### **Using Python with `apt` Module:**

The `apt` module in Python provides a way to interact with APT. Here's how you can update the package list using Python:

```python
import apt

# Create an apt cache object
cache = apt.Cache()

# Update the package list
cache.update()

# Reopen the cache after the update
cache.open()
print("Package list updated successfully!")
```

---

### **2. Upgrading Installed Packages**

After updating the package list, you may want to upgrade all installed packages to their latest versions.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo apt upgrade
  ```

- **Explanation**: This command upgrades all installed packages to the newest available versions.

#### **Using Python with `apt` Module:**

You can upgrade packages using Python by iterating over the package cache and marking packages for upgrade.

```python
import apt

# Create an apt cache object
cache = apt.Cache()

# Update the cache and mark packages for upgrade
cache.update()
cache.open()

# Mark all packages for upgrade
cache.upgrade()

# Commit the changes (upgrade the packages)
cache.commit()
print("Packages upgraded successfully!")
```

---

### **3. Installing a New Package**

To install a new package, use the `apt install` command in Bash, or the equivalent Python code with the `apt` module.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo apt install nmap
  ```

- **Explanation**: This installs the `nmap` package, a popular network scanning tool, on your system.

#### **Using Python with `apt` Module:**

You can install packages using Python by marking them for installation.

```python
import apt

# Create an apt cache object
cache = apt.Cache()

# Open the cache
cache.open()

# Check if the package is available in the cache
if 'nmap' in cache:
    pkg = cache['nmap']
    if not pkg.is_installed:
        # Mark the package for installation
        pkg.mark_install()
        cache.commit()
        print("Nmap package installed successfully!")
    else:
        print("Nmap is already installed.")
else:
    print("Package 'nmap' not found.")
```

---

### **4. Removing a Package**

If you no longer need a package, you can remove it using `apt remove` in Bash or via Python.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo apt remove nmap
  ```

- **Explanation**: This removes the `nmap` package from your system, keeping its configuration files.

#### **Using Python with `apt` Module:**

To remove a package using Python:

```python
import apt

# Create an apt cache object
cache = apt.Cache()

# Open the cache
cache.open()

# Check if the package is installed
if 'nmap' in cache:
    pkg = cache['nmap']
    if pkg.is_installed:
        # Mark the package for removal
        pkg.mark_delete()
        cache.commit()
        print("Nmap package removed successfully!")
    else:
        print("Nmap is not installed.")
else:
    print("Package 'nmap' not found.")
```

---

### **5. Searching for a Package**

Sometimes, you might need to search for a package to check if it exists in the repository.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  apt search nmap
  ```

- **Explanation**: This searches the APT repositories for the `nmap` package and displays relevant information.

#### **Using Python with `apt` Module:**

To search for a package in Python, you can use the following approach:

```python
import apt

# Create an apt cache object
cache = apt.Cache()

# Open the cache
cache.open()

# Search for the package
if 'nmap' in cache:
    print("Package 'nmap' found in the repository.")
else:
    print("Package 'nmap' not found.")
```

---

### **6. Cleaning Up Unused Packages**

Over time, packages that are no longer required may accumulate on your system. You can remove them using the `autoremove` command.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo apt autoremove
  ```

- **Explanation**: This command removes packages that were installed as dependencies but are no longer needed.

#### **Using Python with `apt` Module:**

You can automate this cleanup task in Python:

```python
import apt

# Create an apt cache object
cache = apt.Cache()

# Open the cache
cache.open()

# Perform autoremove
cache.clean()
print("Unused packages removed successfully!")
```

---

### **7. Getting Package Information**

To get detailed information about a package, you can use the `show` command in Bash or check the package object properties in Python.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  apt show nmap
  ```

- **Explanation**: This command displays detailed information about the `nmap` package, such as its version, description, and dependencies.

#### **Using Python with `apt` Module:**

To retrieve package information in Python:

```python
import apt

# Create an apt cache object
cache = apt.Cache()

# Open the cache
cache.open()

# Get package information
if 'nmap' in cache:
    pkg = cache['nmap']
    print(f"Package: {pkg.name}")
    print(f"Version: {pkg.installed.version if pkg.is_installed else 'Not installed'}")
    print(f"Description: {pkg.candidate.summary}")
else:
    print("Package 'nmap' not found.")
```

---

### **Summary of Tasks Covered**

| **Task**                         | **Bash Command**                     | **Python with `apt` Module**                                      |
|-----------------------------------|--------------------------------------|------------------------------------------------------------------|
| Update package list               | `sudo apt update`                    | `cache.update()`                                                 |
| Upgrade installed packages        | `sudo apt upgrade`                   | `cache.upgrade(); cache.commit()`                                |
| Install a package                 | `sudo apt install nmap`              | `pkg.mark_install(); cache.commit()`                             |
| Remove a package                  | `sudo apt remove nmap`               | `pkg.mark_delete(); cache.commit()`                              |
| Search for a package              | `apt search nmap`                    | `if 'nmap' in cache`                                             |
| Clean up unused packages          | `sudo apt autoremove`                | `cache.clean()`                                                  |
| Get package information           | `apt show nmap`                      | `pkg.candidate.summary`, `pkg.installed.version`                  |

---

### **Kali Linux: Process Management**

Process management in Linux is a critical skill for system administration, helping you monitor, control, and manage running processes. In this tutorial, we will first demonstrate key process management tasks using **Bash commands**, and then replicate those tasks using **Python** with the `psutil` module, which is a Python library for system and process utilities.

---

### **1. Viewing Running Processes**

To view the running processes, you can use the `ps` command in the terminal or use the `psutil` module in Python.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  ps aux
  ```
- **Explanation**: This command lists all running processes, showing information such as PID (Process ID), CPU usage, memory usage, user, and the command that started the process.

#### **Using Python with `psutil` Module:**

You can list the running processes in Python using the `psutil.process_iter()` function.

```python
import psutil

# List all running processes
for process in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
    print(process.info)
```

---

### **2. Finding a Process by Name**

Sometimes, you want to locate a process by name, like `python` or `nginx`.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  ps aux | grep python
  ```

- **Explanation**: This filters the list of running processes to show only those containing the name "python".

#### **Using Python with `psutil` Module:**

You can search for a process by name using Python:

```python
import psutil

# Search for processes by name
for process in psutil.process_iter(['pid', 'name']):
    if 'python' in process.info['name']:
        print(f"Found process: {process.info}")
```

---

### **3. Viewing Detailed Information About a Process**

You can view detailed information such as CPU usage, memory usage, and more for a specific process by its PID (Process ID).

#### **Using Bash Commands:**

- **Command**:
  ```bash
  ps -p <PID> -o pid,ppid,cmd,%mem,%cpu
  ```

- **Explanation**: This command shows detailed information about the process with the given `PID`.

#### **Using Python with `psutil` Module:**

You can retrieve process information in Python using the PID:

```python
import psutil

# Example PID (replace with actual PID)
pid = 1234

try:
    process = psutil.Process(pid)
    print(f"Process ID: {process.pid}")
    print(f"Parent Process ID: {process.ppid()}")
    print(f"Command: {process.cmdline()}")
    print(f"CPU Usage: {process.cpu_percent()}%")
    print(f"Memory Usage: {process.memory_percent()}%")
except psutil.NoSuchProcess:
    print(f"No process found with PID {pid}")
```

---

### **4. Killing (Terminating) a Process**

You can terminate or kill a running process by its PID.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  kill <PID>
  ```

- **Explanation**: This sends a termination signal to the process identified by `PID`.

#### **Using Python with `psutil` Module:**

You can kill a process in Python as follows:

```python
import psutil

# Example PID (replace with actual PID)
pid = 1234

try:
    process = psutil.Process(pid)
    process.terminate()  # Send terminate signal
    process.wait(timeout=5)
    print(f"Process {pid} terminated successfully.")
except psutil.NoSuchProcess:
    print(f"No process found with PID {pid}")
except psutil.TimeoutExpired:
    print(f"Failed to terminate process {pid} within the timeout period.")
```

---

### **5. Monitoring System Resource Usage (CPU, Memory)**

You can monitor the overall CPU and memory usage on the system.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  top
  ```

- **Explanation**: `top` provides a real-time, interactive view of system resource usage, including CPU and memory.

#### **Using Python with `psutil` Module:**

In Python, you can monitor system resource usage as follows:

```python
import psutil

# Get system-wide CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

# Get system-wide memory usage
memory_info = psutil.virtual_memory()
print(f"Memory Usage: {memory_info.percent}%")
```

---

### **6. Listing the Process Tree (Parent-Child Relationships)**

Sometimes, you may want to see the parent-child relationships between processes.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  pstree
  ```

- **Explanation**: This displays a tree view of processes, showing their parent-child relationships.

#### **Using Python with `psutil` Module:**

To show the parent-child relationship in Python:

```python
import psutil

def print_process_tree(pid, indent=0):
    try:
        process = psutil.Process(pid)
        print(" " * indent + f"{process.pid} - {process.name()}")
        for child in process.children():
            print_process_tree(child.pid, indent + 4)
    except psutil.NoSuchProcess:
        pass

# Example PID (replace with actual PID)
pid = 1  # Usually PID 1 is the init/systemd process
print_process_tree(pid)
```

---

### **7. Changing the Priority (Nice Value) of a Process**

You can change the priority of a running process to make it run slower or faster.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  renice -n 10 -p <PID>
  ```

- **Explanation**: This sets the nice value of the process with `PID` to 10 (lower priority).

#### **Using Python with `psutil` Module:**

You can change the nice value (priority) in Python as follows:

```python
import psutil

# Example PID (replace with actual PID)
pid = 1234

try:
    process = psutil.Process(pid)
    process.nice(10)  # Set the nice value to 10
    print(f"Changed priority of process {pid} to {process.nice()}")
except psutil.NoSuchProcess:
    print(f"No process found with PID {pid}")
```

---

### **8. Running a Command in the Background**

You can start a new process and run it in the background.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  command &
  ```

- **Explanation**: This starts `command` in the background.

#### **Using Python with `subprocess` Module**:

In Python, you can start a new background process using the `subprocess` module.

```python
import subprocess

# Run a command in the background
subprocess.Popen(["sleep", "10"])  # This command sleeps for 10 seconds in the background
print("Process started in the background.")
```

---

### **Summary of Tasks Covered**

| **Task**                             | **Bash Command**                     | **Python Code with `psutil` Module**                            |
|--------------------------------------|--------------------------------------|----------------------------------------------------------------|
| View running processes               | `ps aux`                             | `psutil.process_iter()`                                        |
| Find a process by name               | `ps aux | grep python`               | Loop through `psutil.process_iter()` and filter by name         |
| View detailed information for a PID  | `ps -p <PID> -o pid,ppid,cmd,%mem,%cpu` | `psutil.Process(pid)`                                          |
| Kill (terminate) a process           | `kill <PID>`                         | `psutil.Process(pid).terminate()`                               |
| Monitor system resource usage        | `top`                                | `psutil.cpu_percent()`, `psutil.virtual_memory()`               |
| List process tree                    | `pstree`                             | Recursive `psutil.Process(pid).children()`                      |
| Change process priority              | `renice -n 10 -p <PID>`              | `psutil.Process(pid).nice(10)`                                  |
| Run a command in the background      | `command &`                          | `subprocess.Popen(["command"])`                                 |

---

### **Kali Linux: User and Group Management**

Managing users and groups is a critical task for any system administrator in Linux. In this tutorial, we'll go over the basics of **user and group management** in Kali Linux using **Bash commands** and then show how to automate these tasks using **Python**.

Python's `subprocess` module will be used to execute the user and group management tasks because, unlike `psutil`, there is no direct Python module for managing users and groups. Instead, Python will execute the same Bash commands to automate these tasks.

---

### **1. Creating a New User**

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo adduser newuser
  ```

- **Explanation**: This creates a new user named `newuser` on the system. It prompts for a password and other optional details (name, room number, etc.).

#### **Using Python with `subprocess`:**

You can create a new user by running the same `adduser` command using Python’s `subprocess` module.

```python
import subprocess

# Create a new user using adduser command
subprocess.run(["sudo", "adduser", "newuser"])
```

---

### **2. Deleting a User**

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo deluser newuser
  ```

- **Explanation**: This removes the user `newuser` from the system but retains their home directory and files unless you specify otherwise.

#### **Using Python with `subprocess`:**

You can remove a user in Python by running the `deluser` command.

```python
import subprocess

# Delete a user using deluser command
subprocess.run(["sudo", "deluser", "newuser"])
```

---

### **3. Adding a User to a Group**

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo usermod -aG groupname newuser
  ```

- **Explanation**: This adds `newuser` to the specified group (`groupname`). The `-aG` option appends the user to the group without removing them from other groups.

#### **Using Python with `subprocess`:**

You can add a user to a group using Python’s `subprocess` module as follows:

```python
import subprocess

# Add a user to a group using usermod command
subprocess.run(["sudo", "usermod", "-aG", "groupname", "newuser"])
```

---

### **4. Creating a New Group**

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo addgroup newgroup
  ```

- **Explanation**: This creates a new group named `newgroup` on the system.

#### **Using Python with `subprocess`:**

You can create a new group in Python by running the `addgroup` command.

```python
import subprocess

# Create a new group using addgroup command
subprocess.run(["sudo", "addgroup", "newgroup"])
```

---

### **5. Deleting a Group**

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo delgroup newgroup
  ```

- **Explanation**: This removes the group `newgroup` from the system.

#### **Using Python with `subprocess`:**

You can delete a group using the `delgroup` command in Python.

```python
import subprocess

# Delete a group using delgroup command
subprocess.run(["sudo", "delgroup", "newgroup"])
```

---

### **6. Changing a User's Password**

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo passwd newuser
  ```

- **Explanation**: This changes the password for the user `newuser`. You will be prompted to enter and confirm the new password.

#### **Using Python with `subprocess`:**

To change a user's password, you can use `subprocess` to call the `passwd` command.

```python
import subprocess

# Change the password for a user using passwd command
subprocess.run(["sudo", "passwd", "newuser"])
```

---

### **7. Locking and Unlocking a User Account**

#### **Locking a User Account in Bash**:

- **Command**:
  ```bash
  sudo usermod -L newuser
  ```

- **Explanation**: This locks the user `newuser` account, preventing them from logging in.

#### **Unlocking a User Account in Bash**:

- **Command**:
  ```bash
  sudo usermod -U newuser
  ```

- **Explanation**: This unlocks the `newuser` account, allowing them to log in again.

#### **Using Python with `subprocess`:**

You can lock and unlock user accounts using Python as follows:

```python
import subprocess

# Lock a user account
subprocess.run(["sudo", "usermod", "-L", "newuser"])

# Unlock a user account
subprocess.run(["sudo", "usermod", "-U", "newuser"])
```

---

### **8. Checking User Information**

#### **Using Bash Commands:**

- **Command**:
  ```bash
  id newuser
  ```

- **Explanation**: This command shows the user ID (UID), group ID (GID), and the groups the user belongs to.

#### **Using Python with `subprocess`:**

To check user information with Python:

```python
import subprocess

# Check user information using id command
subprocess.run(["id", "newuser"])
```

---

### **9. Listing All Users**

#### **Using Bash Commands:**

- **Command**:
  ```bash
  cut -d: -f1 /etc/passwd
  ```

- **Explanation**: This lists all users on the system by extracting usernames from the `/etc/passwd` file.

#### **Using Python with `subprocess`:**

You can list all users in Python using the same `cut` command.

```python
import subprocess

# List all users
subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"])
```

---

### **10. Listing All Groups**

#### **Using Bash Commands:**

- **Command**:
  ```bash
  cut -d: -f1 /etc/group
  ```

- **Explanation**: This lists all groups on the system by extracting group names from the `/etc/group` file.

#### **Using Python with `subprocess`:**

You can list all groups using Python:

```python
import subprocess

# List all groups
subprocess.run(["cut", "-d:", "-f1", "/etc/group"])
```

---

### **Summary of Tasks Covered**

| **Task**                         | **Bash Command**                     | **Python Code using `subprocess`**                         |
|-----------------------------------|--------------------------------------|-----------------------------------------------------------|
| Create a new user                 | `sudo adduser newuser`               | `subprocess.run(["sudo", "adduser", "newuser"])`           |
| Delete a user                     | `sudo deluser newuser`               | `subprocess.run(["sudo", "deluser", "newuser"])`           |
| Add a user to a group             | `sudo usermod -aG groupname newuser` | `subprocess.run(["sudo", "usermod", "-aG", "groupname", "newuser"])` |
| Create a new group                | `sudo addgroup newgroup`             | `subprocess.run(["sudo", "addgroup", "newgroup"])`         |
| Delete a group                    | `sudo delgroup newgroup`             | `subprocess.run(["sudo", "delgroup", "newgroup"])`         |
| Change a user's password          | `sudo passwd newuser`                | `subprocess.run(["sudo", "passwd", "newuser"])`            |
| Lock a user account               | `sudo usermod -L newuser`            | `subprocess.run(["sudo", "usermod", "-L", "newuser"])`     |
| Unlock a user account             | `sudo usermod -U newuser`            | `subprocess.run(["sudo", "usermod", "-U", "newuser"])`     |
| Check user information            | `id newuser`                         | `subprocess.run(["id", "newuser"])`                        |
| List all users                    | `cut -d: -f1 /etc/passwd`            | `subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"])`     |
| List all groups                   | `cut -d: -f1 /etc/group`             | `subprocess.run(["cut", "-d:", "-f1", "/etc/group"])`      |

---

### **Kali Linux: Networking**

Networking is a fundamental part of Linux administration, and it's particularly important for tasks like configuring network interfaces, testing connectivity, and managing network services. In this tutorial, we will go through some basic **networking tasks** in Kali Linux using **Bash commands** and then replicate those tasks using **Python** with modules like `subprocess`, `socket`, and `scapy` (for more advanced networking tasks).

---

### **1. Checking Your Network Interface Configuration**

The `ifconfig` command allows you to view the configuration of your network interfaces.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  ifconfig
  ```

- **Explanation**: This displays detailed information about all the active network interfaces, including IP addresses, MAC addresses, and packet statistics.

#### **Using Python with `subprocess`:**

You can run the `ifconfig` command using Python’s `subprocess` module to get the same output.

```python
import subprocess

# Run the ifconfig command to check network interfaces
subprocess.run(["ifconfig"])
```

---

### **2. Checking Connectivity with Ping**

The `ping` command is used to check whether a remote system is reachable.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  ping -c 4 google.com
  ```

- **Explanation**: This sends 4 ICMP echo request packets to `google.com` and displays the response time, showing whether the host is reachable.

#### **Using Python with `subprocess`:**

You can ping a host from Python by running the `ping` command with `subprocess`.

```python
import subprocess

# Run the ping command to check connectivity
subprocess.run(["ping", "-c", "4", "google.com"])
```

---

### **3. Checking Your IP Address**

To check your system's IP address, you can use the `ip` command or `ifconfig`.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  ip addr show
  ```

- **Explanation**: This shows your system’s IP address and other network interface details.

#### **Using Python with `subprocess`:**

You can run the `ip` command using Python as follows:

```python
import subprocess

# Run the ip command to check the IP address
subprocess.run(["ip", "addr", "show"])
```

Alternatively, you can also use the `socket` module to get your local IP address.

```python
import socket

# Get the local machine's IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"IP Address: {ip_address}")
```

---

### **4. Checking Open Ports on a System**

The `netstat` command (or `ss` in modern Linux distributions) allows you to check for open ports and active network connections.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  netstat -tuln
  ```

- **Explanation**: This shows all listening TCP and UDP ports with the `-tuln` options.

#### **Using Python with `subprocess`:**

You can check open ports in Python by running the `netstat` command.

```python
import subprocess

# Run the netstat command to check open ports
subprocess.run(["netstat", "-tuln"])
```

Alternatively, using the `socket` module, you can check if specific ports are open on the local machine.

```python
import socket

def check_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex(('localhost', port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

# Example: Check if port 80 (HTTP) is open
check_port_open(80)
```

---

### **5. Network Scanning with Nmap**

You can use `nmap` to scan a network for open ports and services.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  nmap -sP 192.168.1.0/24
  ```

- **Explanation**: This scans the local network (192.168.1.0/24) to find active hosts.

#### **Using Python with `subprocess`:**

You can call the `nmap` command from Python to run the same scan.

```python
import subprocess

# Run an nmap network scan
subprocess.run(["nmap", "-sP", "192.168.1.0/24"])
```

For a more Pythonic solution, you can use the `python-nmap` library to perform network scans programmatically.

```python
import nmap

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Scan the network for active hosts
nm.scan('192.168.1.0/24', arguments='-sP')

# Display the results
for host in nm.all_hosts():
    print(f"Host {host} is {'up' if nm[host].state() == 'up' else 'down'}")
```

Make sure to install the `python-nmap` library if you're using this approach:
```bash
pip install python-nmap
```

---

### **6. Tracing the Route to a Host**

The `traceroute` command traces the path that packets take to reach a specific host.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  traceroute google.com
  ```

- **Explanation**: This command shows each hop along the way from your system to `google.com`, providing latency information at each step.

#### **Using Python with `subprocess`:**

You can execute the `traceroute` command using `subprocess` in Python.

```python
import subprocess

# Run traceroute to a host
subprocess.run(["traceroute", "google.com"])
```

---

### **7. Creating a Simple Network Packet (Advanced)**

For advanced network tasks such as crafting network packets, you can use Python’s `scapy` module, which is a powerful tool for packet manipulation.

#### **Using Scapy in Python**:

You can create and send a simple ICMP (ping) packet using `scapy`.

```python
from scapy.all import ICMP, IP, sr1

# Create an ICMP packet
packet = IP(dst="google.com") / ICMP()

# Send the packet and wait for a response
response = sr1(packet, timeout=2)

# Print the response details
if response:
    response.show()
else:
    print("No response received")
```

Make sure to install `scapy` before running this code:
```bash
pip install scapy
```

---

### **8. Network Interface Configuration**

You can bring network interfaces up or down using the `ip` or `ifconfig` commands.

#### **Using Bash Commands:**

- **Bring an Interface Up**:
  ```bash
  sudo ifconfig eth0 up
  ```

- **Bring an Interface Down**:
  ```bash
  sudo ifconfig eth0 down
  ```

#### **Using Python with `subprocess`:**

You can automate enabling and disabling network interfaces using `subprocess` in Python.

```python
import subprocess

# Bring the eth0 interface up
subprocess.run(["sudo", "ifconfig", "eth0", "up"])

# Bring the eth0 interface down
subprocess.run(["sudo", "ifconfig", "eth0", "down"])
```

---

### **Summary of Tasks Covered**

| **Task**                               | **Bash Command**                          | **Python Code**                                         |
|----------------------------------------|-------------------------------------------|--------------------------------------------------------|
| Check network interface configuration  | `ifconfig`                                | `subprocess.run(["ifconfig"])`                         |
| Check connectivity with ping           | `ping -c 4 google.com`                    | `subprocess.run(["ping", "-c", "4", "google.com"])`     |
| Check IP address                       | `ip addr show`                            | `subprocess.run(["ip", "addr", "show"])`, `socket`      |
| Check open ports                       | `netstat -tuln`                           | `subprocess.run(["netstat", "-tuln"])`, `socket`        |
| Perform a network scan                 | `nmap -sP 192.168.1.0/24`                 | `subprocess.run(["nmap", "-sP", "192.168.1.0/24"])`, `python-nmap` |
| Trace the route to a host              | `traceroute google.com`                   | `subprocess.run(["traceroute", "google.com"])`          |
| Bring a network interface up or down   | `sudo ifconfig eth0 up/down`              | `subprocess.run(["sudo", "ifconfig", "eth0", "up/down"])` |
| Create and send network packets        | Use tools like `scapy`                    | `from scapy.all import IP, ICMP, sr1`                   |

---

### **Kali Linux: Security**

Kali Linux is designed for security testing, making it essential to understand basic security tasks such as scanning networks, checking for vulnerabilities, and analyzing security logs.

---

### **1. Checking for Open Ports with Nmap**

Nmap is a powerful network scanning tool used to discover open ports, services, and vulnerabilities on a system.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  nmap -sS -p 1-1000 192.168.1.10
  ```

- **Explanation**: This performs a SYN scan (`-sS`) of ports 1-1000 on the IP address `192.168.1.10`. This is one of the most common techniques for checking open ports.

#### **Using Python with `subprocess`:**

You can use the `subprocess` module to automate the Nmap scan in Python.

```python
import subprocess

# Run an Nmap scan on the target system
subprocess.run(["nmap", "-sS", "-p", "1-1000", "192.168.1.10"])
```

---

### **2. Scanning for Vulnerabilities with Nikto**

Nikto is a web server scanner that detects vulnerabilities such as outdated software, dangerous files, and configuration issues.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  nikto -h http://example.com
  ```

- **Explanation**: This scans the web server at `http://example.com` for vulnerabilities.

#### **Using Python with `subprocess`:**

You can automate the Nikto scan in Python using `subprocess`.

```python
import subprocess

# Run a Nikto scan on the target web server
subprocess.run(["nikto", "-h", "http://example.com"])
```

---

### **3. Cracking Passwords with John the Ripper**

John the Ripper is a popular password cracking tool that can be used to crack password hashes.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
  ```

- **Explanation**: This command uses a wordlist (in this case, the `rockyou.txt` wordlist) to attempt to crack the passwords in `hashes.txt`.

#### **Using Python with `subprocess`:**

You can run the same password cracking task using Python.

```python
import subprocess

# Crack passwords with John the Ripper
subprocess.run(["john", "--wordlist=/usr/share/wordlists/rockyou.txt", "hashes.txt"])
```

---

### **4. Checking for Running Services with Netstat**

Netstat helps to identify open ports and running services on a system. This is useful for identifying potentially vulnerable services.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  netstat -tuln
  ```

- **Explanation**: This shows all listening TCP and UDP ports, helping you see which services are active and potentially vulnerable.

#### **Using Python with `subprocess`:**

You can check for running services in Python by using the same `netstat` command.

```python
import subprocess

# Check for running services using netstat
subprocess.run(["netstat", "-tuln"])
```

---

### **5. Monitoring Logs for Suspicious Activity**

The `tail` command can be used to monitor logs in real-time, helping you keep an eye on suspicious activities.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  tail -f /var/log/auth.log
  ```

- **Explanation**: This command shows real-time updates of the `auth.log` file, which logs authentication-related events such as login attempts.

#### **Using Python with `subprocess`:**

You can monitor logs in real-time using Python.

```python
import subprocess

# Monitor the authentication log in real-time
subprocess.run(["tail", "-f", "/var/log/auth.log"])
```

---

### **6. Generating Secure Passwords**

In Bash, you can generate random passwords using `openssl` or similar tools.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  openssl rand -base64 12
  ```

- **Explanation**: This generates a random, base64-encoded password of 12 characters.

#### **Using Python with `secrets`:**

In Python, you can use the `secrets` module to generate cryptographically secure random passwords.

```python
import secrets
import string

# Generate a secure password
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(12))
print(f"Generated password: {password}")
```

---

### **7. Capturing Network Traffic with TCPDump**

TCPDump is a powerful packet analyzer used to capture and analyze network traffic.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sudo tcpdump -i eth0 -w capture.pcap
  ```

- **Explanation**: This captures all network traffic on the `eth0` interface and saves it to the file `capture.pcap` for later analysis.

#### **Using Python with `subprocess`:**

You can automate traffic capture with Python.

```python
import subprocess

# Capture network traffic using tcpdump
subprocess.run(["sudo", "tcpdump", "-i", "eth0", "-w", "capture.pcap"])
```

---

### **8. Testing for Weak SSL/TLS Configurations**

OpenSSL can be used to check the strength of SSL/TLS configurations on a server.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  openssl s_client -connect example.com:443
  ```

- **Explanation**: This checks the SSL/TLS certificate and cipher suites of the server at `example.com` on port 443.

#### **Using Python with `subprocess`:**

You can check the SSL/TLS configuration using Python as well.

```python
import subprocess

# Test for weak SSL/TLS configurations
subprocess.run(["openssl", "s_client", "-connect", "example.com:443"])
```

---

### **9. Hashing a File for Integrity Verification**

Hashing files allows you to verify the integrity of a file to ensure that it hasn’t been tampered with.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  sha256sum file.txt
  ```

- **Explanation**: This generates the SHA-256 hash of `file.txt`, which you can use to verify its integrity.

#### **Using Python with `hashlib`:**

In Python, you can use the `hashlib` module to generate file hashes.

```python
import hashlib

# Hash a file using SHA-256
def hash_file(filename):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# Hash the file and print the result
print(hash_file('file.txt'))
```

---

### **10. Scanning for Malware with ClamAV**

ClamAV is a popular open-source antivirus tool used for scanning systems for malware.

#### **Using Bash Commands:**

- **Command**:
  ```bash
  clamscan -r /home/user
  ```

- **Explanation**: This scans the `/home/user` directory recursively for malware.

#### **Using Python with `subprocess`:**

You can automate ClamAV scanning using Python.

```python
import subprocess

# Scan the home directory for malware
subprocess.run(["clamscan", "-r", "/home/user"])
```

---

### **Summary of Tasks Covered**

| **Task**                            | **Bash Command**                                       | **Python Code using `subprocess`/modules**                          |
|-------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------|
| Check for open ports with Nmap      | `nmap -sS -p 1-1000 192.168.1.10`                      | `subprocess.run(["nmap", "-sS", "-p", "1-1000", "192.168.1.10"])`   |
| Scan for web vulnerabilities        | `nikto -h http://example.com`                          | `subprocess.run(["nikto", "-h", "http://example.com"])`             |
| Crack passwords with John           | `john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt` | `subprocess.run(["john", "--wordlist=/usr/share/wordlists/rockyou.txt", "hashes.txt"])` |
| Check running services              | `netstat -tuln`                                        | `subprocess.run(["netstat", "-tuln"])`                              |
| Monitor logs for suspicious activity| `tail -f /var/log/auth.log`                            | `subprocess.run(["tail", "-f", "/var/log/auth.log"])`               |
| Generate secure passwords           | `openssl rand -base64 12`                              | `secrets.choice(alphabet)`                                          |
| Capture network traffic             | `sudo tcpdump -i eth0 -w capture.pcap`                 | `subprocess.run(["sudo", "tcpdump", "-i", "eth0", "-w", "capture.pcap"])` |
| Test for weak SSL/TLS configurations| `openssl s_client -connect example.com:443`
