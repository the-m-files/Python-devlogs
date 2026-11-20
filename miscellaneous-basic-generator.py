#A generator object basically loads items lazily, meaning it only gives it upon request.
#you just can't read a generator object by looking at it because it is just a memory address
#you have to unpack it or get a certain value.

#here is an example of a generator object

#dont worry about this function, you will understand it later
def square(input):
  for i in range(0, input+1):
    yield i**2 #this is what makes the generator object instead of return

generator = square(10)
print(generator)
print(next(generator)) #requests the value and goes and gets it
print(next(generator))
print(next(generator))

#this is obviously a bad way becuase it is taking to much work.
#we can unpack this into a list and print it all out at the same time:

print(list(generator))