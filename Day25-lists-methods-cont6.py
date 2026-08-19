#-----------------------------#
#             ZIP             #
#-----------------------------#

#the zip object is a generator type object. it is like a tuples and zips multiple lists

monday = ["Go to work", "Come home", "sleep"]
tuesday = ["Go to bank", "Go to work", "Come home", "Sleep"]
wednsday = ["Go to Bakery", "Buy coffee", "Go to work", "Come home", "Sleep"]

print(zip(monday, tuesday, wednsday))
print(type(zip(monday, tuesday, wednsday)))
print(list(zip(monday, tuesday, wednsday)))

#NOTE: when you zip this it takes first element of monday, first element of tuesday
# and first element of wednsday and adds them together in a tuple and does this until
# it hits a remainder.

