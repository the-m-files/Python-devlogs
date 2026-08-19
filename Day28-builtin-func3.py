#-----------------------------#
#           LAMBDA            #
#-----------------------------#

#the lambda method is a way of defining single use functions that are light weight
#this is moslty combined with either filter or map

#this is one way:
def count1(word):
    return len(word)>5

list1 = ["Hello", "xdalf", "waeoi", "hoae11"]

print(list(filter(count1, list1)))

#this is the one usong lamda

print(list(filter(lambda count: len(count)>5, list1)))

#here is an anatomy of the lambda function:

#1.) lamda is the first thing you put like def for a regular function
#2.) then the attribute such as "count" in line 18 followed by a :
#3.) and finally the opperation. notice that this should be a single expression and if not it wont work

print("-"*25)
#here is an example that will return all elements from a list that have p in them

#original way:

names = ["riley", "robert", "brinda", "bob", "Baily", "annie", "Rie"]

def checkp(word):
    return "r" in word
print(list(filter(checkp, names)))

#using the lambda method:

print(list(filter(lambda name: "r" in name, names)))

print("-"*25)
#there are some flaws with using the lambda method because you cant call it later in your program
#but it is also really compact and neat to look at.

#not only can you use lambda in filter you can also use it in map

#here is the orginal way to check the len of each word:

#original:

def count(word):
    return len(word)

print(list(map(count, list1)))

#lambda:

print(list(map(lambda word: len(word), list1)))

#as you can see this is really good for compact one line.

#here is one final example:

print(list(map(lambda repl: repl.replace("r", "#"), names)))


#this example will return the elements in a list that will equal to number you typed in
def right_words(words, number):
    
    return list(filter(lambda word: len(word) == number, words))

print(right_words(names, 3))
print("-"*25)


#-----------------------------#
#             ALL             #
#-----------------------------#

#the any function will make it so that it will return a true or false value to an iterable datastructure based on if it is truthy/falsy
#here is it in action:

example1 = [True, True, True]
print(all(example1))

example2 = [1, 2, 3, 5, 4]
print(all(example2))

#notice how ther is one zero which is a falsy value? so it is false
example3 = [1, 4, 2, 0, 5]
print(all(example3))

example4 = ["Hello", "4", "e"]
print(all(example4))

#As soon as it sees one false/falsy value the entire list becomes false

#-----------------------------#
#             ANY             #
#-----------------------------#

#this is really really similar to the all function but will return true even when there is only one true/truthy value in a list

print(any(example1))
print(any(example2))
print(any(example3))
print(any(example4))
print('-'*25)
#so as you could have seen this is just the all function with a not in front of it

#-----------------------------#
#             MAX             #
#-----------------------------#

#the max function like its name will return the biggest value in a list

example5 = [1, 3, 52, 6, 0, 4]

example6 = ["alpha", "beta", "gamma", "delta", "epsilon", "ilios", "kappa"]
print(max(example5))

print(max(example1))

print(max(example3))

#when you put words into a max function it checks what is the letter closest to z

print(max(example6))

#-----------------------------#
#             MIN             #
#-----------------------------#

#the min function is the polar opposite of the max function

print(min(example5))

print(min(example1))

print(min(example3))

print(min(example6))

print("-"*25)

#-----------------------------#
#             SUM             #
#-----------------------------#

#the sum method will add every element in a list together

numbers = [1,56,3,7]

print(sum(numbers))

numbers2 = [1.53, 6.25, 2.564, 7, 9.54, 0.2]

print(sum(numbers2))

#notice: you cant add words/strings or any other data structures after numbers

