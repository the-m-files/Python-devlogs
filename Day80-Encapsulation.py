
class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count
    
    def copyright(self):
        return f"Copyright {self._author}, {self._publisher}"
        
    def rip_in_half(self):
        if self.page_count>1:
            self.page_count = self.page_count/2
            return self.page_count
        else:
            self.page_count = 0 
            return self.page_count

book = Book(author = "Grant Cardone", publisher = "10X Enterprises", page_count = 10)

print(book.copyright()) # Copyright Grant Cardone, 10X Enterprises

print(book.page_count) # 10
book.rip_in_half()
print(book.page_count) # 5.0
book.rip_in_half()
print(book.page_count) # 2.5
book.rip_in_half()
print(book.page_count) # 1.25
book.rip_in_half()
print(book.page_count) # 0.625
book.rip_in_half()
print(book.page_count) # 0
book.rip_in_half()
print(book.page_count) # 0

#-----------------------------#
#         ENCAPSULATION       #
#-----------------------------#

#i know i have covered this earlier in the devlog but here i a second time because i have to watch it again:
#a setter and getter are like rules on how to use/acess attributes to objects.
#a setter lets you set the value of an attribute with confined rules such as it can't go below zero or above hundred else it will be set to None
#a getter is something that lets you see a value, imagine inside the object you are using metric system but since your fellow coders who code with you use american measurments you whenever someone wants to see a value you can automatically convert it to the american sustem

#off the bat we start to define a height class which uses inches internally but feet externally
class Height:
    def __init__(self, feet):
        self._inches = feet * 30.48  # Convert cm to inches

    #The getter method retrieves the height in feet by converting inches back to feet.
    #notice how it uses underscore? It means not to invoke it directly
    def _get_feet(self):
        return self._inches / 30.48  # Convert cm back to feet

    #The setter validates and sets the height, ensuring it's a non-negative value in inches.(it also uses underscore so it means not to call it)
    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 30.48  # Store height in cm
    
    #We create a property feet that combines the getter and setter methods, allowing for a clean interface.
    feet = property(_get_feet, _set_feet)


#so now, your code buddies who want to use the american measurement are happy and you who coded the internals is sane
h = Height(5)  # Initialize height as 5 feet
print(h.feet)  # Access the height in feet (outputs: 5.0)

h.feet = 6  # Set the height to 6 feet
print(h.feet)  # Outputs: 6.0