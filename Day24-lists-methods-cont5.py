#-----------------------------#
#            COPY             #
#-----------------------------#

#this copy method lets you copy a shallow copy of a list. This means that it wont work for lists inside lists, or other complex data structures

words = ["Hello", "Starve", "Great", "War", "Will", "I"]

backup = words.copy()

print(backup)

#since these two different lists are separate we can alter one without the other changing

#-----------------------------#
#            SPLIT            #
#-----------------------------#

#the split method will split up a string into multiple elements in a list with a delimiter

name = "Stan Lee Gee"

print(name.split(" "))


#as you can see, the delimiter was the space. it seperated it and put them in a list
#you can also tell python how many times to split a string 

jargon = "Comman, Altnam, Priosin, Kilotor, Komma, Grandiaroz"

print(jargon.split(", ", 2))

#Vocab: the second argument is called maxsplit

#-----------------------------#
#             JOIN            #
#-----------------------------#

stringing = ["Slow", "Glow", "Of", "Direction", "Breaks", "Souls"]

print(" ".join(stringing))

print(", ".join(stringing))

#as you could have seen; the join function will take a list and join it together with whatever you give it to put inbetween
#it is like the inverse of split.

test = ["cater", "pil", "", "er"]

print(" ".join(test))