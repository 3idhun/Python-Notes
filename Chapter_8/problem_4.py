'''

Q4. Write a recursive function to calculate the sum of
    first n natural numbers.

'''

def sum(n): #Here a function is declared
    if(n==1): # for recursion to not run infinitely, base condition should be declared
        return 1
    return sum(n-1) + n

print(sum(4))

'''

here, sum of first n numebers means
sum(n) = 1+2+3+4+n
i.e, sum(n) = 1+2+3+(n-1)+n
thus sum(n) = sum(n-1) + n

'''