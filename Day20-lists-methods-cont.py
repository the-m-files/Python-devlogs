#-----------------------------#
#             POP             #
#-----------------------------#

#the pop method will let you remove one element from a list

fruits = ["apple", "banana", "candy", "durian"]

#we know that candy isn't a fruit so we remove it from the list
#the pop method needs an index for it to work
fruits.pop(2)

print(fruits)

#we also have to notice that the pop method actually returns the index. since it
#doesn't know what to do with it, it forgets it and deletes from the list

print(fruits.pop(2))

#notice how it returns durian even though it wasn't in the list
print(fruits)

#when you do not provide an index the pop method will remove the last elment fron a list

fruits = ["apple", "banana", "durian", "orange", "jackfruit"]

fruits.pop()

print(fruits)



#-----------------------------#
#     LIST COMPREHENSION      #
#-----------------------------#

#List comprehension is simply a shorter way of creating a list.

#Normal way:

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)

#Output:
#[0, 1, 2, 3, 4]

#The exact same thing can be written in one line.

numbers = [i for i in range(5)]

print(numbers)

#General format:

#[expression for variable in iterable]

#expression
#What gets added to the list.

#variable
#The temporary variable used in the loop.

#iterable
#Anything you can loop through.

#Example:

squares = [x * x for x in range(6)]

print(squares)

#Output:
#[0, 1, 4, 9, 16, 25]

#Here:
#x takes on the values:
#0, 1, 2, 3, 4, 5

#Each time:
#x * x
#is added to the list.

#You can also use if statements.

evens = [x for x in range(10) if x % 2 == 0]

print(evens)

#Output:
#[0, 2, 4, 6, 8]

#This means:
#"Loop through the numbers 0-9,
#but only add the even ones."

#You can even change strings.

names = ["john", "emma", "liam"]

capitalized = [name.capitalize() for name in names]

print(capitalized)

#Output:
#['John', 'Emma', 'Liam']

#NOTE:
#List comprehensions DO NOT do anything new.
#They are simply a shorter way of writing a for loop
#that creates a list.

#If you ever get confused,
#just write the normal for loop instead.

