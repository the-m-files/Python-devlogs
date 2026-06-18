#this is a continuation of last video. This is more focused on boolean values as returns.
alphabet = "abcdefghijklmnopqrstuvwxyz"
lower = "hello world"
upper = "HELLO WORLD"
sentence = "Goodness, me! It has been 7 days since we started."
title = "Hello Gerald!"
favnum = "100"

#here are some examples:
print(sentence.islower())
print(lower.islower())
#-----------------------
print(sentence.isupper())
print(upper.isupper())
#-----------------------
print(sentence.istitle())
print(title.istitle())
#-----------------------
print(sentence.isalpha())
print(alphabet.isalpha())
#-----------------------
print(alphabet.isnumeric())
print(favnum.isnumeric())
#-----------------------
print(title.isalnum())
print(alphabet.isalnum())
#-----------------------
print("S".isspace())
print(" ".isspace())

#This section, we will learn a form of edidting strings(note: you can't edit strings, they are immuntable only make new ones)

st1 = "        3333Yes---               "
#this will remove the empty spaces from the left.
print(st1.lstrip())
#this will remove the empty spaces from the right.
print(st1.rstrip())

#By giving certain key words you can target to eliminate certain characters:
print(st1.lstrip("3"))