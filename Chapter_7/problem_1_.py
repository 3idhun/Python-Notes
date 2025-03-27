'''

Q1. WAP tp print the multiplication table of a following
    number.

'''

'''number=int(input("Enter the number : "))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")
    pass'''

#using while loop

number=int(input("Enter the number : "))
i=0
while (i<10):
    i+=1
    print(f"{number} x {i} = {number * i}")
    pass

'''

Always take the input as integer, the range 1,11 for
correct output of range 1-10

'''