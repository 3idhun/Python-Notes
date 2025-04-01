'''

Q4. A file contains a word "Donkey" multiple times. You
    need to write a program to replace the word with
    "#####" by updating the same file.

'''


word = "Donkey"

with open("Donkee.txt", "r") as f:
    content = f.read()

content_new = content.replace("Donkey", "#####")

with open("Donkee.txt", "w") as f:
    f.write(content_new)


