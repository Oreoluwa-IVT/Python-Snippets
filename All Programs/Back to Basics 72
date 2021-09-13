#Building a Restraurant Menu with GUI
from tkinter import *

class Restaurant_Menu(Frame):
    """A GUI application with A Restaurant Menu."""
    def __init__(self,master):  #this is a constructor, it executes the moment the class is instantiated
        """ Initialize the Frame. """
        super(Restaurant_Menu,self).__init__(master) #This help intiate the constructor of the base class 
        self.grid() #this helps us add a grid to every widget
        self.create_widgets() #this instantiates the create_widgets class defined later in this program
    
    def create_widgets(self):
        """ Create three buttons that do nothing."""
        self.button1=Button(self,text="1") #the widgets have to be stated with the self.variable format
        self.button1.grid()
        
        self.button2=Button(self,text="2")
        self.button2.grid()
        
        self.button3=Button(self,text="3")
        self.button3.grid()
        
        self.button4=Button(self)
        self.button4.config(text="4")
        
        
        
        
root =Tk(); #this is a class for the tkinter library used o create GUIs
root.title("Restaurant Menu") #this gives the GUI a label 
root.geometry("600x400")# This defines the dimension of a GUI

app=Restaurant_Menu(root) #Wll widget need to a frame, there for we initialize the root object in the frame method.
app.grid() #this is a method that all widgets must have
lbl=Label(app,text="Our List of Exotid Foods".title()) # this are more like texts in the GUI
lbl.grid() # All widgets, just like this one here , must have the grid() attached

button1=Button(app)
button1.grid()
button1.configure(text="Display Menu")
#alternative button1["text"]="Display Menu"

root.mainloop()# this creates a loop to prevent the appication from closing
