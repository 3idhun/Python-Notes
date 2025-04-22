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
