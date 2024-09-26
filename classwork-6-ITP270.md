### Module - 6 (Lists and Dictionaries)

---

## **Introduction:**

Data structures are a fundamental part of programming, allowing us to organize and store data efficiently. In the context of ethical hacking, understanding how to handle lists and dictionaries in Python is crucial for automating tasks such as managing IP addresses, storing credentials, or handling payloads.

---

## **Part 1: Lists in Python**

### **What is a List?**

A list is an ordered collection of items (or elements) that can hold various data types. Lists are **mutable**, meaning you can change them after creation. Lists are useful for storing sequences of data, such as IP addresses or open ports.

### **Creating a List:**

```python
# A list of IP addresses in a local network
ip_addresses = ['192.168.1.1', '192.168.1.2', '192.168.1.3']

# A list of commonly used ports
common_ports = [21, 22, 80, 443]
```

### **List Operations:**

1. **Accessing Elements:**
   You can access elements in a list using an index, starting from 0.

```python
# Access the first IP address
print(ip_addresses[0])  # Output: 192.168.1.1
```

2. **Modifying Elements:**

```python
# Changing the second IP address
ip_addresses[1] = '192.168.1.20'
```

3. **Appending New Data:**

```python
# Adding a new IP address
ip_addresses.append('192.168.1.4')
```

4. **Removing Data:**

```python
# Removing an IP address from the list
ip_addresses.remove('192.168.1.3')
```

---

### **Real-World Example: Port Scanning**

In ethical hacking, we often scan for open ports on target machines. Let’s create a Python script that stores a list of open ports after scanning.

```python
# A simple script to scan open ports (this example will just add ports to a list)
open_ports = []

# Simulating a scan that found ports 80 and 443 open
open_ports.append(80)
open_ports.append(443)

# Display the open ports
print(f"Open ports: {open_ports}")
```

*Explanation: In this example, we’re using a list to store and display open ports discovered during a scan.*

---

## **Part 2: Dictionaries in Python**

### **What is a Dictionary?**

A dictionary is a **key-value** data structure where each key is associated with a value. This is useful when you want to map something (like an IP address) to relevant data (such as its status or open ports).

### **Creating a Dictionary:**

```python
# A dictionary mapping IP addresses to their status
network_devices = {
    '192.168.1.1': 'Online',
    '192.168.1.2': 'Offline',
    '192.168.1.3': 'Online'
}
```

### **Dictionary Operations:**

1. **Accessing Values:**
   Use the key to retrieve its associated value.

```python
# Get the status of a specific IP address
print(network_devices['192.168.1.1'])  # Output: Online
```

2. **Modifying Values:**

```python
# Updating the status of an IP address
network_devices['192.168.1.2'] = 'Online'
```

3. **Adding New Key-Value Pairs:**

```python
# Adding a new device
network_devices['192.168.1.4'] = 'Online'
```

4. **Removing Key-Value Pairs:**

```python
# Removing a device
del network_devices['192.168.1.3']
```

---

### **Real-World Example: Storing Device Data**

Ethical hackers often need to map IP addresses to other data such as their status, operating system, or the services they are running. Let’s create a dictionary that stores this information.

```python
# A dictionary mapping IP addresses to device information
device_info = {
    '192.168.1.1': {'status': 'Online', 'OS': 'Linux', 'open_ports': [22, 80]},
    '192.168.1.2': {'status': 'Offline', 'OS': 'Windows', 'open_ports': []}
}

# Display device info
for ip, info in device_info.items():
    print(f"IP: {ip} - Status: {info['status']}, OS: {info['OS']}, Open Ports: {info['open_ports']}")
```

*Explanation: In this example, we store more complex information about each device in the dictionary, including its operating system and open ports.*

---

## **Advanced Concepts:**

### **List Comprehensions:**
List comprehensions are a concise way to create lists.

```python
# Create a list of IP addresses that are online
online_devices = [ip for ip, status in network_devices.items() if status == 'Online']
print(online_devices)
```

### **Nested Dictionaries:**
Dictionaries can contain other dictionaries, allowing for more complex data structures.

```python
# Adding more detailed information to the device_info dictionary
device_info['192.168.1.3'] = {
    'status': 'Online',
    'OS': 'Linux',
    'open_ports': [22, 80, 443],
    'services': {'SSH': 22, 'HTTP': 80, 'HTTPS': 443}
}
```

---

## **Use Case Examples:**

### **Example 1: Automating Network Scanning**

This script creates a dictionary to store device information after scanning a local network.

```python
import os

# Simulate a network scan with nmap (this is a mockup)
device_info = {
    '192.168.1.1': {'status': 'Online', 'OS': 'Linux', 'open_ports': [22, 80]},
    '192.168.1.2': {'status': 'Offline', 'OS': 'Windows', 'open_ports': []},
}

# Display the scan results
for ip, info in device_info.items():
    print(f"IP: {ip} - Status: {info['status']}, OS: {info['OS']}, Open Ports: {info['open_ports']}")
```

### **Example 2: Password Storage and Management**

This script demonstrates using a dictionary to store user credentials securely in an ethical hacking context.

```python
# Simulating a user credential storage
user_credentials = {
    'admin': 'hashed_password_12345',
    'user1': 'hashed_password_67890'
}

# Access a user's password
print(f"Admin's hashed password: {user_credentials['admin']}")
```
