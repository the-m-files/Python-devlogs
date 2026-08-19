#-----------------------------#
#           INSERT            #
#-----------------------------#

# the insert method will let you put an item inbetween objects in a list. This means you can change a list without replacing objects

task = list(("Wake up", "Brush teeth", "Walk"))

#here is an example of it in in use:

task.insert(2, "Eat")

print(task)

#-----------------------------#
#           EXTEND            #
#-----------------------------#

#to combine two different lists into one bigger list we can use the extend method

movies = ["Coco", "Ferdinand", "Nemo", "Cars", "Toy story", "Moana"]
newmovies = ["Shrek", "Puss in boots", "Kung fu panda"]

#to add new movies to movies we can use the extend method like below:

movies.extend(newmovies)
print(movies)

#so ass you could have seen we have added all elements from newmovies to movies.

#-----------------------------#
#           REMOVE            #
#-----------------------------#

fruits = ["Apples", "Bananas", "Oranges", "Kiwi", "Mango"]

fruits.remove("Kiwi")
print(fruits)

#Notice: the remove will only remove the first occurence of the element. it will stop at after that

numbers = [1,3,2,5,6,8,2,4]

numbers.remove(2)
print(numbers)



#-----------------------------#
#             ADD             #
#-----------------------------#

#the append method will let you add elements to a list

numbers = [1,2,3]

numbers.append(4)
numbers.append(5)
print(numbers)

#notice though you can only add one item at time

#to over come this you can either use the extend method, or something like this:

numbers += [6,7,8,9]

print(numbers)

#this works like the extend under the hood tho.