

def fizbuz(a):
    x = 0
    while x != a:
        x += 1
        if x%3 == 0 and x%5 == 0:
            print("fizbuz")
        elif x%5 == 0:
            print("buz")
        elif x%3 == 0:
            print("fuz")
        else:
            print(x)


fizbuz(30)          
print("-"*20)

def countdown(n):
    # 1. Base Case (The exit condition)
    if n <= 0:
        print("Blast off!")
        return 
        
    # 2. Action step
    print(n)
    
    # 3. Recursive Case (Call itself with a smaller input)
    countdown(n - 1)

countdown(5)


print("-"*20)

def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        #print(a*(factorial(a-1)))
        return number*(factorial(number-1))

print(factorial(4))