# Write a program to print the multiplication table of a given number by user.

num=int(input("Enter the number"))

print(f"Table of {num}")
for i in range(1,11):
    print(f"{num} x {i} =",i*num)
    