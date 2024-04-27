'''>.Given an input string with the combination of the lower and upper 
case arrange characters in such a way that all lowercase letters should 
come first.
str1 = "PytHONStudy"
'''

string_in=input("Enter the string:")
str1=[]
str2=[]
for i in string_in:
    print(i)
    if i.islower()==True:
        str1.append(i)
    else:
        str2.append(i)


str1=''.join(str1)
str2="".join(str2)
print("String : ",str1+str2)
        
# print(str1)

