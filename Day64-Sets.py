#-----------------------------#
#             SETS            #
#-----------------------------#

#Okay, THIS ISN'T A TUPLE. This is a set, meaning it is unordered and doesn't have an index based storing system. also immutable
#but you can add and delete items

#the word actually comes from a mathematical study of data, meaning sets are in maths too.
#in maths sets are defined groups of objects that don't repeat.
#some examples are the set of quadrilaterals, the set of all real numbers and etc...


#this is how you define a set:

#this is the first way, easy and simple:
greetings = {"hello", "Hi", "Greetings", "Salutations"}

#notice how there are two ones but only one one remains in usingsetmethod variable?
#this can be used to convert other datastructures to sets too.
#notice you have to pass in a list into a set to print it out.
usingsetmethod = set([1,3,4,5,6,2,1])
print(usingsetmethod)
#to add something to a set, we can use the add method. But the order is not gaurenteed, it may change every time you run the program
greetings.add("welcome")

print(greetings)


#to add more than one item to set at a time, we can use update(yea, from dicts)
#here is an example:

setA = {
    "el1",
    "el2",
    "el3",
    "el4"
}

setB = {
    "el5",
    "el6",
    "el7"
}

setA.update(setB)
print(setA)
