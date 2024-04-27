'''Perform following operations on both sets and find the output
Intersection, difference, union, difference, symmetric_difference, symmetric_difference_update, difference_update
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3=set1.intersection(set2)
print("Intersection:",set3)

set4=set2.difference(set1)
print("Difference for set2:",set4)

set4=set1.difference(set2)
print("Difference for set1:",set4)

set5=set1.union(set2)
print("Union",set5)

set6=set1.symmetric_difference(set2)
print("Symmetric difference:",set6)

set7=set1.symmetric_difference_update(set2)
# print("Symmetric difference update: ",set7)
print("Symmetric difference update:" ,set1)
print("Symmetric difference update:" ,set2)

set7=set2.symmetric_difference_update(set1)
# print("Symmetric difference update: ",set7)
print(set1)
print(set2)

set8=set1.difference_update(set2)
print(set1)
print(set2)

set8=set2.difference_update(set1)
print(set1)
print(set2)
