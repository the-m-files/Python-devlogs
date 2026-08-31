#-----------------------------#
#          __name__           #
#-----------------------------#

#this is a dunder method and all modules created will automatically have one pre-created with a value:
import math
print(math.__name__)

math.__name__ = "NERD"

print(math.__name__)
print(dir(math))

#but these are okay but what would you need these for?
#well, since this cannot be demostrated in this file please go to the modules folder

#-----------------------------#
#        FROM, IMPORT         #
#-----------------------------#

#this is going to teach us how to import only the functoins we need from other modules using the from keyword

from math import ceil, floor, tan

#so now only these tree functions are goin to work because we didn't add the others to the shared namespace.
print(math.ceil(10.3))
print(math.tan(23))
print(math.floor(32.1))

#but notice, since we are only importing part of it we don't need to add math so it can simply be like these:
print(ceil(13.1))
print(floor(3.1))
print(tan(12342))

#okay, but what if you want it so that you import all the modules seperatly
#so that you don't have to type the module name every time
#to do that we can use from x_module import *
# the asterisk imports everything from x_module

from string import *
#so now this becomes possible:
print(ascii_letters)
print(ascii_lowercase)
print(punctuation)