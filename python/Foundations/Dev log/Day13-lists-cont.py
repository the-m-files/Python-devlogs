#We will continue form were we left off yesterday. Which was extracting elements and their letters
#now we can extract slices of strings like lists
fruits = ["Apple", "Banana", "Cantaloup", "Dragon Fruit"]
letter = ["a", "b", "c", "d", "e", "f"]
print(fruits[0:3])
print(fruits[-1:2])
print(fruits[-1::])
print(fruits[1:100])
print(fruits[::-1])

def split_in_two(lis, val):
    return lis[2:] if val % 2 == 0 else lis[:2] 

