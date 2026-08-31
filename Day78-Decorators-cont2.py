#-----------------------------#
#            KWARGS           #
#-----------------------------#

#We already know what they are from previous lessons, they can take in any amount of positional arguemtns and put them inside a dictionary
#but the question is how do we use them inside decorators? The awnser is that they will let us use these with functions that take in stuff


#here is how a decorator works:
#1.) we create a higher order function and make it take a function as an argument
#2.) we store that function inside a variable and then call it inside another nested function within that function with some extra stuff
#3.) we finally then will return that nested function as a new object

#but this has a problem: this decorator can't take in any functions in as arguments that need attributes to be defined

#here is how it will look like:

#this decorator will check what the return value of a function is and print it:

def say_type(func):
    def inner(**kwargs):
        return_value = func(**kwargs)
        print(f"{type(return_value)}--->  ", end="")
        return return_value
    return inner

#this @, just means that it will run whenever we use this function
@say_type
def employee_email(name, fav_color):
    return f'{name}.{fav_color}@gmail.com'

print(employee_email(name="Trav", fav_color="Burple"))

#but now imaging what if we have another function that adds stuff
@say_type
def add(a, b):
    return a+b

print(add(a=1, b=4))

#so, yeah we have something super flexible, that will work for literally any function
#but notice we aren't actually running def add... function. we are running the decorator's inner function and just calling add() there.
#so it is a different function we are actually running
#this also means get your variables strait

#but what about *args

#-----------------------------#
#            ARGS             #
#-----------------------------#

#args are exactly like kwargs but instead of a dict they store it in a tuple
#and don't have to be said like a=1, b=3 or something like that and can be given directly with more flexibilty
#these are mostly supposed to be used with eachoter

def num_of_args(func):
    def inner(*args):
        # Use *args to unpack the tuple into individual arguments
        result = func(*args) 
        print(f"Number of arguments: {len(args)}")
        return result
    return inner

def subtract(a, b):
    return a - b

# 1. Pass the function itself to the decorator
decorated_subtract = num_of_args(subtract)

# 2. Pass the arguments when calling the decorated function
print(decorated_subtract(1, 3))

#so, when using both we can literally pass in any function.

