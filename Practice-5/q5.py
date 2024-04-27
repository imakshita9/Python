'''Write a Python function called fibonacci_sequence that takes an integer n as input and returns a list containing the first n Fibonacci numbers. 
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.'''

def fibonacci_sequence():
    n=int(input("Enter the number upto which you have to print fibonacci series:"))
    first=0
    second=1
    print("0 1",end=" ")
    for num in range(1,n+1):
        add= first + second 
        print(add,end=" ")
        first = second
        second = add

fibonacci_sequence()