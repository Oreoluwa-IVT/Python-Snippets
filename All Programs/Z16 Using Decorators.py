#Classy Critter 
#Demonstrates class attributes and static methods

class Critter(object):
    """A virtual pet"""
    total=0

    @staticmethod # this is called a decorator . It simply creates a static method
    def status():
        print("\nThe Total number of critters is",Critter.total)

        #notice that the status method doesn't have the self paramter. This is because
        #the status method is only meant to be invoked through a class and not an object
    
    def __init__(self,name):
        print("A Critter has  been born!")
        self.name=name # this is by default , a public attribute. meaning that it can be accessed from outside the code directly. Check for private atrribuite in "Back to basics 52"
        Critter.total +=1

#main
print("Accessing the class attribute Critter ,total",end="")
print(Critter.total)

print("\nCreating critters.")
crit1=Critter("critter1")
crit2=Critter("critter2")
crit3=Critter("critter3")

Critter.status()
print("\nAccessing the class attribute through an object:",end="")
print(crit1.total)

input("\n\nPress the enter key to exit.")