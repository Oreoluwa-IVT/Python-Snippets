#Defining a class
#Simple Critter
#Demonstrates a basic class and object 


class Critter(object):
    """A virtual pet"""
    def talk(self): # it compulsory that the methods of a class have a default parameter. " in this case I decided to call it self"
        print("Hi. I'm an instance of class Critter")
    def okay(self):
        print("3x3 is: ",3*3)


#main
crit=Critter()  # this is called instantiation
now=Critter()
crit.talk()
crit.okay()
print("We just used created ")
now.talk()
now.okay()

input("\n\nPress the enter key to exit.")

