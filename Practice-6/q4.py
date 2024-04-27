'''Write a python program read data from file productdata.txt, copy all the lines starting with 12 and ending with 0 in file myproduct.txt
(use regular expression ^12.*0$)'''


import re
with open ("productdata.txt","r") as f:
    for i in f :
        contents=i.strip()
        if re.match(r"^12.*0$",contents):
            with open("myproduct.txt","a")as f1:
                f1.write(contents+"\n")
            print(contents)