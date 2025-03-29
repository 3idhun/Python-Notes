'''

Q1. WAP to read a text from the given file 'poem,txt' and find out whether it
    contains the word 'twinkle'.

'''

f=open("poem.txt")
content=f.read()
if "twinkle" in content:
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is present in the content")
f.close()



