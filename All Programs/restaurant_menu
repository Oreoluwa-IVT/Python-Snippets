from tkinter import *
class Restaurant_Menu(Frame):
    """A GUI for a Restaurant Menu"""
    def __init__(self,master):
        super(Restaurant_Menu,self).__init__(master) #super here also mean super class, it take the class name and the type alont with it's on init initialized as master
        self.grid() # this are simply attribute
        self.bttnclk=0
        self.widgetlayout() 
        
    def widgetlayout(self):
        self.bttn=Button(self)
        self.bttn["text"]="Total Clicks: 0" #The text option was used here to give the button text
        self.bttn["command"]=self.keepcount #The command option is used to help invoke the "keepcount()" method once the button is clicked
        self.bttn.grid()
        
    def keepcount(self):
        """Display's the Restaurant Menu once the button is clicked"""
        self.bttnclk +=1
        self.bttn["text"]="Total Clicks: " + str(self.bttnclk)



root=Tk()
root.title("Restaurant Menu")
root.geometry("400x400")

app=Restaurant_Menu(root)

root.mainloop()