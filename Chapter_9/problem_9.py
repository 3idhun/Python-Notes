'''

Q9. WAP to find out whether a file is identical &
    matches the content of another file.

'''

with open("Donkee.txt") as f:
    first_file_content=f.read()

with open("Donkee_copy.txt") as f:
    second_file_content=f.read()

if first_file_content==second_file_content:
    print("Yes, These files are identical")
else:
    print("No, These files are not identical")
