'''

Q10. WAP to print multiplication table of n using for loops in
     reversed order

'''

number = int(input("Enter the number: "))
i=0
for i in range (1, number+1):
    print(f"{number} x {number+1-i}= {number*(number+1-i)}")

