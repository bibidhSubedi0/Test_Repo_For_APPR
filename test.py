import os
import subprocess
import time

# GLOBAL VARIABLE (Bad Practice)
user_cache = []

def process_user_data(user_input, filename):
    """
    Reads a file and processes user commands.
    """
    # 1. RESOURCE LEAK: Opening file without 'with' statement
    f = open(filename, 'r')
    data = f.read()
    
    # 2. SECURITY FLAW: Command Injection
    # Never pass user input directly to a shell command!
    print(f"Log: Processing {user_input}")
    subprocess.call(f"echo {user_input} >> system.log", shell=True)

    # 3. LOGIC BUG: Modifying list while iterating
    # This will skip elements or crash
    numbers = [1, 2, 3, 4, 5, 6]
    for n in numbers:
        if n % 2 == 0:
            numbers.remove(n)

    # 4. PERFORMANCE DISASTER: O(n^3) Complexity
    # This triple nested loop does nothing but waste CPU
    total = 0
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                total += 1
    
    # 5. TYPE ERROR: Adding String to Integer
    # This will crash at runtime
    result = total + " processed"
    
    return result

class Database:
    # 6. SECURITY FLAW: Hardcoded Secrets
    def __init__(self):
        self.password = "admin123" 
        self.url = "postgres://admin:admin123@localhost:5432/db"

    def connect(self):
        print("Connected!")