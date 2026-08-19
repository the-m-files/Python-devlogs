alphabet = "abcdefjhijklmnopqrstuvwxyz"
print(alphabet[::-1])


def first_three_characters(word):
    return word[:3]



print(first_three_characters("helloafda"))

#Today we have learned that we can use one more thing to this string slicing
#We can skip over a limited amount.
#For example look at line 16. You can see that we are skipping by 2. We can also use negative numbers to reverse the direction such as in line 2

print(alphabet[::2])

#While using strings we may want some stuff to print on different lines. So we can use "/n" to make that happen.
print("--"*10)
print("Sheakspeare wasn't the greatest poet...  \nHe was the one who defined greatest poets.")
#A problem that still exists is to use qoutes without syntax errors. To do that look bellow
print("\"May the end of saparta be the end of civilization\" said Horace")

#a new problem arises from this, how will you print website links?
#to overcome this we will convert this to raw string.

rawstring = r"c://Mahathish/desktop/python"
print(rawstring)

#To find a specific item/group of characters from a string you can use the "in" keyword
print("a" in alphabet)

#You can also use the "not" keyword with the "in" keyword to inverse this
print("#" not in alphabet)
print("destiny"[:4])

#------------------------------------------------------------------------------------
#CHAPTER 7 STARTS HERE
#------------------------------------------------------------------------------------

# Find method like the "in" keyword, this will also return the index of where it is. if it doesn't exist it will say -1
print(rawstring.find("//"))