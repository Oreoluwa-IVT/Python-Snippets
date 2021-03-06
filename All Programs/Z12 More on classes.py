class Card(object):
    """A playing card."""
    RANKS=["A","2","3","4","4","6","7","8","9","10","J","K",]
    SUITS=["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        rep=self.rank +self.suit
        return rep


class Hand(object):
    """A hand of playing cards"""

    def __init__(self):
        self.cards=[]
    
    def __str__(self):
        if self.cards:
            rep=""
            for card in self.cards:
                rep +=str(card) + " "
        else:
            rep="<empty>"
            return rep
    
    def clear(self):
        self.cards=[]

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_card):
        self.cards.remove(card)
        other_hand.add(card)


#main
card1=Card(rank="A",suit="c")  # card1 is an object of the Card class
print("Printing a Card object:")
print(card1)



card2=Card(rank="2",suit="c")
card3=Card(rank="3",suit="c")
card4=Card(rank="4",suit="c")
card5=Card(rank="5",suit="c")

print(card2)
print(card3)
print(card4)
print(card5)


#Creating an empty hand object

yourhand=Hand()
print("\nPrint my hand before I add any cards:")

my_hand.add(card1)
