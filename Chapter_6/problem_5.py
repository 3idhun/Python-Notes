
'''

Q5. WAP to which finds out whether a given name is present
    in the list or not.

'''

list_=[]
for _ in range(5):
    element = input("Enter the elements : ")
    list_.append(element) #dont equate this to a new name as this name will always be none value.
print("The list is : ", list_)

word_in_list=input("Enter the word : ")
if word_in_list in list_: #Donot use brackets unnecessarily.
    print("Present")
else:
    print("Not present")
