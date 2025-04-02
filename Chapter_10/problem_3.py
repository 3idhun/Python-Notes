'''

Q3. Create a class with a class attribute a; create an object from it
    and set 'a' directly using a=0. Does this change the class attribute.

'''



class Demo:
    a=4

o = Demo() #prints the class attribute because instance attribute is not present
print(o.a)
o.a = 0 # instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present
print(Demo.a)
