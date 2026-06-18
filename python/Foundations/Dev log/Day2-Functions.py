# To make a basic function you have to use the def keyword

#first you use the def then the name of the function and then paranthesises. you may give arguments in them but are not nescesary
#then you put the name of the function and whatever indented after are part of the function
#

def hello_world():
    print("Hello world")

#the function above will print hello world when ran you can use the "pass Keyword to silence a function"
hello_world()

#You can add parameters to a function. Parameters act like input function values/variables that your function will change.
#this parameter can be anything you want.

def p(text):
    print(text)

p("This is the p function")

def add(a,b):
    print(f"{a}+{b} is {a+b}")

add(3,5)
# you can also do this:
add(a=4, b=3)

print("genius"[:4])