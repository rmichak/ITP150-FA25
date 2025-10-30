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
