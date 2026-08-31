#-----------------------------#
#          DECORATORS         #
#-----------------------------#

#a decorator is a way of "decorating" or enhancing a regular function by passing it in another function.
#so it is basically a function that takes in a function and returns a function

#for example here is a way you can use one:

#this function is going to return a lot of prints. so it will clutter the terminal, to identify it easier we can add print("-"*25) after and before it.
def example():
    x = 10
    for i in range(1,x+1):
        print(x, "googoo")


#here is a better way though:

def cleaner(function):

    def add_stuff():
        print("-"*25)
        function()
        print("-"*25)

    return add_stuff

#so we can do this now:
retrun_value = cleaner(example)
retrun_value()

#since this is messy we can just do this:
cleaner(example)()


def greet():
    print("Hello!")

def decorator(func):
    def add_stuff():
        print("Starting...")
        func()
        print("Ending...")
    return add_stuff

greet1 = greet

decorator(greet1)()