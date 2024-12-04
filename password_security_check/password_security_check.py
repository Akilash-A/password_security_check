import re
import os
import platform

# Function to detect the correct rockyou file based on the system
def get_rockyou_file():
    # Check if the system is BlackArch by looking for a specific file
    if os.path.exists("/usr/share/wordlists/rockyou.txt"):  # BlackArch uses this path
        return "/usr/share/wordlists/rockyou.txt"
    elif os.path.exists("/usr/share/seclists/Passwords/Leaked-Databases/rockyou-05.txt"):  # For Kali and others
        return [
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-05.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-10.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-15.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-20.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-25.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-30.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-35.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-40.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-45.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-50.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-55.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-60.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-65.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-70.txt",
            "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-75.txt"
        ]
    else:
        return None  # If no wordlist is found

# Function to read and load passwords from files into a dictionary for quick lookup
def load_password_files(file_paths):
    password_dict = {}
    for file_path in file_paths:
        try:
            with open(file_path, 'r', errors='ignore') as file:
                for line in file:
                    password = line.strip()
                    password_dict[password] = file_path  # Store the password with the file name
        except Exception as e:
            print(f"Could not read {file_path}: {e}")
    return password_dict

# Function to check the strength of the password
def check_password_strength(password, password_dict=None):
    # Criteria
    length_criteria = len(password) >= 12
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_+=[]{}|;:'\",.<>?/\\`~" for char in password)
    no_common_pattern = not re.search(r'(123|abc|password|qwerty|letmein|iloveyou)', password, re.IGNORECASE)

    # Check if the password is from the leak files
    if password_dict and password in password_dict:
        return f"Password is from a leaked database: {password_dict[password]}"

    # Initialize strength score
    strength_score = 0

    # Update strength score based on criteria
    if length_criteria:
        strength_score += 2
    if uppercase_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if digit_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 2
    if no_common_pattern:
        strength_score += 2

    # Determine strength level
    if strength_score >= 8:
        return "Strong Password"
    elif strength_score >= 5:
        return "Moderate Password"
    else:
        return "Weak Password"

# Display important note before running the code
print("\033[92mNote: Before running this code:")
print("\033[92m- The program will check if the password is from a known leaked database (e.g., RockYou, other password dumps).")
print("\033[92m- It will also evaluate the strength of the password based on length, character variety, and complexity.")
print("\033[92m- If the wordlist (RockYou or others) is installed, the program will alert you if the password is found in the database.")
print("\033[92m- If the wordlist is not installed, the program will continue to check the password's strength without comparing it to leaked passwords.")
print("\033[0m")  # Reset color

# Get the correct rockyou file(s) based on the system
rockyou_file = get_rockyou_file()

if rockyou_file:
    # Load passwords from the specified files into a dictionary
    if isinstance(rockyou_file, list):  # If it is a list, load all files
        password_dict = load_password_files(rockyou_file)
    else:  # If it is a single file, just load that
        password_dict = load_password_files([rockyou_file])
    print("\033[93mWarning: RockYou wordlist found and used for password checking.\033[0m")
else:
    password_dict = None  # No wordlist available
    print("\033[91mAlert: No RockYou wordlist found. Password checking will continue normally.\033[0m")

# Input from the user
password = input("Enter your password: ")

# Check password strength and whether it is in the leak files
result = check_password_strength(password, password_dict)
print(f"\033[0mPassword strength: {result}")
