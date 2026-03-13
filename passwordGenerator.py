import secrets
import string
import math

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?"

# Ask the user for the password length
#Faith part
def ask_length(min_len=8):
    while True:
        try:
            length = int(input(f"Enter password length (at least {min_len}): "))
            if length >= min_len:
                return length
            else:
                print(f"Length must be at least {min_len}. Please try again.")
        except ValueError:
            print("Please enter a whole number.")
#
# Kishwer part
#Generate the password which contains charactors, special characters and digits align with the required length (taken from user). the function takes user's required length as an input
def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += SYMBOLS

    if not character_pool:
        return "Error: No character types selected!"

    password = "".join(secrets.choice(character_pool) for _ in range(length))
    return password
#the generated password should meet the minimum password policy. this function verify it
def is_secure(pw, min_len=8):
    """Return True if password meets minimum policy."""
    if len(pw) < min_len:
        return False
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_symbol = any(c in SYMBOLS for c in pw)
    return has_upper and has_lower and has_digit and has_symbol
    
#function defines the entropy of the generated password
def estimate_entropy_bits(pw):
    """Rough entropy estimate based on the size of the character set actually used."""
    charset = 0
    if any(c.islower() for c in pw):
        charset += 26
    if any(c.isupper() for c in pw):
        charset += 26
    if any(c.isdigit() for c in pw):
        charset += 10
    if any(c in SYMBOLS for c in pw):
        charset += len(SYMBOLS)
    # Avoid log2(0)
    if charset == 0:
        return 0.0
    return len(pw) * math.log2(charset)
    
#ben Part
#define below function rate the strength of the generated password as fair, strong, very strong on the bases of calculated entropy and policy
def rate_strength(pw):
    """Return a simple label based on entropy and policy."""
    entropy = estimate_entropy_bits(pw)
    if not is_secure(pw):
        return "❌ Not Secure", entropy
    # Rough bands (you can tweak these)
    if entropy < 50:
        return "⚠️ Fair", entropy
    elif entropy < 80:
        return "✅ Strong", entropy
    else:
        return "🛡️ Very Strong", entropy


#print("Generated Password:", generate_password(len))

if __name__ == "__main__":
    #input taken for the required length from the user
    length = ask_length(8)
    # print("Your secure password is:", generate_password(length))

     #Keep generating until it meets the secure policy (optional loop)
    # If you prefer to generate once and simply report, remove the loop and just evaluate.
    while True:
        password = generate_password(length)
        if is_secure(password):
            break

    label, entropy = rate_strength(password)
    print("\nYour secure password is:", password)
    print(f"Strength: {label}  (≈ {entropy:.1f} bits of entropy)")


# Ben - corrected code so takes into consideration the user inputs and first and second part function as intended
