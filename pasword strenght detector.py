import re

def check_password_strength(password):
    strength = 0

    # Conditions
    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Levels (added "Excellent" for max score = 5)
    levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong", "Excellent"]
    return levels[strength]

# Run Program
if __name__ == "__main__":
    password = input("Enter a password: ")
    print("Password Strength:", check_password_strength(password))
