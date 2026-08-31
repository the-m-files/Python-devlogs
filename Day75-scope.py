#-----------------------------#
#       SCOPE EXPLAINED       #
#-----------------------------#

#a scope in python is the namespace which variable share, python can have many namespaces across levels of nestedness.
#you can't use a variable in a lower nested level in a level above it but can use variables from higher levels lower.

#here are some usecases:

age = 12

def sayage():
    age = 10
    return age

#notice, there are actually two varaibles named age and each store a different value.
#you aren't changing the value of age from above but simply restoring one from below:

#so that is how these to will work:
print(age)
print(sayage())


#but then how does this work:

#well, first python searches for age in it's current namespace(local scope) and then if it didn't find it, it will look someplace else.
age = 12

#so this is the age from the main level:
def sayage():
    return age

print(age)
print(sayage())

#so here is a simple thing:

age = 12 # is a global variable

def sayage():
    age = 10 #and this age is a local variables
    return age


#-----------------------------#
#             LEGB            #
#-----------------------------#

#LEGB, is the rule python uses to search for a variable/constant in localscopes
#it stands for local, enclosing, global and built-in. it will search for that variable in that order and when it finds it, it will stop
#if it doesn't recongnize any of that(doesn't find it) it will return a notfound error.


#here is a small sample that will explain it to you:

def outer():
    x = 10

    def inner():
        x = 5
        return x

    return inner()

#so suppose what do you think will happen if we do this:
print(outer())

#well, the reason it returns 5 is because when python searches for x from line 60 it finds x = 5 in local scope so it just returns that
#and since outer returns whatever the return value of inner is it will print 5

#but suppose we remove the x = 5 from the inner:

def outer():
    x = 10

    def inner():

        return x

    return inner()

#this time it will return 10 because it didn't find it in the local scope so it searches up and finds x=10 so it returns that.
print(outer())


#and finally if we had already defined x outside of the function it will just use that(global level)

x = 15

def outer():

    def inner():

        return x

    return inner()

#so this time when invoking outer we get 15
print(outer())