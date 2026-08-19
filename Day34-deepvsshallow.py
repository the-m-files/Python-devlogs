#-----------------------------#
#    SHALLOW VS DEEP COPY     #
#-----------------------------#

import copy

numbers = [1, 2, 3]

shallow = numbers.copy()

shallow.append(4)

print(numbers)
print(shallow)

#the copy() method creates a new list
#changing the new list will not affect the original list

#however things become different when there are nested lists

grades = [[90, 85], [70, 65]]

shallow = grades.copy()

shallow[0][0] = 100

print(grades)
print(shallow)

#both lists changed!
#this is because copy() only copies the outer list
#the inner lists are still shared between both variables

#this is called a shallow copy

deep = copy.deepcopy(grades)

deep[0][0] = 50

print(grades)
print(deep)

#deepcopy() copies everything
#the outer list and every nested object are duplicated

#changing the deep copy will not affect the original list

#use copy() for simple lists
#use deepcopy() when your list contains other lists or nested objects