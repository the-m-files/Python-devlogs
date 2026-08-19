#-----------------------------#
#             DEL             #
#-----------------------------#

#this is similar to the pop method but can delete slices of strings

stuff = ["cookie", "sock", "doormat", "window", "pin", "frame", "television"]

del stuff[1]

print(stuff)

del stuff[3:5]

print(stuff)

#you can also use negative indexes too

#-----------------------------#
#           REMOVE            #
#-----------------------------#
games = ["soccer", "swimming", "basketball", "limbo", "Football"]

#the remove function will remove the item you say to remove from a list

games.remove("soccer")
print(games)

#when there are multiple occurences it will only remove the first one
#when it can not find it it will return a value error