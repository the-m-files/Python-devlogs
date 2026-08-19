#-----------------------------#
#          DICTIONARY         #
#-----------------------------#

#dictonarys are like the books but have keys that you can use to retrieve data.
#they are mutable data structures that have values and keys.

#notice: keys are unique but values can be duplicates and keys are always immutable, the values however cabe any data type
#here is how to create a dictinary:

#the rice is the key and the price is the value.
#you can have the same price but not the same item.
#if you have the same item it will simplytake the value of the key that you declared the last.
menu = {
    "Rice":3.5,
    "Meat":5.99,
    "Milk": 2.99, 
    "Oranges":1, 
    "Kiwi": 3.5  
        }

print(len(menu))

#to get values from the list you can use the key
print(menu["Rice"])

#note you cant use the value:
#print(menu[3.5])


#NOTICE: this is not an ordered data structure. just because rice is in top it will not be evaluated first.


#you can even use lists:

school = {
    "class1":["Jamba", "Oonga bunga", "Cratos", "browser"],
    "class2":["Grunch", "Grug", "Bugrick", "Doodey"],
    "class3":["Poodey", "Dugrick", "xX--Sob--Xx", "lobbey"]
}

print(school["class2"])

#-----------------------------#
#             GET             #
#-----------------------------#

#the get method is an alternative for getting a value using a key

print(school.get("class2"))

#but you may ask what if the key doesn't exist well wont it crash?

#then you can set it so that it will return a different value

print(school.get("class35", ["ungo", "dingo", "bingo"]))
print("-"*25)
#-----------------------------#
#             ADD             #
#-----------------------------#

#to add a key pair value to a list in python you can follow this framework: dictname[key] = value
#so that it would show up something like this: dictname = {key:value}

coords = {}

coords[1] = 0

print(coords)

user_info = {"name": "Alice"}
user_info["age"] = 30  # Adds a single key-value pair

print(user_info)
