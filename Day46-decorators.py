#-----------------------------#
#          DECORATORS         #
#-----------------------------#

#a decorator is a design pattern used to modify or extend the behavior of a function or method without changing its actual
#source code

import time

#notice how this function is messy because it is doing two things and is modifying the actual function?
#sometimes you don't want the time
#what if you want to do this for another function?

def brewtea():
    starttime = time.time()
    time.sleep(1)
    print("tea is ready")
    endtime = time.time()
    print(f"it took {endtime-starttime} seconds to brew your tea")

brewtea()


#here is that same function but using a decorator

def timeit(func):

    def wrapper():
        starttime = time.time()

        func()

        endtime = time.time()
        print(f"it took {endtime-starttime} seconds to run")

    return wrapper


#now we can use our decorator on our function

@timeit
def brewtea():
    time.sleep(1)
    print("tea is ready")

brewtea()


#notice that we did not have to change the actual brewtea function
#the decorator added the timing functionality to it


#this:

@timeit
def brewtea():
    time.sleep(1)
    print("tea is ready")


#is basically the same as doing this:

def brewtea():
    time.sleep(1)
    print("tea is ready")

brewtea = timeit(brewtea)


#the @timeit is just a cleaner way of applying the decorator


#now let's make another function

@timeit
def makecoffee():
    time.sleep(2)
    print("coffee is ready")

makecoffee()


#notice how we can reuse the same decorator
#we don't have to copy the timing code into every function


#the basic structure of a decorator looks like this:

def decorator(function):

    def wrapper():
        #code that runs before the function

        function()

        #code that runs after the function

    return wrapper


#then we can use it like this:

@decorator
def myfunction():
    print("hello")

myfunction()


#the decorator takes our original function
#then it creates a new function called wrapper
#the wrapper adds extra behavior around our original function
#finally, the decorator returns the wrapper function


#one problem with our decorator is that it only works with functions
#that don't need any arguments

#for example, this would not work correctly:

@timeit
def greet(name):
    print("hello", name)


#greet("Alex")


#we can fix this by allowing our wrapper to accept arguments

def timeit(func):

    def wrapper(*args, **kwargs):
        starttime = time.time()

        func(*args, **kwargs)

        endtime = time.time()
        print(f"it took {endtime-starttime} seconds to run")

    return wrapper


#now our decorator can work with functions that have arguments

@timeit
def greet(name):
    print("hello", name)

greet("Alex")


#*args allows us to pass any number of positional arguments
#**kwargs allows us to pass any number of keyword arguments


#here is another example

def announce(func):

    def wrapper(*args, **kwargs):
        print("starting function")

        func(*args, **kwargs)

        print("function finished")

    return wrapper


@announce
def sayhello(name):
    print("hello", name)

sayhello("Alex")


#the decorator added code before and after the function
#without changing the actual sayhello function


#the gist of decorators:

#def decorator(function):
#
#    def wrapper(*args, **kwargs):
#        #extra code
#
#        function(*args, **kwargs)
#
#        #extra code
#
#    return wrapper


#then use it like this:

#@decorator
#def myfunction():
#    print("hello")


#decorators are especially useful when you want to add the same
#functionality to many different functions

#for example:
#timing functions
#logging
#checking permissions
#caching
#validating information

#you will see decorators a lot when working with frameworks
#such as FastAPI

#for example, FastAPI uses decorators like this:

#@app.get("/")
#def home():
#    return {"message": "Hello World"}

#the decorator tells FastAPI what should happen
#when someone sends a GET request to the "/" URL