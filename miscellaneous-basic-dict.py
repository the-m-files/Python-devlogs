#dicts are literally just real life dicts but they work a bit differently

#here are the quilifactions to a dict:

#1.) dicts don't have index values, they are sorted by key-value pairs.
mydict = {"home":12, "games":2}

#to add something to a dict we can use these handy syntaxes:

mydict["play"] = 14

#we can also use the setdefault method to get some value from a dictionary but also add it on the fly

mydict.setdefault("math", 0) #finds math if finds it then returns that value, if not then return 0
#also would add the value math:0 to the dict on the fly so the next time it doesn't add it.

#to remove something from a dict we can use the pop method or remove method

#i know I said that the dict doesn't have an index, but python uses an internal index value list to calculate stuff
#here is how pop would work:

subjects = {
    "math":2,
    "ela":2,
    "science":1,
    "music":0.5,
}

subjects.pop(-1) #removes the last item

print(subjects)

#to add multiple elements to a dict, we can use the update method similar to the lists

subjects.update({"health":0.2, "robotics":1.3, "PE":2.1})

print(subjects)