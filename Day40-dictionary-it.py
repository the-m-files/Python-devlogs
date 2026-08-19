#-----------------------------#
#         ITERATION           #
#-----------------------------#

#this is a different unit from the last 5 lessons about dictionaries these are about iteration and they are about basics
#first is iterating over a for loop:

meals = {
    "Chicken Nuggets":4.99,
    "Cheese Burger":9.5,
    "Double Cheese Burger":21.99,
    "Apple cider":3.99
}

#notice: when doing this meal can be anything but it will represent the key. not the entire value as a whole.
for meal in meals:
    print(f"{meal} is ${meals[meal]}")


print("-"*25)
#here  is another example:

votes = {
    "Chocolate":234,
    "Chocoloate chip":219,
    "Vanilla":187,
    "Cake":97,
    "Cookies":1
}

for flavor in votes:
    print(f"{flavor} has {votes[flavor]} votes")
print("-"*25)
    
#-----------------------------#
#            ITEMS            #
#-----------------------------#

#the items value is an iteratable object that is basically will return the entire key value pair instead of only the keys like above
#the items method will return the key and value pairs as tuples and will basically unpack them in the for loop like bellow:

#notice how we have done a much elegent solution for the problem above?
votes = {
    "Chocolate":234,
    "Chocoloate chip":219,
    "Vanilla":187,
    "Cake":97,
    "Cookies":1
}

for flavor, vote in votes.items():
    print(f"{flavor} has {vote} votes")

print("-"*25)

#this is how they will look like in unpacked form
print(tuple(votes.items()))

#-----------------------------#
#             KEYS            #
#-----------------------------#

#the keys is like the items function but will only return the keys
print("-"*25)
xycoords = {
    1:3,
    3:3,
    0:4,
    5:5
}

for x in xycoords.keys():
    print(f"the x coord is {x}")

print("-"*25)
#these also have another use:

print(2 in xycoords.keys())

print(list(xycoords.keys()))

#-----------------------------#
#           VALUES            #
#-----------------------------#

#Values are like exactly the keys but return the values. they work nearly identicle hence see the comparision
print("-"*25)
xycoords = {
    1:3,
    3:3,
    0:4,
    5:5
}

for y in xycoords.values():
    print(f"the y coord is {y}")

print("-"*25)
#these also have another use:

print(2 in xycoords.values())

print(list(xycoords.values()))