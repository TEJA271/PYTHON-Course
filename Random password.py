import random
import string

def easy_password(length=6):
    characters = string.ascii_letters + string.digits  # ascii_letters = a-z + A-Z
    password = ''.join(random.choices(characters, k=length))
    return password

print("Your super easy password is:", easy_password())
