#Invoking Base Class Methods
#Overiding a class
#Playing Cards 3.0
#Demonstrates inheritance - overriding methods

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



# We Practice overiding methods in a base class in this class below "Unprintable_Card"
class Unprintable_Card(Card):
    """A Card that won't reveal its rank or suit when printed"""
    def __str__(self):
        return "<unprintable>"

    # notice that this method "___str___" was also defined the Card class and it is also defined here as well. 
    # However, what happens here is , because we defined here also, it will overide the one defined in the base class

#Note: Fun Fact: Base class is also known as a super class

# Note:so you can say "Card" is a super class of the Positional_Card , Unprintable_Card class

now=Unprintable_Card(rank="A",suit="c")
print(now)

class Positionable_Card(Card):
    """A Card that can be face up or face down"""
    def __init__(self,rank,suit,face_up=True):
        super(Positionable_Card,self).__init__(rank,suit) #The first argument of super, "Postional_Card", tell python that you want to invoke the method of the base class to it.
        #the second argument "self", is simply a reference to the newly instantiatd Positionalbe_Card object so that all the code in the Card can get at the object to add the rank and suit attributes to it.
        #__init__ simply tells python that this is the method you want to invoke.
        self.is_face_up=face_up 

    def __str__(self): 
        if self.is_face_up:
            rep=super(Positionable_Card,self).__str__()
            #this part simply returns the __str__ method from the base class
        else:
            rep="XX"
        return rep 

    def flip(self):
        self.is_face_up= not self.is_face_up


#main
card1=Card("A","c")
card2=Unprintable_Card("A","d")
card3=Positionable_Card("A","h")

print("Printing a card object:")
print(card1)








print("\nPrinting an Unprintable_Card object:")
print(card2)


print("Printing the third card before flipping")
print(card3)

card3.flip()

print("\nPrinting the third card after flipping")
print(card3)

