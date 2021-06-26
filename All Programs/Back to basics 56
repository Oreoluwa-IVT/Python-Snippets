#Alien Blaster 
#Demonstrates object interaction

class Player(object):
    """A player in a shooter game"""

    def __init__(self):
        """this is a constructor"""
        print("Hey guys, Player")
    
    def blast(self,enemy):
        print("The player blasts an enemy")
        enemy.die()

class Alien(object):
    """An alien in a shooter game."""
    def die(self):
        print("The alien gasps and says, 'Oh, this is it . This is the big one. \n"\
            "yes, it's getting dark now. Tell my 1.6million larvae that I loved them... \n"\
                "Good-bye, cruel universe.' ")


#main
print("\t\tDeath of an Alien \n")
hero=Player()    #hero is the first object
invader=Alien()   #invader is the second object
hero.blast(invader) #the two objects send each other messages heres

input("\n\nPress the enter key to exit")


#Note that the relationships behing these object communicating by sending and receiving messages via calling their 
#method is simply the beauty of OOP