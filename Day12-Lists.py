#--------------------------------------#
#           LISTS STARTS HERE          #
#--------------------------------------#

#lists are arrays. in short they are basically like a grocery list containing multiple values in a long line.
#here are the ways to define a list:

empty = []
empty = list()

words = ["hello", "you", "can", "add"]

#You can arrange lists like this if they get long.
words2 = [
    "hello",
    "hi",
    "i",
    "am",
    "python",
]

#Notice, some function behave differentaly with lists. for example the len function:
print(len("Proton"))
print(len(words))

#You can use the in keyword from the strings lesson to figure out if an item exists in a list
print("last" in "chloroplast")
print("glass" in "plexiglass")
print("hi" in words2)

#Like the getting the indexes of strings, we can get the index items of items ina list almost similaryly:
#note: it starts from 0
print("a" in words2[3])
print(words2[3])
print(words2[1])
print(words[2])
print("-"*20)
#you can actually take individual letters from a list by using this method:
#this will take the 3rd letter from the 0th(1st) item in a list
print(words2[0][3])

#Like strings we can get the last value by inputting negative values:
print(words[-1])

#this one gives us the second to last value:
print(words[-2])

