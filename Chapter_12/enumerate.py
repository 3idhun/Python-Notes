l = [3,513,53,535]

'''index = 0 
for item in l:
    print(f"The item at index {index} is {item}")
    index += 1'''
    
'''
The item at index 0 is 3
The item at index 1 is 513
The item at index 2 is 53
The item at index 3 is 535
'''

#same code can be written using enumerate function
for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")

