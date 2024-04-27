# Take 3 numbers from user and print largest no.

n1=int(input('Enter n1: '))
n2=int(input('Enter n2: '))
n3=int(input('Enter n3: '))

if(n1 > n2) & (n1 > n3):
    print('Largest number is :',n1)

elif(n2 > n1) & (n2 > n3):
    print('Largest number is :',n2)
else:
    print('Largest number is :',n3)