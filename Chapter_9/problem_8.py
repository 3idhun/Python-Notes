'''

Q8. WAP to make a copy of a text file present in this folder.

'''

with open ("Donkee.txt") as f:
    content = f.read()

with open ("Donkee_copy.txt", "w") as f: #Don't forget w here.
    f.write(content)