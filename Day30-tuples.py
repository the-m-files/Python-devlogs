#-----------------------------#
#       UNPACKING TUPLES      #
#-----------------------------#

person = ("Alex", 16, "Canada")

name, age, country = person

print(name)
print(age)
print(country)

#instead of using indexes like person[0], person[1], and person[2]
#you can unpack the tuple into separate variables

coordinates = (15, 42)

x, y = coordinates

print(x)
print(y)

#the number of variables must match the number of values in the tuple

#this will cause an error:
#x, y, z = coordinates

#you can also swap variables using tuple unpacking

a = 10
b = 20

a, b = b, a

print(a)
print(b)

#this is much shorter than using a temporary variable

#tuple unpacking is commonly used when functions return multiple values
#or when looping through dictionaries and lists of tuples

employee = ["Oompa", "loompa", "5", "managaer"]

fname, lname, age, role = employee

#you can also fit more than one value in a variable like a list:

fname, lname, *details = employee

#* the asterisk means that it will take the rest of the values
#but can only be used once
print(details)
