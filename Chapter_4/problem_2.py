'''

Q2. WAP to accept marks of 6 students and display them in a sorted manner.

'''

marks=[]

f1=int(input("enter the  marks here = "))
marks.append(f1)
f2=int(input("enter the  marks here = "))
marks.append(f2)
f3=int(input("enter the  marks here = "))
marks.append(f3)
f4=int(input("enter the  marks here = "))
marks.append(f4)
f5=int(input("enter the  marks here = "))
marks.append(f5)
f6=int(input("enter the  marks here = "))
marks.append(f6)
f7=int(input("enter the  marks here = "))
marks.append(f7)

marks.sort()

print(marks)

'''

Always remember to convert string to integer before 
getting sorted. Alt+j is used to select multiple occuances
in pycharm where we can modify all same words at once. Same 
option is present in VS code.

Tuple cannot be modified and we say it as immutable.


'''