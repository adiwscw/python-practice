#Password Strength Checker Program
import re

#Checking the strength
password = input("Enter Your Password. ")
if len(password) < 12:
    print("Password must be at least 12 characters long.")
elif not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
elif not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")
elif not re.search("[0-9]", password):
    print("Password must contain at least one digit.")
if not re.search("[!@#$%^&*(),.?\":{}|<>=]", password):
    print ("Password should contain at least one special character.")
else:
    print("Strong: Password meets the criteria.")