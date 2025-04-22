#Map Example
l=[1,2,3,4,5]
square = lambda x:x*x
sqList = map(square, l)
print(list(sqList))
#[1, 4, 9, 16, 25]

#Filter Example
def even(n):
    if (n%2 == 0):
        return True
    return False
    
onlyEven = filter(even, l)
print(list(onlyEven))
#[2, 4]

#Reduce Example
from functools import reduce
def sum(a,b):
    return a + b
print(reduce(sum,l))
#15 i.e, 1+2+3+4+5
    