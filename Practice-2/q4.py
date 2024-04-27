'''Write a Python program that takes a number n as input from the user and prints two lists: 
one containing all the even numbers   to n and the other containing all the odd numbers  to n." (Using List Comprehension)

'''
lis=[]
n = int(input("enter any number : "))
for i in range(n):
    var1=input(f"input {i} element:")
    lis.append(var1)

print(lis)

# even_numbers = list(range(2, n, 2))
# print(even_numbers)
l1=[k for k in range(2,n,2)]
print("Even numbers are:",l1)



# odd_numbers = list(range(1,n,2))
# print(odd_numbers)

l2=[j for j in range(1,n+1,2)]
print("Odd numbers are: ",l2)
