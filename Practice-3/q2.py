'''A pangram is a sentence that contains all the letters of the English alphabet at least once, for
example: The quick brown fox, jumps over the lazy dog!!!!.
Your task here is to write a python progra to check a
sentence to see if it is a pangram or not.'''

str1=input('Enter any string: ')

str2='abcdefghijklmnopqrstuvwxyz'

str1=str1.lower()
found=0

for i in str2:
    if i in str1:
        found = 1
    else:
        found = 0

if(found == 1):
    print('Pangram')
else:
    print('Not a pangram')
