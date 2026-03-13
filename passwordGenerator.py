
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
