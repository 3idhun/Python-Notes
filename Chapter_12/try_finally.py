def main():
    try:
        a = int(input("hey, Enter a number:"))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("Hey I am inside of finally") #this gets executed whatever the condition is
        
main()

'''
Here using try and exeption does not breal the code.
Using global keyword makes the variable defaul
if we declare global a, a=13 we cant modify the value of a again.
