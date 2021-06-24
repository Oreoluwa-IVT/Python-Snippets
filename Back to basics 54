# Controlling Access to private attributes

#Property Critter
#Demonstrates properties 

class Critter(object):
    """A new class uhmm"""
    def __init__(self,name):
        print("Welcome to the divine access",name)
        self.__name=name
    
    @property
    def name(self):
        return self.__name
        # this property is simply placed here to allow indirect access to the attribute "main"
    
    @name.setter # this is calle a decorator
    def name(self,new_name):
        if new_name=="":
            print("A Critter's name can't be the empty string")

        else:
            self.__name = new_name  #----------------------- >|
            print("Changed my dear")   #                      |
                                       #                      |
                                    #                         |
                                    #                         |
                                     #                        | 
                                     #                        |
#main                                                         |
new=Critter("Oreoluwa")              #                        |
print(new.name)                       #                       |
new.name="Randolph" # you this is how you change an attribute |
print(new.name)

input("\n\nPress the Enter key to exit")



