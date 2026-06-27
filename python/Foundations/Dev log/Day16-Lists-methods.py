

#-----------------------------#
#           REPLACE           #
#-----------------------------#

#the first way you can change a list is by re-assigning a new value to an existing index position:

animals = ["Kangaroo", "Giraffe", "Monkey", "Dolphin"]

animals[1] = "Lion"

#the line above will set "Giraffe" to "Lion" this is because we are assigning the first item at the index 1 to a new string:
print(animals)

animals[0] = "Rhino"
print(animals)

#just like how you can use negative values to get the last element of a list you can use it here too!
animals[-1] = "Donkey"
print(animals)

#WARNING: NEVER USE INDEX POSITIONS THAT DONT EXIST IN A LIST
print("-"*35)

#to replace an entire section of items with your own strings you can use something similar
#you can use smaller lists to give multiple elemets
Toys = ["Woody", "Buzz", "Jessie", "Bullseye", "Rex"]
print(Toys)

#Notice how Buzz and Jessie have been swapped with Hamm and Bo Beep?
Toys[1:3] = ["Hamm", "Bo Beep"]
print(Toys)

#When you only give two indexes but give three items python will wipe those two and stick the three in their place
Toys[1:3] = ["Hamm", "Bo Beep", "Aliens", "Forky"]
print(Toys)

print("-"*35)

#-----------------------------#
#             ADD             #
#-----------------------------#

shopping = ["Dresses", "Shoes", "Food"]

#to add something to the list we can use a method called append. Here is an example bellow:

shopping.append("Water")
print(shopping)

#note: Lists are mutable datastructures, so that means you don't have to do shopping = shopping.append("Water"). You are not making a new list that you have to assign it to the original.