number = "555 000 555 002"
#These lines bellow show us how strings behave when put in rpelace finctons. It did its job but it didn't change the original string
#TO do that we have to re assign it again to the var.
print(number.replace(" ", "-"))
print(number.replace("5", "*"))
print(number)

#This section we will talk about the format funciton
#Here is a simple demo on how it works:
sentence = "I am a {}, I love {} and {} which is also my friend"
#If you give too little, it will raise an error but it will not care if there is more than the number of braces available
print(sentence.format("Dog", "kids", "icecream"))

# You can alter the order of words by listing indexes.
sentence = "I am a {0}, I love {1} and {2} which is also my friend"
print(sentence.format("Dog", "kids", "icecream"))
#-------------------------------------------------------------------#
sentence = "I am a {1}, I love {0} and {2} which is also my friend"
print(sentence.format("Dog", "kids", "icecream"))

#You can make keywords that will work like attributes
#-------------------------------------------------------------------#
sentence = "I am a {noun}, I love {food} and {item} which is also my friend"
print(sentence.format(noun = "Mug", food = "Hot dog", item = "Totem" ))

#---------------------------------------------------------------------------------------------#
#IF CONDITIONAL STATMENTS START HERE!!!
#---------------------------------------------------------------------------------------------#

#If conditions basically check if a group of code will evaluate to a bool. if the bool is true it will run and if not it will not

if 3>1:
    print("3 is greater that of one")

if type(number) == str:
    print(f"{number} is a string")

if 1 == 1:
    print("1=1")

if "Jon" == "jon":
    print("this will not run")

#-------------What are truthy/falsy values?---------------#

#any number except zero is a truthy bool

if 3:
    print("this has run. 3 is truthy")

if -2:
    print("this will run. -2 is a truthy value")

if 0:
    print("this will not run. 0 isn't truthy")

#any string that isn't empty is truthy

if "adlkg":
    print("adlkg is truthy.")

if "":
    print('this didnt print')

#Instead of finding out wether something in python is truthy/falsy we can use the bool function

print(bool(0))
print(bool(1))
print(bool("hello"))
print(bool(""))
print(bool(3.145232))


#There are things called else statements in python. They are activated when the if condition they are chained with isn't true

if 3>5:
    print("this is false")
else:
    print("three is not greater than 5")

if 0:
    print("hello, this is a falsy value")