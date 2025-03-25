'''

Q1. WAP to find the greatest of four numbers entered by the user.

'''


#Using Conditional Loop like in video
a1 = input("Enter the first number: ")
a2 = input("Enter the second number: ")
a3 = input("Enter the third number: ")
a4 = input("Enter the fourth number: ")
if a1>a2 and a1>a3 and a1>a4:
    print(f"{a1} is the greatest number")
elif a2>a1 and a2>a3 and a2>a4:
    print(f"{a2} is the greatest number")
elif a3>a1 and a3>a2 and a3>a4:
    print(f"{a3} is the greatest number")
if a4>a1 and a4>a2 and a4>a3:
    print(f"{a4} is the greatest number")
else:
    print("The number is invalid")


#self program
'''
numbers=[]
a1 = input("Enter the number: ")
numbers.append(a1)
a2 = input("Enter the number: ")
numbers.append(a2)
a3 = input("Enter the number: ")
numbers.append(a3)
a4 = input("Enter the number: ")
numbers.append(a4)

print(numbers)
c=sorted(numbers)
print("The largest number is:", c[-1])

'''



#The above mentioned program can be also wriiten in this for loop form which is short

'''

numbers = [int(input("Enter the number: ")) for _ in range(4)]
print(numbers)
c=sorted(numbers)
print("The largest number is:", c[-1])

'''

''' 

The underscore in for loop can be used 
 _	                       Throwaway variable (e.g., in loops)
 _                         in the interpreter	Holds the last evaluated result
 x, _, y = (1, 2, 3)	   Ignore values during unpacking, out=1,3
 class_                    Used with temporary variables to prevent it from clashing with keywords.
 
 '''


