#-----------------------------#
#           MODULES           #
#-----------------------------#

#modules are like being able to use functions/objects from other files. Great way to split up a big program into many files

#here is a simple set of functions that can do some arithmetic:

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

print(add(1,3,4,2,1))
print(subtract(3, 2 ,4 ,2))
print(multiply(3,4))

#this is obviously not the entire thing to see that please go check the modules folder above

#-----------------------------#
#           STRING            #
#-----------------------------#

#the string modules is a built in module that is in the python standard library(a library that comes pre-installed with the python files)
#it has a lot of useful stuff
import string

#prints all letters in the english alphabet(capitals and lower)
print(string.ascii_letters)

#prints all lower letts in english
print(string.ascii_lowercase)

#prints all upper case letters in english
print(string.ascii_uppercase)

#this prints all number chars
print(string.digits)

#this prints all printable chars, the space of line is actually /n
print(string.printable)

#this prints all punctuation
print(string.punctuation)

#similar to the title method we can capwords
print(string.capwords("akdfja is what i spam"))

#-----------------------------#
#             MATH            #
#-----------------------------#

#the math function lets you do a lot of math stuff
import math

#here is the ceil which will return the next biggest integer after the input:
print(math.ceil(4.5))
print(math.ceil(4.8))
print(math.ceil(4.00001))

#the floor is opposite of the ceil
print(math.floor(3.99))
print(math.floor(3.5))
print(math.floor(3.00001))

#and the sqrt is practically the square root
print(math.sqrt(16))
print(math.sqrt(982))

#and like for variables we can import the pi value
print(math.pi)

print(dir(math))