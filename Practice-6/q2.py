'''file "data.txt" contains following data
999-999-3567
789 456 7896
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
192.168.80.163
10.208.54.155
172.168.24.153
8.8.8.8

a. print IPv4 addresses from above file
b. print email ids only
c. print websites only.'''

import re
ip_list=[]
email_list=[]
website_list=[]

with open ("data.txt",'r') as f:
    for i in f :
        contents = i.strip()
        
        if re.match(r"^(\d{1,3}\.){3}(\d{1,3})$",contents):             #(\d{1,3}\.){3}= (\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)
            ip_list.append(contents)

        elif re.match(r"^[a-zA-Z0-9-.]+@[a-z-]+\.[a-z]+$",contents):
            email_list.append(contents)

        elif re.match(r"^(http|https)(://)(|www\.)[a-zA-Z]+\.[a-z]+$",contents):
            website_list.append(contents)

    print(ip_list)
    print(email_list)
    print(website_list)

