#4. Password Generator
#A password generator creates random passwords for users. You can set rules for the length and characters (letters, numbers, and symbols) to make strong passwords.




import random
import string

password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print("Generated password:", password)

