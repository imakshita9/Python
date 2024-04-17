str1=input("Enter a name:")

#convert string in lower and upper case
print("String in lower case is:",str1.lower())
print("String in upper case is:",str1.upper())

#to check if string is in lower or upper case 
print("Is the string in lower case:",str1.islower())
print("Is the string in upper case:",str1.isupper())

#to check if the enterd string is end with y or not
print("Does string ends with y - True or False: ",str1.endswith('y'))

#find a specific word's index no of a character or word. 
print("Index no. of a character or word is: ",str1.index('s'))

#find total counts of a specific word in given string.
print("count of a character or word is: ",str1.count('a'))