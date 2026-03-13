import secrets
import string

# Ask the user for the password length
len = int(input("Enter the desired password length: "))
# Faith 



def generate_password(length=(len-4), use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += "!@#$%^&*()-_=+[]{};:,.<>?"

    if not character_pool:
        return "Error: No character types selected!"

    password = "".join(secrets.choice(character_pool) for _ in range(len))
    return password

print("Generated Password:", generate_password(len))

def is_strong_password(password):
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    long_enough = len(password) > 8

    if has_letter and has_digit and has_special and long_enough:
        return "Password is strong"
    return "Password is not strong enough"
    
print(is_strong_password(password))

# Ben
