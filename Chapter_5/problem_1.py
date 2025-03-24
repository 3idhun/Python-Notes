'''

Q1. WAP to create a dictionary of Hindi words with values as their English
    translation. Provide user with an option to look it up!

'''

words={
    "madad":"help",
    "garam":"hot",
    "kursi":"chair"
}

word=input("Enter the hindi word: ")
print(words[word])

'''

Dictionary is mutable, indexed. to create a dictionary, name{} is used
but for creating a set, name() is used.

The purpose of creating dictionary is that, to be data efficient, by making
it list can take more data which depletes the efficiency of the code.

'''