'''

Q7. WAP to print star pattern. for n=3
    *     *     ***
   ***    **    * *
  *****   ***   ***

'''

#case 1

n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(" " * (n-i), end="") #end is used to print the star in same line
    print("*" * (2*i-1), end="") #2*i-1 is the odd number form
    print("")# it is used to add intentional blank line. print() is also used in this case.
print(" ")
#case 2


for i in range(1,n+1):
    print("*" * i, end="")
    print("")
print(" ")

#case 3

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")
print(" ")




