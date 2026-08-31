#-----------------------------#
#            REMOVE           #
#-----------------------------#

#the remove method is a way to remove one specific element from a set, it will raise an error if it isn't there in the set.

Weather = {"Sunny", "Rainy", "Snowy", "Cold"}
Weather.remove("Cold")
print(Weather)

#here is an example if it cannot find it:

if "Gold" in Weather:
    Weather.remove("Gold")
else:
    print("Not Found")


#-----------------------------#
#           DISCARD           #
#-----------------------------#

#as said before this is highly similar to Remove, but will not raise an error if it can't find something in a set

Weather = {"Sunny", "Rainy", "Snowy", "Cold"}

Weather.discard("Sunny")
print(Weather)

Weather.discard("kdfa;")
print(Weather)

Weather.discard("COLD")
print(Weather)

#notice it didn't raise an error, and just failed silently?
#use this whenever you don't want the program to raise an error while working with sets.

#-----------------------------#
#         INTERSECTION        #
#-----------------------------#

#the intersection method is for checking if the same items are present in two different sets

#we can use either the & symbol or the .intersection(seta, setb)

Day1 = {"Pancake", "Chicken Rice", "Soup"}

Day2 = {"Soup", "Burrito", "Mac and Cheese"}   

#to see what is common between day1's diet and day2's diet we can use either method one or two:

print(Day1.intersection(Day2))

#but instead of this we can also use the & symbol

print(Day1 & Day2)

#python will only check if they are equivilant not equal so floats and ints are going to show up like this example below:

set1 = {1.0,2.0,3.0,5}
set2 = {1,2,3,4}

print(set1 & set2)

#-----------------------------#
#            UNION            #
#-----------------------------#

#the union method is similar to the update method from dicts and lists.

#here are some examples of how they are used:

class1 = {"Gary", "Shay", "Mario", "Carlos"}

class2 = {"Marla", "Cameron", "Steve", "Alex"}

students = class1.union(class2)

#the union method will not add duplicates if it finds them.

students = sorted(students)
print(students)

#like the intersection method this also has a character to do the same job: 
#as an alternative you can use | the strait character instead of the union method

deserts = {"Cake", "Shake", "Icecream"}
lunch = {"Chicken Rice", "Clam Chowder", "Soda"}

order = deserts | lunch

print(order)

#-----------------------------#
#          DIFFERENCE         #
#-----------------------------#

#the difference is opposite of the intersection, it will identify whatever elements are not common between sets
#okay here is how it is:

Day1 = {"Pancake", "Chicken Rice", "Soup"}

Day2 = {"Soup", "Burrito", "Mac and Cheese"}   

#this is aksing what elements from day2 are different from day1
print(Day2.difference(Day1))

#this is aksing what elements from day1 are different from day2
print(Day1.difference(Day2))

#note as a bonus you can also do this:
#which is also the same thing
print(Day1-Day2)