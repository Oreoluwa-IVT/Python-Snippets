#We are going to be showing the concept of inheritance in this program
#first we start be creating a few classes
#Then lastly, we create one mself class that inherits the attributes and methods of the other classe


class Card(object):
    RANKS=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS=["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        rep= self.rank+self.suit
        return rep
    

class Hand(object):
    """ A hand of playing cards"""
    def __init__(self):
        self.cards=[]

    def __str__(self):
        if self.cards:
            rep=""
            for card in self.cards:
                rep+=str(card)+ "\t"
        
        else:
            rep="<empyty>"
        return rep

    def clear(self):
        self.cards=[]
    
    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
                
    

    # we are about to create a new class called Deck. Deck will be a derived
    #  class simply because it's going to inherit of all Hands methods and attributes

class Deck(Hand):
    """A deck of playing cards"""
    def populate(self): # notice that there isn't any constructor method present in Deck simply  because already inherits the constructor from the Hand class           
        for suit in Card.SUITS:
            for rank in Card.RANKS: # remember that class names are used to access class attributes
                 self.add(Card(rank,suit))
        
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,hands,per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_cards=self.cards[0]
                    self.give(top_cards,hand)  #take time to under this code , it's a bit tricky but you'd get it. pay attention fo methods "give and deal". notice 
                    #the

                else:
                    print("Can't continue deal. Out of cards!")
                    



#main 
deck1= Deck()
print("Created a new deck")
print("Deck:")
print(deck1)


#since the deck is empty, we are going to populate the deck with the created populate method


deck1.populate()
print("\nPopulated the deck.")
print("Deck:")
print(deck1)

print("\nShuffle of the deck")
print("Deck:")
print(deck1)

my_hand=Hand()
your_hand=Hand()
hands=[my_hand,your_hand]

deck1.deal(hands,per_hand=5) # take the number of hands and the number of cards to give each hand

print("\n\n\n\n\n\nHand 1",my_hand,"\n\n")
print("Hand 2",your_hand,"\n\n")
print("Deck 3",deck1,"\n\n")



deck1.clear()
print("\nCleared the deck")
print(deck1)


print("Deck:", deck1)
input("\n\nPress the enter key to exit")