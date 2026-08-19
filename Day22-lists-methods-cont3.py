#-----------------------------#
#          REVERSED           #
#-----------------------------#

#the reverse function is like what it says. it will reverse the elements of  alist

letters = ["a", "b" "c"]

letters.reverse()

print(letters)

#-----------------------------#
#             SORT            #
#-----------------------------#

scores = [60, 63, 71, 80, 90, 40, 23, 50]

scores.sort()

print(scores)

names = ["Kay", "Jay", "May", "Trey", "Larry", "Chingusmungus"]

names.sort()

print(names)

#as you could have seen this is a really useful method. it will alphabetize and arrange numbers from smallest to greatest
#you can combine multiple sentences

#NOTE: the capital letters will always be sorted first.

#since these methods change this list from the core their originla structures can be lost
#to overcome this we can use the sorted() function

names = ["Kay", "Jay", "May", "Trey", "Larry", "Chingusmungus"]

print(sorted(names))

print(names)

