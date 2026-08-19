#-----------------------------#
#           SORTED            #
#-----------------------------#

#the sorted function like is used for the lists can also be used for dictionaries, this will sort the keys from alpha numeric orders

flavors = {
    "chocolote":1.44,
    "Peanut butter":0.5,
    "mango":3.1,
    "dark frost":1.44
}

print(sorted(flavors))


#this will only sort the keys into an ordered list
print(sorted(flavors.keys()))

#this will only sort the values
print(sorted(flavors.values()))