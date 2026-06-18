#first thing we can do is find the length of objects using len keyword(note: will not suit for every object)

string = "Hello world"

print(len(string))
#will give me the legnth of Hello world

#print(len(4))
#the line above wont work

#
#Concatnation. This will help you undertand how ot merge strings
#

conc = 'hi'+' how'+ ' are you?'

print(conc)

#It is possible to get the exact letter or a string using these:
#note: python counts from 0 so to get p you need to put 0 instead of 1
print(string[3])

print(string[-1])
# the line above will give you the last letter. and adding a negative will count from the last.

#it is possible to get multiple letters at once like bellow:
print(string[0:2])
# the first number is telling python were to begin from and the second number tells when to stop
# this makes it so that it read "He"
# Leaving, an attribute null like this: print(D1:) it will continue to the end of the string.
print(conc)
print("-"*20)
D1 = "This is a string!"
print(len(D1))
print(D1+conc)
print(len(D1+conc))
print(D1[3])
print(D1[0:3])
print(D1[3:6])
print(D1[0:])

