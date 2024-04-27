#Write a python program to accept mobile number and validate it. it should contain exactly 10 digits.

import re
mob_no=input("Enter the mobile number : ")

if re.match(r'^[0-9]{10}$',mob_no):
    print("valid")
else:
    print("not valid")

