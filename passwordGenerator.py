import string
import secrets

# Ask the user for the password length
length = int(input("Enter the desired password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
use_digits = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"
# Faith

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += "!@#$%^&*()-_=+[]{};:,<>?"

    if not character_pool:
        return "Error: No character types selected!"

    password = "".join(secrets.choice(character_pool) for _ in range(length))
    return password

print("Generated Password:", generate_password(length, use_upper, use_lower, use_digits, use_symbols))

# Ben - corrected code so takes into consideration the user inputs and first and second part function as intended
