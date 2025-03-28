'''

Q7. WAP to remove a given word from a list and strip
    it at the same time.

'''


def rem(list_, word):
    n=[]
    for item in list_ :
        if not(item==word):
            n.append(item.strip(word))
    return n

list_ = ["Midhun","Shambu","Smijo","dhun"]
print(rem(list_,"dhun"))