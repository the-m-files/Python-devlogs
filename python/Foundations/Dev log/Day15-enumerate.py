def sps(string, count=25):
    print(string*count)

#-----------------------------#
#          ENUMERATE          #
#-----------------------------#

#the enumerate is something close to the reversed() function, 
#It will ??? and give each element in the list an index number.

movies = ["Cars", "Wall-e", "Croods", "Moana", "Lion king"]

for index, film in enumerate(movies):
    print(f"{film} is number {index} in movies")
print("-"*30)
#since this prints from zero we can change this by adding this modification below:
#the start will tell python to start counting from where.
for index, film in enumerate(movies, start=1):
    print(f"{film} is number {index} in movies")

#-----------------------------#
#            RANGE            #
#-----------------------------#

#the range function is a keyword that is used with the for loop. It is good to generate a certain slice of numbers.
#for example the for loop below will output all numbers between 1 through ten(note:ten will not be included. it will be up to it).
for i in range(10):
    print(i)
sps("-", 25)
#you can tell range where to start by giving it an attribute before ten:
for i in range(0,10):
    print(i)
sps("-", 25)
#you can tell range how much to skip by too!:
for i in range(0,10,2):
    print(i)
sps("-")
#You can even go backwards! by decrementing like this:
for i in range(11, -1, -1):
    print(i)

#-----------------------------#
#            BREAK            #
#-----------------------------#

#the break keyword will stop whatever program from reaching its final conclusion when a certain conditions is met
#here is an example:
sps("-")
for i in range(1,10):
    print(i)
    if i >= 5:
        break
#see how we broke the run of the for loop using the condition?

#-----------------------------#
#           CONTINUE          #
#-----------------------------#

#the continue keyword is a keyword used for "for loops" to skip the current block
#See how the else block will skip the current code and ask the function to go to the
#next possible value? this is what the continue keyword is used for.
#this is complementry to the Break keyword
sps("-")
def add_sum_of_positives(listt):
    total = 0
    for i in listt:
        if i >0:
            total = total+i
        else:
            continue
    return total

t1 = [3,-4,5,2,-9]
print(add_sum_of_positives(t1))
sps("_")
for index, num in enumerate([1, 1, 2, 2, 5]):
  if index < num:
    continue
 
  print(num)

#-----------------------------#
#             ARGV            #
#-----------------------------#

#Argv stands for argument variable, it is used by our terminals for some stuff
#Here are some implications of why you might need it:

import sys

print(sys.argv)
