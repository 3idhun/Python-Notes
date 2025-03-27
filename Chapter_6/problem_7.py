
'''

Q7. WAP to find out whether a given post is
    talking about "Midhun" or not.

'''

post_ = input("Enter the post : ")
lowercase_post = post_.lower() #converting the input to lowercase.

if "midhun" in lowercase_post:
    print("The post is about Midhun")
else:
    print("The post is not about Midhun")


'''

To check whether a keyword is present in the paragraph
always convert to either lower or uppercase.

'''