#-----------------------------#
#      DICT COMPREHENSION     #
#-----------------------------#

#this is like list comprehenstion but for dictionaries

timestwo = {1:2, 2:4, 3:6, 4:8}

timesthree = {val: val*3 for val in timestwo.values()}

print(timesthree)

#now what if we try to implement if conditionals?

#this is how you will do it:
#notice you can also combine these two into dicts and lists

tempsacrosscity = {"Denver":45, "Colorado Springs":55, "Nome":-12, "Death valley":103, "Seattle":70}

tempsabovex = [city for city, temp in tempsacrosscity.items() if temp >=50]
print(tempsabovex)

#here is how you will do this for dictionaries
tempsabovex = {city: temp for city, temp in tempsacrosscity.items() if temp >=50}

print(tempsabovex)


#here is an example that doesn't use this:
squares = {}

for x in range(5):
    squares[x] = x * x

print(squares)

#here is an example that does use this:
squares = {x: x * x for x in range(5)}

print(squares)

#here is the gist of how it is split:
#squares = {x: x * x for x in range(5)}
#the x: part is the key
#everything after is used to calculate the vavlue

#here is an example that doesn't uses strings:

names = ["Alex", "Bob", "Charlie"]

name_lengths = {name: len(name) for name in names}

print(name_lengths)

#now lets make this a bit complex by adding an if condition

numbers = {x: x ** 2 for x in range(10) if x % 2 == 0}

print(numbers)

#notice: the if condition will make it so hat it will only add it to the numbers list if it is true(it will only run the range function)



