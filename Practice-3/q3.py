''' write a program to swap to numbers. (Do not use third variable'''

num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))

print("Before swapping value of num1 is:",num1)
print("Before swapping value of num2 is:",num2)
num1,num2=num2,num1
print("After swapping value of num1 is:",num1)
print("After swapping value of num2 is:",num2)