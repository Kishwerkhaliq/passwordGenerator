# passwordGenerator
The Password Generator project creates strong, random passwords based on a length entered by the user. It combines letters, numbers, and symbols to produce secure passwords, demonstrating user input handling, randomness, and basic programming logic.

Here are the features of the updated password generator code:

User input validation
Prompts for length and re-asks on non-numeric input or values below the minimum.


Minimum length policy (≥ 8)
Enforces a floor length (configurable via parameter).


Cryptographically secure randomness
Uses secrets.choice to generate unpredictable passwords.


Rich character set
Combines uppercase, lowercase, digits, and symbols (customisable SYMBOLS).


Security policy check (is_secure)
Verifies the password contains at least one uppercase, one lowercase, one digit, and one symbol, in addition to meeting the length rule.


Entropy estimation (estimate_entropy_bits)
Provides an approximate strength measure (bits) based on which character sets are present and the length.


Human‑readable strength rating (rate_strength)
Labels passwords as Not Secure, Fair, Strong, or Very Strong.


Optional enforcement loop
Regenerates passwords until they meet the security policy.


Clean, modular design
Separate functions for length input, generation, policy validation, entropy estimation, and strength rating, easy to test and extend.


Clear user feedback
Prints helpful prompts and error messages, and displays the final password with its strength and entropy estimate.


