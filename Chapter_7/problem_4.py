
'''

Q4. WAP to find a given number is prime or not.

'''

number = int(input("Enter the number: "))

if number == 1: #also use number < 2
    print("The number is neither prime nor composite.")
else:
    for i in range(2, number):
        if number % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.") #using else in down of if loop creates 3 output saying the number is prime.
