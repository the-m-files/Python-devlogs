#-----------------------------#
#            COUNT            #
#-----------------------------#

#the count method lets you see how many of an element is there in each list

things = ["Cat", "Marshmallow", "Bars", "Car", "Cat", "cat"]

print(things.count("Cat"))
print(things.count("cat"))

#-----------------------------#
#            INDEX            #
#-----------------------------#

#the index method will give you the first occurence of an item in a list through the items index.

print(things.index("Cat"))

#it gives you a value error when it can't find it so use this:

if "Car" in things:
    print(things.index("Car"))