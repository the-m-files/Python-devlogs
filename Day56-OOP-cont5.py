#-----------------------------#
#   SOFTWARE ARCHITECTURE     #
#-----------------------------#

# Today I focused less on writing code and more on planning.

# I learned that large programs should be split into parts where
# each part has a single responsibility.

# Planned architecture for dummy-os.py:

# Terminal
#   - Handles user input/output.

# FileSystem
#   - Manages files, folders, and navigation.

# Folder
#   - Stores files and subfolders.

# File
#   - Stores file data and contents.

# I also learned that the FileSystem should create files and folders,
# while the Terminal should only forward commands from the user.

# Even though I didn't write much code today, I designed how the
# program should be organized before implementing it.

#-----------------------------#
#          @PROPERTY          #
#-----------------------------#

#this is a decorator that lets methods behave like attributes. highly helpful for idk situations

class employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{self.fname}.{self.lname}@gmail.com"

#the problem with this is the fact that when you re-run/re-assign an attribute's value

vjy = employee("Congobongonobo", "Bok")
vjy.fname = "Boogoo"
print(vjy.email)
print(vjy.fname)
print("-"*25)

#to get over this we can make email into a method
#the porblem with this is because then you would have to add a () after every email you typed
#since that isn't optimal we can use the @PROPERTY decorator

class employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        self.email = f"{self.fname}.{self.lname}@gmail.com"

vjy = employee("Congobongonobo", "Bok")
vjy.fname = "Boogoo"
print(vjy.email)
print(vjy.fname)
    