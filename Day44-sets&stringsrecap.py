#-----------------------------#
#         REMOVEPREFIX        #
#-----------------------------#

#this will remove the first set of chars in a str.

name = "John Depe"

lastname = name.removeprefix("John ")

print(lastname)

#this will only work for strings

#-----------------------------#
#         REMOVESUFFIX        #
#-----------------------------#

#this will remove the last set of chars in a str

name = "John Depe"

firstname = name.removesuffix(" Depe")

print(firstname)

print("-"*25)


#-----------------------------#
#             SETS            #
#-----------------------------#

#Set items are unordered, unchangeable, and do not allow duplicate values.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#Note: like vice versa, 0 and flase are considered the same
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#to get the legnth of a set, we can use the len function
print(len(thisset))

#to use the set constructor we can follow this anatomy:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
print("-"*25)
for element in thisset:
    print(element)

#notice: once a set is created you cannot change the order of elements but you can add new elements

#to add an element to a set we can look at the following methods below

#1.) the add method is for the sets class and can be used to add elements to a set

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#2.) the update method, as it worked for lists, dict, tuples this also works for the set:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#note: this doesn't have to be just sets to sets or lists to lists, this can mix these types:

thisset = {"apple", "banana", "cherry"}
tropical = ["pineapple", "mango", "papaya"]

thisset.update(tropical)

print(thisset)

#to remove an element from a set we can use one of the following methods below:

#1.) remove:

thisset = {"pineapple", "mango", "papaya"}

thisset.remove("papaya")

print(thisset)

#2.) discard

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#note: the difference between discard and remove is that when remove cant find something in a set it will raise an error but discard wont.

#3.) pop:

#you may be asking, wait. doesn't pop need an index position to remove an element? and doesn't sets have no indexes?
#well, in that case we can use a small variable to overcome that problem like this bellow:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#notice, each time this will remove a random element in a set. not what you want

#4.) clear:

#as you can see this will clear all the elments in a set

thisset = {"apple", "banana", "cherry"}

x = thisset.clear()
print(thisset)

#5.) the del keyword will erase the set completely(the clear set it to empty)

thisset = {"apple", "banana", "cherry"}

del thisset

#it even deletes the variable so don't run it:
#print(thisset)

