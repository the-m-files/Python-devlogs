#Today we are continueing our last lesson. and learning about mostly two things. The "return" keyword and default function values

#to understand why we need the return value here is a good example:

def add(a,b):
    print(a+b)

print(add(1,1))

# when you runn this you could see that it returned "none"
#but running the same function bellow will give you 1+1

def add(a,b):
    return a+b
print(add(1,1))

# in python if you don't give a value for every attribute to a function it will raise errors. to stop this we can set a default value like this:

def multiply(a=1,b=1):
    return a*b

print(multiply(3))

#Bonus!
#It is also possible to specify the type of an attribute to a function,
#look bellow for to see how it is done

def repeat_str(word, times):
    return word*times

print(repeat_str('Hello world', 4))

#the function above is practically just a reg function

def repeat_str(word:str, times:int) -> str:
    return word*times
print(repeat_str("Classified_str", 4))

# by adding ":" after the attrubute you can specify what type of value you are expecting and adding -> lets you decide what type of value the function will give back