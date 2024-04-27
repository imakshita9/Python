'''Try to change an element in the my_tuple created in Task 1. Note and comment on the result.
Explain why tuples are considered "immutable" data types.'''

tuple_1=(4,5,7)
tuple_1[2]=9
print(tuple_1)

#Tuples are immuatable meaning once value assigned can't be modified
# isha@isha:~/Python_Assign4$ python3 q7.py
# Traceback (most recent call last):
#   File "q7.py", line 5, in <module>
#     tuple_1[2]=9
# TypeError: 'tuple' object does not support item assignment