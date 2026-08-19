#-----------------------------#
#            HELP             #
#-----------------------------#

#THE HELP FUNCTION IS OP IT WILL GIVE WHAT A FUNCTION DOES

#help(print)

#-----------------------------#
#             MAP             #
#-----------------------------#

#the map func will let you test a range of values to a given def function or built in ones

numbers = [1,3,4,5,6,23]

squares = [number **2 for number in numbers]

print(squares)

#as you could have seen that is one way to do this problem 
#the second way is this:

def square(number):
    return number ** 2

print(map(square, numbers))

#since this is returned as a generator object we have to use a for loop and print all values of it out or convert it to a list

print(list(map(square, numbers)))

#so the map function will ask for the def function and the range of numbers
#the first is the function and the second is the range

#here is an example that uses a built in function:
animals = ["Monkey", "Donkey", "Gorrilla", "Lion", "Antelope"]

print(list(map(len, animals)))


