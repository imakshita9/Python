'''>.Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String
Given:
str1 = "RakeshzipPetabb"
Output
zip
str2 = "JazzbonAyxx"
Output
bon'''

str1="RakeshzipRoshan"
size_str=len(str1)
middle=int((size_str)/2)

print("middle three characters:",str1[middle-1:middle+2])

str2=input("Enter the string of odd length: ")
size_str2=len(str2)
middle1=int(size_str2/2)
print("middle three characters:",str2[middle1-1:middle1+2])


