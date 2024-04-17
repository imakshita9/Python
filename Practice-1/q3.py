'''Write a Python program that does the following:

Takes two strings as input from the user.
Concatenates the two strings.
Prints the length of the concatenated string.
Prints the first character of the concatenated string.
Prints the last character of the concatenated string.
'''

str1=input("Enter string 1: ")
str2=input("Enter string 2: ")

str3=str1+" "+str2
print("Concatenation of two strings is:", str3)
print("Length of concatenated string : ",len(str3))

print("first character of the concatenated string:",str3[0])

print("last character of the concatenated string:",str3[-1])