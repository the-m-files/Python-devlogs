#-----------------------------#
#        OPENING FILES        #
#-----------------------------#

#to open files we have to use a few methods, such as open, close and read but it is recommended to use with

with open("Foundations/Dev-log/dummytext.txt", "r") as loremipsum:
    print("you have opened dummytext.txt")
    loremipsum_var = loremipsum.read()
    print(loremipsum_var)

#with manages a resource for me and automatically cleans it up when I leave the block.

#since loremipsum is an iterable object it can be split up into lines

print("\n"*3)
with open("Foundations/Dev-log/dummytext.txt", "r") as loremipsum:
    for line in loremipsum:
        print(line)

#you may have noticed that there is some spacing between each line, that is becaues the print function's end attribute is set to \n

#-----------------------------#
#      WRITING TO FILES       #
#-----------------------------#

#to write something one a file using python it is alsmost the same as opening and reading files syntax

with open("Foundations/Dev-log/dummytext.txt", "w") as loremipsum:
    loremipsum.write("Hello World, Mahathish")

#note: if the file doesn't exist python will create one but if it exists it will replace that.

#here is an example of creating a file:

with open("Foundations/Dev-log/dummytext2.txt", "w") as creation:
    creation.write("Hello, this file is created\n")
    #to add a line break use \n
    creation.write("this is a new line \n")

#-----------------------------#
#           APPEND            #
#-----------------------------#

#the append method is similar to the write but it won't replace the entire thing, and simple just add on to it.

with open("Foundations/Dev-log/dummytext2.txt", "a") as append_example:
    append_example.write("This will be appended!")

