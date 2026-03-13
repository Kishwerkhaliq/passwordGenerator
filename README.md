# passwordGenerator
The Password Generator project creates strong, random passwords based on a length entered by the user. It combines letters, numbers, and symbols to produce secure passwords, demonstrating user input handling, randomness, and basic programming logic.
import random
import string 

length = int(input("Enter the length of the password: "))
letters = ''.join(random.choice(string.ascii_letters) for i in range(length // 2))

remaining = length - len(letters)
others = ''.join(random.choice(string.digits + string.punctuation) for i in range(remaining))
