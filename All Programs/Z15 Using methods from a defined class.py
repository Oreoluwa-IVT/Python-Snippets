#Using Attributes 

#Atrribue Critter
#Monstrates creating and accessing object attributes

class Critter(object):
    """A Virutal pet"""
    def __init__(self,name):
        print("A new critter has been born!")
        self.name=name

    def __str__(self): # this part of the program is printed when you try to print an object
        rep="Critter object \n"
        rep+="name:"+ self.name + "\n"
        return rep

    def talk(self):
        print("Hi, I'm",self.name, "\n")

#main
first=Critter("Gbemisola")
first.talk()

second=Critter("Jadesola")
second.talk()

print("Printing Crit1")
print(first)


print("Direclty accessing first.name")
print(first.name)

input("\n\nPress the enter key to exit")
