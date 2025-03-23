'''

Q2. WAP to fill in a letter template given below with name and date.
    Dear <Name>,
    You are selected!
    <Date>

'''

letter='''Dear <Name>,
    You are selected!
    <Date>'''

print(letter.replace("<Name>", "Midhun").replace("<Date>", "11 February 2002"))

''' 

Triple Quotes are also used to create multiple line strings, ".replace" is used to replace the elements in the paragraph.

'''
