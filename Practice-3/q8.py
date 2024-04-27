#Write a program to calculate the factorial of a given number

num=int(input("Enter the number"))
result=1
for i in range(1,num+1):
    result*=i

print(result)