#alrighto, we are at sets now!

#so sets in python are basically just a combination of unordered items, meaning that they don't have
#index values.

#these are the requirements of a set:

#1.) their values have to be hashable(meaning be able to be decoded or immutable)
#2.) they can't have duplicates
#3.) they have higher memory requirements because they use dict like structures within them

#to add an element in a set we can do this:

myset = set(1, 3, 4)

#myset = {1, 3, 4} works too.

myset.add(5) #this is going to be placed randomly because sets don't have indexes

print(myset)

#to add multile items at once we can use the update method:

myset.update([11, 34, 42]) #has to be similar to lists

#to remove something there are two choices:
nums = {10, 20, 30}

nums.discard(99)  # No error
nums.remove(20)   # Removes 20; nums is now {10, 30}



