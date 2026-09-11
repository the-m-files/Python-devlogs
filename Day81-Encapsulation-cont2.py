#-----------------------------#
#     PROPERTY ALTERNATIVE    #
#-----------------------------#

#in the last lesson we saw how we used property, since it was a decorator we could just use the @ short hand.

#here is an example of a class that uses cents internally but dollars externaly:

class Currency():
    def __init__(self, dollars):
        self._cents = dollars*100


    #in the last lesson we converted this into a "hidden method" and passed it into the property() method as input
    #since the short hand exists, we can simply do this:
    @property
    def dollars(self):
        return self._cents/100


#so this will work now:
bank1 = Currency(10000)
print(bank1.dollars)

s = "Race car"
print(s.replace(" ", "").lower().strip())
print(reversed(s.replace(" ", "")))
print(tuple(s.replace(" ", "").lower().strip()) == tuple(reversed(s.replace(" ", "").lower().strip())))
