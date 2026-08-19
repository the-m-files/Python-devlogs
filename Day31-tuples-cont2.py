#-----------------------------#
#       ARG DEF FUNCTION      #
#-----------------------------#

#when defining functions it is possible that you might not know in advance how many arguments you might need, so this elaborate solution exists:

def takestuff(*args):
    print(type(args))
    print(args)

takestuff(1,4,5,6)
takestuff(2,4,4,"helo")

#as you can see it will take any arguemnts

#here is an implementation of this:

def my_max(*N):
    total = N[0]
    for number in N:
        if number > total:
            total = number
    return total

print(my_max(1,3,4,1,1,90))

#but what if you needed multiple args?
#just do this:

def my_max(setname, *N):
    print(setname+":")
    total = N[0]
    for number in N:
        if number > total:
            total = number
    return total

print(my_max("Hello", 1,3,4,1,1,90))
