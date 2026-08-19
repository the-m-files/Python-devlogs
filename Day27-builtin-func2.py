#-----------------------------#
#           FILTER            #
#-----------------------------#

#the filter function will take an iterable object and repeat a function on it and 
#give you the truth and false(if not applicable it will give truthy/falsy values)

words = ["Song", "Book", "literature", "Library", "student"]

def longerthan5(word):
    return len(word)>5

print(filter(longerthan5, words))

#you should not put () after the function

#just like the map function to see it you have to convert it to a list or run each value through a for loop and print it out individually

#method one: 
print("-"*25)

for item in filter(longerthan5, words):
    print(item)

print("-"*25)

#method 2:
print(list(filter(longerthan5, words)))


#this can also be used to clean a data set without work

bad_data = [0, "Apple", "", "Banana", False, None, "Cherry"]

# Remove empty strings, zeros, and None
clean_data = list(filter(None, bad_data))

print(clean_data)  # Output: ['Apple', 'Banana', 'Cherry']

