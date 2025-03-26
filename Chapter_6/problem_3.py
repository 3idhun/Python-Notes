
'''

Q3. A spam comment is defined as a text containing following keywords:
    "Make a lot of money", "but now", "subscribe this", "click this". Write
    a program to detect these spams.

'''

comment_=input("Enter the comment :")
for _ in comment_:
    if ("Make a lot of money" or "buy now" or "subscribe this" or "click this"):
        print("The comment is spam")
    else:
        print("The comment is not spam")