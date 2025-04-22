'''
Q3. A list contains the multiplication table of 7, write a program to convert it to a vertical string of same numbers.
'''

table = [str(7*i) for i in range(1,11)]
s="\n".join(table)
print(s)

'''
7
14
21
28
35
42
49
56
63
70
'''