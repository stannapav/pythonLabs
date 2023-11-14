import random
import string

def containsNumber(password):
    return any(char.isdigit() for char in password)

def containsUpper(password):
    return any(char.isupper() for char in password)

def containsLower(password):
    return any(char.islower() for char in password)

def containsPunctuation(password):
    return any(char in string.punctuation for char in password)

random.seed()
password = ""

while True:
    rand = random.randint(1, 5)

    if rand == 1:
        password += random.choice(string.ascii_letters).upper()
    elif rand == 2:
        password += random.choice(string.ascii_letters).lower()
    elif rand == 3:
        password += random.choice(string.digits)
    elif rand == 4:
        password += random.choice(string.punctuation)

    if len(password) >= 8 and containsNumber(password) and containsUpper(password) and containsLower(password) and containsPunctuation(password):
        break

print(password)