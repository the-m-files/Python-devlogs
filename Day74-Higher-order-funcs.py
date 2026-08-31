#-----------------------------#
#   HIGHER ORDER FUNCTIONS 1  #
#-----------------------------#

#before we actually hit decorators we have to understand functions too are objects, so whatever you can do with other objects you can do it with funcs
#that means if you can store ints, you can store funcs. But it is a bit counter-intuitive so stick by

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

#the operation attribute expects a function as it's argument.
def calculate(operation: function, a:int, b:int):
    return operation(a,b)


#since functions are objects this code bellow should work:

#notice we aren't invoking add, we are just giving it(don't put parantheses)
#see how it works?
print(calculate(add, 1, 3))
print(add(1,3))
print(subtract(9.1,1))

#this means we can also store functions in lists

def add(*args):
    return sum(list(args))

def subtract(first, *args):
    result = first
    for num in args:
        result -= num
    return result

def divide(dividend, divisor):
    return dividend/divisor

def multiply(*args):
    values =list(args)
    total = 1
    for number in values:
        total *= number
    return total

options = [add, subtract, divide, multiply]

#subtracting
print(calculate(options[1], 1,2))

#adding
print(calculate(options[0], 1, 9))

#-----------------------------#
#       NESTED FUNCTIONS      #
#-----------------------------#

#it is possible to define functions inside functions, they are useful code designs to represent context over complexity

#here are the two ways we can do this:

#this way makes it so that the function is outside and can be used by the outside code
def one():
    return 1

def example_func():
    one()
    one()
    one()


#converting cups to pints:

def convert_gallons_to_cups(gallons):

    def gallons_to_quarts(gallons):
        print(f"{gallons} gallons converted to quarts")
        return gallons*4

    def quarts_to_pints(quarts):
        print(f"{quarts} quarts converted to pints")
        return quarts * 2

    def pints_to_cups(pints):
        print(f"{pints} pints converted to cups")

    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pints_to_cups(pints)
    return cups

#so speaking this should work:
convert_gallons_to_cups(3)
convert_gallons_to_cups(1)
print("-"*25)

#since the def functions are defined inside the function their namespace is limited and can't be used or called outside

#-----------------------------#
#  FUNCTIONS AS RETURN VALUES #
#-----------------------------#

#we have seen a lot of use cases for functions, but what about returning functions as return values?
#we will see that below even if it feels similar it is still new

def calculator(func):

    def add(a, b):
        return a+b

    def subtract(a, b):
        return a-b

    if func == "add":
        return add

    if func == "subtract":
        return subtract

#so know we can get a return value for add, but how do we even get add to work?
print(calculator("add"))

#well, we know that calculator("add") eventually simplifies into: add, so all we gotta do are put some paranthesis right?
print(calculator("add")(1,3))
print("-"*25)
#this eventually turns into print(add(1,3))

#so there you have it a function that returns functions, but we have something more fun to do.
#notice how this uses both? and is really simple yet complex?
def square(num):
    return num**2

def cube(num):
    return num**3

def multiplybyten(num):
    return num*10

operations = [square, cube, multiplybyten]

for operation in operations:
    print(operation(4))

    