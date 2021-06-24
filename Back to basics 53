# Creating a private method
#to to do this , all you have to do , is add two underscores to the name of the method

class now(object):
    """Demonstrating a few private methods"""

    def __init__(self):
        print("This is constructor. It runs once the class instantiated")
    
    @staticmethod
    def now():
        print("This is a static method. It is invoked only by the Class name")
    
    def __private(self,okay):
        self.okay=okay # Remember this is a public attribute. it can be invoked by the class and the object outside of the class definition
        print("This is called a private method",okay)


    #this is how to access private methods within a class 
    
    def newmethod(self):
        print("This is a new method")
        self.__private("Johnson")  #this is how you access a private method in a class | this simply means that the  method will run once 
        # once newmethod is called 




#main
crit=now() # crit object was instantiated here
print(crit._now__private("Oreoluwa \n\n")) # are accessing the private method " __private()"
print(crit.newmethod())

