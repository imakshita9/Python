# validate email addresses in Python.

import re
email=input("Enter the email address : ")

if re.match(r'^([a-zA-Z0-9])*@([a-z])*\.([a-z])+$',email):
    print("Valid email")

else:
    print("Inavlid email")
