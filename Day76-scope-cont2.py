#-----------------------------#
#           CLOSURES          #
#-----------------------------#

#a nested function that remembers and retains access to variables from its
#enclosing (outer) scope even after the outer function has completely finished executing

#this is kind of a complex idea, but it is simply returning a function and saving it in a variable to call it later:


def make_greeter(person_name):

    def greet():
        name = person_name
        return f"Hello {name}!"

    return greet

def make_secret(message):

    def secret_closure():
        return message

    return secret_closure


def make_counter():
    start = 0
    def counter():
        nonlocal start
        start +=1
        return start

    return counter

counter1 = make_counter()

print(counter1())
print(counter1())
print(counter1())
print(counter1())



#-----------------------------#
#           NONLOCAL          #
#-----------------------------#

#nonlocal allows an inner function to MODIFY a variable
#from its enclosing (outer) function

#without nonlocal, Python would treat "start" as a new
#local variable inside counter()

def make_counter():

    start = 0

    def counter():
        nonlocal start
        start += 1
        return start

    return counter


counter1 = make_counter()

print(counter1())
print(counter1())
print(counter1())
print(counter1())

#1
#2
#3
#4


#-----------------------------#
#     MULTIPLE CLOSURES       #
#-----------------------------#

#each time the outer function is called,
#a new closure with its own remembered variable is created

counter1 = make_counter()
counter2 = make_counter()

print(counter1())
print(counter1())

print(counter2())
print(counter2())

print(counter1())
print("-"*25)
#1
#2
#1
#2
#3


#counter1 and counter2 have separate "start" variables
#
#counter1:
#start = 3
#
#counter2:
#start = 2

#-----------------------------#
#           GLOBAL            #
#-----------------------------#

#Global makes so that a variable can be used anywhere in the file, including directly inside nested functions without closures
#it is similar to nonlocal but it works at the file scale.

#here is an example:

#varaible:
number = 12

#a function to change number:

def change_number():
    number = 25 #this is actually creating a new variable called number inside this current scope and we are returning that variable.
    #an easier fix would be to do this: return number+1 and delete number = 25 above it.
    return number

print(change_number())
print(number)


#but here is a better solution:

def change_number():
    global number #global makes it so that it tell python that we are referencing the variable above, and not creating one
    #so that means whenever we do something to number it also changes it in the number variable above.
    number = 25
    return number

print(change_number())
print(number)

