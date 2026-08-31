#-----------------------------#
#     SYMMETRIC_DIFFERENCE    #
#-----------------------------#

#this is like comparing two sets and returning all the elements that are not common between the two sets

#as like the previous lessons here are the syntax:

#1.) the symetric_difference method

Movies = {"Harry Potter", "Interstellar", "Toy Story 1"}
Books = {"Harry Potter", "Fresh Ink", "All American Boys"}

print(Movies.symmetric_difference(Books))

#2.)

Movies = {"Harry Potter", "Interstellar", "Toy Story 1"}
Books = {"Harry Potter", "Fresh Ink", "All American Boys"}

print(Movies ^ Books)

#-----------------------------#
#           ISSUBSET          #
#-----------------------------#

#this is a method you can use to check if a set is a sub set of another set
#here is an example:

even = {2,4,6,8}
integers = {0,1,2,3,4,5,6,7,8,9,10}

#we know even numbers are integers so they are in the integers making them a subset:
print(even.issubset(integers))

#to use the shorthand we can use either <=(this means will return true even if bot sets are the same) or <

numbers1 = {1,2,3,4}
numbers2 = {1,2,3,4}
print(numbers1 <= numbers2)
print(numbers1 <= numbers2)

#true (equivilant to <=):
print(numbers2.issubset(numbers1))
#false:
print(numbers1 < numbers2)
print("-"*25)

#-----------------------------#
#         ISSUPERSET          #
#-----------------------------#

#think of this as the opposite of Issubset. it checks if a larger set contains a smaller set

print(numbers1.issuperset(numbers2))

seta = {1,2,3,4,5,6,7,8,9,10,11,12,13}
setb = {5,2,1,6}

print(seta.issuperset(setb))

#like the issubset this also has a short hand which is > and >=

print(seta > setb)
print(seta >= setb)
print(numbers1 >= numbers2)
print(numbers2 > numbers1)