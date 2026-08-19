#-----------------------------#
#             DIR             #
#-----------------------------#

#the dir is similar to the help but will tell you what are all methods that can be used on an object

#print(dir([]))

#dunder is an acronym for "double underscores"
#the stuff with double  underscores are called dunder methods
#these methods are used by pythons and not meant for the devs

#the pretty much do the samething tho:

print("Hello".__len__())

print(len("Hello"))

print("-"*25)

print("in" in "intelligence")

print("intelligence".__contains__("in"))

print("-"*25)

print("non"+"agon")

print("non".__add__("agon"))

print("-"*25)


#-----------------------------#
#           TUPLES            #
#-----------------------------#

#tuples are the immutable versions of list with fixed legnths they can contain multiple types of data


#you can define these with these two ways:

trees = "Birch", "Oak", "Spruce", "Cherry", "Mangrove", "Acacia"

trees = ("Birch", "Oak", "Spruce", "Cherry", "Mangrove", "Acacia")


#but you may ask what will happen to an empty tuple or one that contains only one value

ex1 = ()

print(type(ex1))

ex2 = (1)

print(type(ex2))

ex3 = 1,

print(type(ex3))

#you can also use the similar tuple function like the list

print(tuple(["Hello", "Hi", "Goodbye"]))

#if you put an element without the list [] stuff it will make it so that each char is its own element in a tuple

print(tuple("abc"))