'''Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
1. Find out how many students are in the list
2. Change Lisa’s favourite colour
3. Remove 'Jenny' and her favourite colour
4. Sort and print students and their favourite colours alphabetically by name
5. Sort and print students and their favourite colours alphabetically by Student's name'''

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print("original dictionary: ",people)
#Find out how many students are in the list
len_1=len(people)
print("Total number of students in dictionary are : ",len_1)

#Change Lisa’s favourite colour
colour=input("Enter the new colour for Lisa: ")
people["Lisa"]=colour
print("New value for Lisa is:",people)

#Remove 'Jenny' and her favourite colour
del people["Jenny"]
print("Updated dictionary after removing Jenny is:",people)

#Sort and print students and their favourite colours alphabetically by name
a=sorted(people)
print("Dictionary in sorted manner according to name is: ",a)
# print(people)

#Sort and print students and their favourite colours alphabetically by value
sort_value=sorted(people.items(),key=lambda items:items[1])
print(sort_value)
dict_2=dict(sort_value)
print("Dictionary in sorted manner according to colour is:",dict_2)