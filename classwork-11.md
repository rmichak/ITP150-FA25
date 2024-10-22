### **Command Line: Basic Navigation**

### **Objective**

- `pwd`: Print working directory
- `ls`: List files in the current directory
- `cd`: Change directory
- `mkdir`: Create new directories
- `rmdir`: Remove empty directories
- `cp`: Copy files or directories
- `mv`: Move or rename files or directories
- `find`: Search for files and directories

### **1. `pwd` (Print Working Directory)**

**Purpose**: Shows the full path of the current working directory.

#### **Example Scenario**:
You’re not sure which directory you are in while running a security script or checking logs.

#### **Usage**:
```bash
pwd
```

#### **Output**:
```bash
/home/user/security-scripts
```
This command displays the absolute path of the current working directory. It's useful for confirming where you are before running any commands.

---

### **2. `ls` (List Directory Contents)**

**Purpose**: Lists the contents of the current directory, including files and directories.

#### **Example Scenario**:
You want to inspect the contents of a directory containing your security scripts or logs.

#### **Usage**:
```bash
ls
```

#### **Output**:
```bash
script1.py  script2.py  log1.txt  log2.txt
```

#### **Additional Options**:
- `ls -l`: Displays detailed information, including permissions, ownership, and file sizes.
- `ls -a`: Includes hidden files (files starting with a dot).
- `ls -lh`: Combines human-readable file sizes with detailed information.

```bash
ls -la
```
This will list all files, including hidden ones, in a detailed format.

---

### **3. `cd` (Change Directory)**

**Purpose**: Changes the current directory to another directory.

#### **Example Scenario**:
You want to navigate to a specific directory where your scripts or logs are stored.

#### **Usage**:
```bash
cd /var/log
```
This command changes your current directory to `/var/log`, where system logs are stored.

#### **Going Back to Home Directory**:
```bash
cd ~
```
The `~` symbol represents your home directory. This command takes you back to your home folder.

#### **Going Up One Directory Level**:
```bash
cd ..
```
The `..` means "parent directory," so this command takes you one level up in the file system hierarchy.

#### **Navigation Tip**:
- You can combine paths to move multiple levels at once: 
  ```bash
  cd ../Documents/Reports
  ```

---

### **4. `ls -R` (Recursive Directory Listing)**

**Purpose**: Lists all files in the current directory and its subdirectories.

#### **Example Scenario**:
You need to search through a directory tree, like finding scripts or log files in nested directories.

#### **Usage**:
```bash
ls -R /home/user/security-scripts
```

#### Output Example**:
```bash
/home/user/security-scripts:
script1.py  script2.py  logs/

/home/user/security-scripts/logs:
log1.txt  log2.txt
```

This command lists the contents of all directories under `/home/user/security-scripts` recursively.

---

### **5. `tree` (Display Directory Tree)**

**Purpose**: Displays the directory structure as a tree. This is not installed by default in most Linux distributions, but you can install it if needed.

#### **Example Scenario**:
You want to visualize the directory structure of your project folders.

#### **Usage**:
```bash
tree /home/user/security-scripts
```

#### Output**:
```bash
/home/user/security-scripts
├── script1.py
├── script2.py
└── logs
    ├── log1.txt
    └── log2.txt
```

This command gives a visual tree-like view of your directory structure, which is useful when working with large projects.

---

### **6. `mkdir` (Make Directory)**

**Purpose**: Creates a new directory in the current working directory or specified path.

#### **Example Scenario**:
You are organizing log files or scripts and want to create a new folder.

#### **Usage**:
```bash
mkdir logs
```
Creates a new directory called `logs` in your current directory.

#### **Creating Nested Directories**:
```bash
mkdir -p /home/user/security-scripts/2024/logs
```
The `-p` option allows the creation of parent directories if they don’t already exist, making it easier to create a multi-level directory structure in one command.

---

### **7. `rmdir` (Remove Directory)**

**Purpose**: Deletes an empty directory.

#### **Example Scenario**:
You want to remove a folder that’s no longer needed, but it must be empty before deletion.

#### **Usage**:
```bash
rmdir logs
```
This command removes the `logs` directory, but it will only work if the directory is empty.

#### **Removing Non-Empty Directories**:
If you need to remove a directory with files, use the `rm` command with the `-r` option (recursive):
```bash
rm -r logs
```
This will delete the directory along with its contents.

---

### **8. `cp` (Copy Files and Directories)**

**Purpose**: Copies files or directories from one location to another.

#### **Example Scenario**:
You want to back up a configuration file before editing it.

#### **Usage**:
```bash
cp config.txt config_backup.txt
```
This command creates a copy of `config.txt` called `config_backup.txt`.

#### **Copying Directories**:
To copy a directory and all its contents:
```bash
cp -r /var/log /home/user/log_backup
```
The `-r` option means "recursive," allowing the command to copy all the contents, including subdirectories.

---

### **9. `mv` (Move or Rename Files and Directories)**

**Purpose**: Moves files or directories from one location to another or renames them.

#### **Example Scenario**:
You want to move log files to a backup folder or rename a script file.

#### **Usage** (Move File):
```bash
mv log.txt /home/user/backup/
```
Moves `log.txt` to the `backup` folder.

#### **Usage** (Rename File):
```bash
mv old_script.py new_script.py
```
Renames `old_script.py` to `new_script.py`.

---

### **10. `find` (Search for Files and Directories)**

**Purpose**: Searches for files and directories based on specific conditions, such as name or type.

#### **Example Scenario**:
You’re searching for Python scripts within your project directories.

#### **Usage** (Search by Name):
```bash
find /home/user/security-scripts -name "*.py"
```
This command searches the directory `/home/user/security-scripts` for all Python files (`*.py`).

#### **Search by Type (Directory)**:
```bash
find /home/user/security-scripts -type d
```
Searches for all directories under `/home/user/security-scripts`.

---

### **Command Line: `help` and `man` Commands**

In Linux, understanding how to use commands effectively is crucial. Two essential commands for obtaining information about other commands and programs are **`help`** and **`man`**. 

---

### **1. `help` Command**

The `help` command provides quick information about built-in **shell commands** (also known as *bash built-ins*). These are commands that are part of the shell itself, not external programs.

#### **Usage**:
```bash
help [command]
```
- The `help` command gives a brief description of a command, showing its syntax, options, and a short description.

#### **Example**:
```bash
help cd
```
**Output**:
```bash
cd: cd [-L|[-P [-e]] [-@]] [dir]
    Change the shell working directory.
    ...
```
This shows the syntax and options available for the `cd` (change directory) command.

#### **Key Points**:
- `help` is only available for **shell built-in commands** such as `cd`, `echo`, `exit`, `export`, etc.
- The information provided is brief and is primarily meant to give quick help on how to use the command.

#### **Example: Using `help` for the `exit` command**:
```bash
help exit
```
**Output**:
```bash
exit: exit [n]
    Exit the shell.
    Exits the shell with a status of N. If N is omitted, the exit status is that of the last command executed.
```
This output gives you the basic usage of the `exit` command, explaining how to use it to exit the shell and set the exit status.

---

### **2. `man` Command**

The `man` command (short for "manual") is used to display the **manual pages** for any command or program installed on the system. These manual pages are much more detailed than the `help` command and typically include sections like name, synopsis, description, options, examples, and sometimes even the author's information.

#### **Usage**:
```bash
man [command]
```
- The `man` command opens the manual page for the specified command, providing comprehensive documentation.

#### **Example**:
```bash
man ls
```
**Output** (partial):
```bash
LS(1)                    User Commands                    LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List information about the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
...
```
The `man` command for `ls` opens a detailed manual, which includes sections like **Name**, **Synopsis**, **Description**, **Options**, etc.

#### **Key Points**:
- The `man` command is available for almost every command, program, or system utility installed on the system.
- The manual pages provide detailed documentation, making them ideal for understanding more advanced options or usage patterns.
- The `man` command is useful for **external commands and programs** like `ls`, `find`, `grep`, etc.

#### **Navigating in `man` Pages**:
- Use the **arrow keys** or **Page Up/Page Down** to scroll.
- Press **`q`** to quit and exit the manual page.
- You can also search inside a `man` page by pressing **`/`** followed by the search term, and press **`n`** to find the next occurrence.

#### **Example: Using `man` for the `find` command**:
```bash
man find
```
**Output** (partial):
```bash
FIND(1)                General Commands Manual               FIND(1)

NAME
       find - search for files in a directory hierarchy

SYNOPSIS
       find [path...] [expression]

DESCRIPTION
       This manual page documents the GNU version of find.  find searches the
       directory tree rooted at each given starting-point by evaluating the
       given expression from left to right, according to the rules of prece‐
       dence (see section OPERATORS), until the outcome is known...
```
This provides a complete guide to using the `find` command, explaining all its options and how to use it for searching files.

---

### **Key Differences Between `help` and `man`**

| **Feature**         | **`help`**                        | **`man`**                        |
|---------------------|-----------------------------------|----------------------------------|
| **Purpose**         | Provides quick info on **shell built-ins**. | Displays **detailed manual pages** for any command, program, or utility. |
| **Scope**           | Limited to **bash built-in** commands like `cd`, `exit`, etc. | Works for both **built-in** and **external commands** like `ls`, `find`, etc. |
| **Detail Level**    | Basic usage and brief explanation. | Comprehensive documentation with all options and descriptions. |
| **Best For**        | Quick help on built-in commands.   | Detailed help for understanding all aspects of a command. |

---

### **Practical Examples of Using `help` and `man`**

#### **Example 1: Checking Help for the `echo` Command**
The `echo` command is a shell built-in that prints text to the terminal.

```bash
help echo
```
**Output**:
```bash
echo: echo [-neE] [arg ...]
    Write arguments to the standard output.
```

#### **Example 2: Viewing the Manual for the `echo` Command**
The `man` command provides a detailed description of the external `echo` command.

```bash
man echo
```
**Output** (partial):
```bash
ECHO(1)                    User Commands                    ECHO(1)

NAME
       echo - display a line of text

SYNOPSIS
       echo [SHORT-OPTION]... [STRING]...

DESCRIPTION
       Echo the STRING(s) to standard output.
       ...
```

#### **Example 3: Learning About the `exit` Command Using `help`**
```bash
help exit
```
**Output**:
```bash
exit: exit [n]
    Exit the shell.
    Exits the shell with a status of N.
```

#### **Example 4: Detailed Information About `find` Using `man`**
The `find` command is a versatile tool for searching directories. Using `man find` provides a wealth of information for its complex usage.

```bash
man find
```

---

### **Additional Tips**

- **Help for Specific Sections**:
  You can look for specific sections in a manual by appending a section number. For example, to look up system calls, use:
  ```bash
  man 2 open
  ```

- **`whatis` Command**:
  To get a brief one-line description of a command, you can use the `whatis` command:
  ```bash
  whatis grep
  ```
  **Output**:
  ```bash
  grep (1) - print lines matching a pattern
  ```

- **`apropos` Command**:
  Use `apropos` to search for commands related to a particular keyword:
  ```bash
  apropos network
  ```
  This will return a list of commands related to "network."

---

### **Summary**

- The **`help`** command is used for shell built-ins like `cd`, `echo`, and `exit`, giving quick and basic usage information.
- The **`man`** command is used to access manual pages for any installed command or utility, providing detailed descriptions, options, and examples.
