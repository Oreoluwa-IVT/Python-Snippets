# playing Cards
# Demonstrates combining objects

#Playing Cards
#Demonstrates combining objects

class card(object):
    """A playing card."""
    RANKS=["A","2","3","4","4","6","7","8","9","10","J","K",]
    SUITS=["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        rep=self.rank +self.suit
        return rep


now=card("A","b")
print(now.RANKS)
print(now.SUITS)
print(now.rank)
print(now.suit)


#note: a class name and an object can access class attributes 
#onte: only a class name can access private class attribuites
#note:for an object to access private attributes, it has to use the class name starting with and underscore. the privaate attributes
