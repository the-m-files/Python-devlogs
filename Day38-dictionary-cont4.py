#-----------------------------#
#             POP             #
#-----------------------------#

#the pop method like in the lists section is really similar to the one in dictionaries.
#NOTICE: you can save whatever you deleted last using the pop method and assiging it to a variable

groceries = {
    "Tomatoes":10,
    "Onion":3,
    "Garlic":2,
    "Pasta":2,
    "Lettuce":1,
    "Chicken":1,
    "Apples":-4
}

#notice how we do not use the index? because as explained the dictionary isn't organized in linear order. just by keys
groceries.pop("Apples")

print(groceries)

#warning: to not get errors use the in function before using pop like below:

if "Lolipop" in groceries:
    groceries.pop("Lolipop")

    print(groceries)

#-----------------------------#
#           CLEAR             #
#-----------------------------#

#the clear method clears all elements in a dictionary

dummdict = {
    "adfae":42,
    "q45q3":53,
    "dkfjk":24,
    "sdfj":4
}

dummdict.clear()

print(dummdict)

#-----------------------------#
#           UPDATE            #
#-----------------------------#

#this is like the extend method for lists 

dict1 = {
    "dflkaj":1,
    "afk":3
}

dict2 = {
    "dfae":3,
    "fkdja":4
}

dict1.update(dict2)

print(dict1)
