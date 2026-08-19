#from the last lesson we realized, we can find certain characters in string, But it stopped after finding the first instead
#of giving all instances of it. We can slightly over come this by skipping certain parts

exstr = 'autocracy is greate for bad actions yet useless against goals'

print(exstr.find("a"))
print(exstr.find("a", 3))
print(exstr.find("X"))

#THere is also another method called, index which acts similar but will raise an error instead of -1.
print("-"*10)
print(exstr.index("a"))
print(exstr.index("ate"))

#Then there is rfind. the big brother of find.
#unlike find rfind is different because it lets you define where to start and when to end. It will also return the highest index
#occurence of the character(s).

text = "apple, banana, cherry, apple, orange"
index = text.rfind("apple")
print(index) 
index = text.rfind("apple", 0, 20) 
print(index) 
# Output: 23

text = "hello world"
print(text.rfind("python")) 
# Output: -1

#The starts with method will help you identify wheter a string starts with a certain characters
print("starts_with:",  exstr.startswith("autocracy"))
print("starts_with:",  exstr.startswith("Autocracy"))

#The ends with method will tell you wheter a string ends with a certain character(s)
print("ends_With: ", exstr.endswith("goals"))
print("ends_With: ", exstr.endswith("Goals"))

#To check how many times a charachter has been used in a string we can use the count method
print(text.count("l"))
print(text.count("blow"))

#To capitalize the first letter of a string you can do this:
print(text.capitalize())
#this one capitalized every word:
print(text.title())
#this one capitalizes everything:
print(text.upper())
#this one makes everythin lower case:
print("HELLO".lower())
#this one swaps the cases:
print("Hi THiS lIve".swapcase())
#P.S you can mix these:
print("BEN FRANK".lower().title())