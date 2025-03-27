
'''

Q3. A spam comment is defined as a text containing following keywords:
    "Make a lot of money", "but now", "subscribe this", "click this". Write
    a program to detect these spams.

'''



p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=input("Enter the comment: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("The comment is spam")
else:
    print("The comment is not spam")

#using for loop


'''comment_=input("Enter the comment :")
for _ in comment_:
    if ("Make a lot of money" or "buy now" or "subscribe this" or "click this"):
        print("The comment is spam")
    else:
        print("The comment is not spam")'''


'''

We can use "in" to check whether the string is present in the given input. 

'''
