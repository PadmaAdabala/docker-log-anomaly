import re

# Load log file
with open("../logs/app.log", "r") as file:
    logs = file.readlines()

# Define what "normal" log entries should look like
normal_patterns = [
    "Normal access",
    "Admin area accessed",
    "Login attempt"
]

print("=== Anomalies Detected ===")
for line in logs:
    if not any(pattern in line for pattern in normal_patterns):
        print(line.strip())
