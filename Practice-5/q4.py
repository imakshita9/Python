'''
Write a Python function called find_max_element that takes a list of numbers as input and returns the maximum element in the list.'''


def find_max_element():
    list1=[]
    n=int(input("Enter number of elements : "))
    for i in range(1,n):
        ele=int(input())
        list1.append(ele)
    
    print(list1)
    print("max element : ",max(list1))

find_max_element()