# password strength checker program
import re

#Password must be at least 8 character long
password = input("Enter Your Password: ")
if len(password) < 8:
    print("password must be at least 8 characters long.")
#Password must contain at least one uppercase letter.
elif not re.search("[A-Z]",  password):
    print("password must contain at least one uppercase letter.")
#Password must contain at least one lowercase letter.
elif not re.search("[a-z]", password):
         print("password must contain at least one lowercase letter.")
#Password must contain at least one number.
elif not re.search 8
    print("password must contain at least one number.")
else:
    print("password is strong")