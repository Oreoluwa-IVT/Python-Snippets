#Private Critter 
#Demonstrates private attributes and methods

class Critter(object):
    """A virutal pet"""
    def __init__(self,name,mood):
        print("We have arrived")
        self.name=name  # this is pubic attribute
        self.__mood=mood # this is a private attribute ( the two underscores show that it's a private attribute)
    
    def talk(self):
        print("\nI'm,",self.name)
        print("\nI'm",self.__mood)


crit=Critter(name="Oreoluwa",mood="happy") 

print(crit.talk())
print(crit.name)

#here we tried accessing a private attribute, but I decided to introduce a try catch. So I don't generate weird errors
try:
    print(crit.mood)
except:
    print("\n\nNice Try. you can't access a private attribute")

input("\n\n\n\n\nPress the Enter key to exit")



# But here's the fun part , you can actually access a private attribute. But you'd have to pull a few strings to do that

print(crit._Critter__mood)



    
