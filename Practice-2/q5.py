# l1=[]
# for i in range(1,20,2):
#     l1.append(i)
# print(l1)

# l2=[x for x in range(2,21,2)]
# print(l2)
# l3=[x for x in range(2,21,2) if x % 3 == 0]
# print(l3)

# Write a Python program that uses list comprehension to generate a list of squares of numbers from 1 to 10.

squares = [value**2 for value in range(1, 11)]
print("Square of first 10 numbers are:",squares) 


# >.Write a Python program that uses list comprehension to generate a list of squares of odd numbers from 1 to 20.
square_odd=[x**2 for x in range(1,21,2)]
print("squares of odd numbers from 1 to 20:",square_odd)

# >.Write a Python program that uses list comprehension to generate a list of squares of even numbers from 1 to 20.
square_even=[y**2 for y in range(2,21,2)]
print("squares of even numbers from 1 to 20: ",square_even)