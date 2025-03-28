'''

Q. WAP using recursion to find factorial of n numbers.

'''
from fontTools.misc.cython import returns


def factorial(n):
    if n==1:
        return 1
    return  n * factorial(n-1) #Here a loop is created

print(factorial(5))

'''

In recursion a loop is created, in which 
if we want the factorial of 5 then,
5 x 4! then goes to loop with 4 x 3! which repeats until 1.

Always declare a base condition like n==1: for avoiding infinite values or error in code
which may crash the program

'''